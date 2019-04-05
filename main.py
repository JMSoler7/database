from faker import Faker


class Person():

    name = Faker().name()

    def __str__(self):
        self.name = Faker().name()
        return self.name


if __name__ == "__main__":
    people = []
    for i in range(10):
        people.append(Person())
    for person in people:
        print person.name