## 抽象工厂
> 在代码需要与多个不同系列的相关产品交互（不同操作系统的UI设计）
> 抽象工厂提供了接口，可用于创建每个系列产品的对象。

### 抽象工厂
> 抽象工厂接口声明了一组能返回不同抽象产品的方法。这些产品属于同一个系列
且在高层主题或概念上具有相关性。同系列的产品通常能相互搭配使用。系列产
品可有多个变体，但不同变体的产品不能搭配使用。

```
interface GUIFactory is
    method createButton():Button
    method createCheckbox():Checkbox
```
### 具体工厂
> 可生成属于同一变体的系列产品。工厂会确保其创建的产品能相互搭配
使用。具体工厂方法签名会返回一个抽象产品，但在方法内部则会对具体产品进
行实例化。
> 每个具体的工厂（WinFactory、MacFactory）包含一个相应的产品变体
```
class WinFactory implements GUIFactory is
    method createButton(): Button is
        return new WinButton()
    method createCheckbox(): Checkbox is
        return new WinBCheckbox()

class MacFactory implements GUIFactory is
    method reateButton(): Button is
        return new MacButton()
    method createCheckbox(): Checkbox is
        return new MacBCheckbox()
```
### 抽象产品
> 系列产品中的特定产品必须有一个基础接口。所有产品变体都必须实现这个接口
```java
interface Button is
    method paint()
    
interface Checkbox is
    method paint()
```
### 具体产品
> 具体产品由相应的具体工厂创建
```java
class WinButton implements Button is
    method paint() is
    //根据Win渲染Button
   
class MacButton implements Button is
    method paint() is
    //根据Mac渲染Button
    
class WinCheckbox implements Checkbox is
    method paint() is
    //根据Win渲染
   
class MacBCheckbox implements Checkbox is
    method paint() is
    //根据Mac渲染
```

## 客户端代码
```
class ApplicationConfigurator is
    method main() is
        config = readApplicationConfigfile()
        if (config.OS == "Windows") then
            factory = new WinFactory()
        elif (config.OS == "Mac") then
            factory = new MacFactory()
        else
            throw new Exception("Error: 未知操作系统")
        
        Application app - new Application(factory)
```