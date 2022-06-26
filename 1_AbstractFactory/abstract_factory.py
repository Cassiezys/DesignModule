# coding:utf-8
# @Time: 2022/6/26 9:03 上午
# @File: abstract_factory.py
# @Software: PyCharm
from abc import ABC, abstractmethod
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreateFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    def create_product_b(self):
        return ConcreteProductB1()

class ConcreateFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()
    def create_product_b(self):
        return ConcreteProductB2()

class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self):
        pass
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return "return product A1"
class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return "return product A2"

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self):
        pass
    @abstractmethod
    def another_useful_function_b(self, collaborator:AbstractProductA):
        pass

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "return product B1"
    def another_useful_function_b(self, collaborator:AbstractProductA):
        result = collaborator.useful_function_a()
        return f"return B1 collaborating with the ({result})"

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "return product B2"
    def another_useful_function_b(self, collaborator:AbstractProductA):
        result = collaborator.useful_function_a()
        return f"return B2 collaborating with the ({result})"

def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}")

if __name__ == '__main__':
    print("Client:first factory type:")
    client_code(ConcreateFactory1())

    print("Client:second factory type:")
    client_code(ConcreateFactory2())
