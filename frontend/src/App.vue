<template>
  <div class="App u-height-screen u-flex u-flex-center">
    <h1 class="App__title u-text-center u-text-hairline">Hello world!</h1>
    <div class="App__footer u-text-uppercase u-text-hairline">
      Made by <span class="u-text-branding-primary">{{ author }}</span> with 💚
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      author: 'Calidae',
    }
  },
  mounted () {
    console.log(
      'Hello world!',
      'This is a sample component. Remove it and start coding!'
    )
  },
}
</script>

<style lang="scss">
$main-color: #888;

.App {
  background-color: #fafafa;
}

.App__title {
  color: $main-color;
  font-size: calc(3.5rem + 1.5vw);
}

/**
 * 1. We can access normandy-css variables from .vue files
 */
.App__footer {
  position: absolute;
  bottom: $global-spacing-unit; /* [1] */
  left: $global-spacing-unit; /* [1] */

  color: $main-color;
  font-size: 0.8rem;
  letter-spacing: 0.1ch;
}
</style>
