# class Human:
#     def __init__(self, name):
#         self.name = name

#     def say_hello(self):
#         print(f'hello my name is {self.name}')


# class Player(Human):
#     def __init__(self, name, xp):
#         # self.name = name
#         super().__init__(name)
#         self.xp = xp

#     # def say_hello(self):
#     #     print(f'hello! my name is {self.name}')


# class Fan(Human):
#     def __init__(self, name, fav_team):
#         # self.name = name
#         super().__init__(name)
#         self.fav_team = fav_team

#     # def say_hello(self):
#     #     print(f'hello my name is {self.name}')


# if __name__ == '__main__':
#     nico_player = Player('nico', 1000)
#     nico_player.say_hello()
#     nico_fan = Fan('nico_fan', 'warriors')
#     nico_fan.say_hello()

from typing import Any


class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(super().__str__())
        return f'Dog : {self.name}'

    def __getattribute__(self, name: str) -> Any:
        print(f'they want to get {name}')
        return "emoggi"


jia = Dog('jia')
print(jia)
