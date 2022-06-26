# 装饰器(Decorators)
> decorator就是一个返回函数的高阶函数, 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
> 接收参数为函数，并且返回一个函数。

函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数:
```python
def a():
    print("abc")
f = a
a()
```
## 一层Decorator
```python
def log(fn):
    print("...")
    fn()
    print("...")
    return "Decorator over"
```
传入a()函数
## 嵌套两层Decorator
假设我们要增强a()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义, 故我们要定义一个能打印日志的decorator：
```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```
log是个decorator，接受参数和返回参数都是函数。借助Python的@语法，将decorator置于函数定义处：
```python
@log
def a():
    print("abc")

>>> a()
```
将`@log`放到`a()`函数定义处后执行`a()`，相当于执行语句:
```python
b = log(a)
>>> b()
```
`wrapper()`函数参数定义是`(*args, **kw)`，因此该函数可以接受任意参数调用。
## 三层Decorator
如果decorator本身需要传入参数，比如要自定义log文本：
```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():'%(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```
3层嵌套decorator用法：
```python
@log('execute')
def a():
    print("abc")
    
>>> a()
```
相当于执行：
```python
b = log('execute')(a)
>>> b()
```
## functools内置函数
经过Decorator装饰过的函数，他们的`__name__`都从'a'变成了'wrapper'
需要利用Python内置的`functools.wraps`来专门解决
- 嵌套两层的decorator
```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```
- 嵌套三层的decorator
```python
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():'%(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```
## 总结
装饰器就是：funcA() 函数装饰器 修饰funcB() 函数
```python
def funcA(fn):
    fn()
    return '...'

@funcA
def funcB():
    
```
