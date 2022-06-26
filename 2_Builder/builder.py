# coding:utf-8
# @Time: 2022/6/26 4:18 下午
# @File: builder.py
# @Software: PyCharm
from abc import ABC, abstractmethod
class Builder(ABC):
    """
        Builder接口定义用来创建产品不同部分的方法
    """
    @abstractmethod
    def product(self):
        pass
    @abstractmethod
    def produce_part_a(self):
        pass
    @abstractmethod
    def produce_part_b(self):
        pass
    @abstractmethod
    def produce_part_c(self):
        pass

class ConcreteBuilder1(Builder):
    """
        继承Builder接口的类 提供方法的不同实施
    """
    def __init__(self):
        self.reset()
    def reset(self):
        self._product = Product1()

    def product(self):
        product = self._product
        self.reset()
        return product
    def produce_part_a(self):
        self._product.add("PartA1")
    def produce_part_b(self):
        self._product.add("PartB1")
    def produce_part_c(self):
        self._product.add("PartC1")

class Product1():
    def __init__(self):
        self.parts = []
    def add(self, part):
        self.parts.append(part)
    def list_parts(self):
        print(f"Product parts:{','.join(self.parts)}", end="")

class Director:
    def __init__(self):
        self._builder = None
