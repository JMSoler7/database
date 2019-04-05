pipeline {
  agent any
  options {
     timeout(time: 10, unit: 'MINUTES')
     disableConcurrentBuilds()
  }
  triggers{
    bitbucketPush()
  }
  environment {
    SLACK_CHANNEL = 'database-ops'
    PYPI_FOLDER = 'django-calidae-database'
  }
  stages {
    stage('Compile images') {
      steps {
        slackSend(message: "Start: Jenkins Build (${env.JOB_NAME}) - <${env.RUN_DISPLAY_URL}| Follow execution>", channel: "${env.SLACK_CHANNEL}", color: '3333FF')
        sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml build --force-rm --no-cache node'
        sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml run -T node npm install --no-audit'
        sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml build --force-rm --no-cache django'
      }
    }
    stage('Launch linters') {
      parallel {
        stage('Front Linter'){
          steps{
            sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml run -T node npm run lint'
          }
        }
        stage('Django Linter'){
          steps{
            sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml run -T django python -m flake8'
          }
        }
      }
    }
    stage('Launch tests') {
      parallel {
        stage('Django tests'){
          steps{
            sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml run -T django env "DB_NAME=test" python ./manage.py test'
            sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml run -T django python ./manage.py migrate'
          }
        }
        stage('Front tests'){
          steps{
            sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml run -T node npm test'
          }
        }
      }
    }
    stage('Build and update pypi module') {
      when {
        branch 'master'
      }
      steps {
        sh 'cd $WORKSPACE/backend/ && bumpr -s $BUILD_NUMBER'
        sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml run -T node npm run build'
        sh 'pip3 wheel $WORKSPACE/backend/ --no-deps'
        sh 'scp *.whl root@pypi.calidae.net:/pippackages/django/$PYPI_FOLDER/'
      }
    }
    stage('Deploy to dev') {
      when {
        branch 'master'
      }
      steps {
        ansiblePlaybook(
          credentialsId: 'ansible_vault',
          limit: 'calidae.dev.database',
          playbook: '/opt/calidae/ansible/update.yml',
          extras: '-v'
        )
      }
    }
  }
  post {
    always {
      echo 'Stop docker machines'
      sh 'docker-compose -f $WORKSPACE/docker-compose.test.yml rm --stop --force'
      echo 'Cleaning environment'
      sh 'sudo chown --recursive jenkins:jenkins $WORKSPACE'
      cleanWs(cleanWhenAborted: true, cleanWhenFailure: true, cleanWhenNotBuilt: true, cleanWhenSuccess: true, cleanWhenUnstable: true, cleanupMatrixParent: true, deleteDirs: true)
    }
    success {
      slackSend(message: "Success: Jenkins Build (${env.JOB_NAME}) - <${env.RUN_DISPLAY_URL}| View execution>", channel: "${env.SLACK_CHANNEL}", color: '00FF00')
    }
    failure {
      slackSend(message: "Failure: Jenkins Build (${env.JOB_NAME}) - <${env.RUN_DISPLAY_URL}| View execution>", channel: "${env.SLACK_CHANNEL}", color: 'FF0000')
    }
  }
}

