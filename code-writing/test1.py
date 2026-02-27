# Step 1: Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


s1 = Student("Manoj", 85)
s1.show()


# Step 2: Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def details(self):
        print(f"Title: {self.title}, Author: {self.author}")


b1 = Book("Python Basics", "Alex")
b1.details()


# Step 3: Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


r1 = Rectangle(5, 4)
print(f"Area: {r1.area()}")


# Step 4: Counter class
class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

    def show(self):
        print(f"Count: {self.count}")


c1 = Counter()
c1.increase()
c1.increase()
c1.increase()
c1.show()


# Step 5: Car class
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0

    def show_speed(self):
        print(f"{self.brand} speed: {self.speed}")


car1 = Car("Toyota")
car1.show_speed()
car1.accelerate()
car1.show_speed()
car1.accelerate()
car1.show_speed()
car1.brake()
car1.show_speed()
car1.brake()
car1.show_speed()
car1.brake()
car1.show_speed()



#Class5 - LoginTracker class
class LoginTracker:
    def __init__(self):
        self._active = set()

    def login(self, user_id: str) -> None:
        self._active.add(user_id)

    def logout(self, user_id: str) -> None:
        self._active.discard(user_id)  # discard = safe even if not present

    def is_logged_in(self, user_id: str) -> bool:
        return user_id in self._active

    def active_user_count(self) -> int:
        return len(self._active)


# Minimal tests
if __name__ == "__main__":
    t = LoginTracker()

    assert t.active_user_count() == 0
    assert t.is_logged_in("u1") is False

    t.login("u1")
    assert t.is_logged_in("u1") is True
    assert t.active_user_count() == 1

    t.login("u1")  # idempotent
    assert t.active_user_count() == 1

    t.logout("u2")  # safe even if never logged in
    assert t.active_user_count() == 1

    t.logout("u1")
    assert t.is_logged_in("u1") is False
    assert t.active_user_count() == 0

    print("All tests passed.")
