from tkinter.font import names


class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def spark(self):
        raise NotImplementedError("子类必须实现这个方法")

class dog(animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} 是一只 {self.breed}，它说: 汪汪!")

Dog = dog("小白", 3, "拉布拉多")
Dog.speak()
