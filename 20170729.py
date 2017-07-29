# def do_plus(a, b):
#     if type(a) != type(1) or type(b) != type(1):
#         raise TypeError
#
#     return a + b
#
# do_plus(1, 5)


### 类与对象 ###
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print(self.name + " is running")
#
# dog = Animal("dog")
# dog.run()
#
#
# def self_run(self):
#     self.run()
#
# self_run(dog)
#
# class Bird(Animal):
#     def fly(self):
#         print(self.name + " is flying")
#
# bird = Bird("bird")
# bird.fly()
# self_run(bird)


def hanoi(n, _from, _by, _to):
    """递归实现汉诺塔"""
    if type(n) != type(1):
        raise TypeError
    if n < 1:
        raise ValueError

    if n == 1:
        print("from "+ _from + " to " + _to)
        return
    else:
        hanoi(n-1, _from, _to, _by)
        print("from "+ _from + " to " + _to)
        hanoi(n-1, _by, _from, _to)

hanoi(3, 'a', 'b', 'c')