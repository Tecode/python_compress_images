#! /usr/bin/pyton3
import os
import time


class Animal:
    animalName = ''
    age = 2
    __weight = '2kg'

    def __init__(self, name, age, weight):
        self.animalName = name
        self.age = age
        self.__weight = weight

    def speak(self):
        __languages = ["C", "C++", "Perl", "Python"]
        for language in __languages:
            print(language, '-----------------')
        print(os.getcwd(), time.time())
        print("%s 说: 我 %d 岁, %s" % (self.animalName, self.age, self.__weight))

class Hello:
    def __init__(self, name):
        self.name = name;
    def seeHello(self):
        print(self.name, '---------');
p = Animal('Loni', 5, '83kg')
p.speak()
c = Hello('sdd');
c.seeHello()
