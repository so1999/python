# -*- coding: UTF-8 -*-
class Employee:
    '所有员工基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name:", self.name, "Salary:", self.salary


class Point:
    def __init(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"


class Parent:
    parentAttr = 100

    def __init__(self):
        print "调用父类构造方法"

    def parentMethod(self):
        print "调用父类方法"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性：", Parent.parentAttr


class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")


print Employee.__doc__
print Employee.__dict__
print Employee.__name__
print Employee.__module__
print Employee.__bases__

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.age = 7
emp1.age = 8
print getattr(emp1, 'age')
print hasattr(emp1, 'age')
print setattr(emp1, 'age', 9)
print delattr(emp1, 'age')
# del emp1.age
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)
del pt1
del pt2
del pt3

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()


class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount


counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
# print counter.__secretCount
print counter._JustCounter__secretCount
