# 生成器模式
> 构建复杂对象时，需要对诸多成员变量和嵌套对象进行初始化工作。

## 构建 汽车 复杂对象
### 产品接口
> 汽车和使用手册没有同样的接口，但却相互关联
```
class Car is
class Manual is
```
### 生成器接口
> 生成器接口声明了创建产品对象不同部件的方法
```
interface Builder is
    method reset() # 清空，从而实例都由空产品对象
    method setSeats(...)
    method setEngin(...)
    method setTripComputer(...)
    method setGPS(...)
```

### 具体生成器
> 具体生成器提供生成器接口的具体实现
> 1. 新生成器实例不许包含一个在后续组装过程中使用的空产品对象
> 2. 所有的生成步骤都会与同一个产品实例进行交互
> 3. 具体生成器需要提醒提供获取方法，【并重置生成器】
```
class CarBuilder implements Builder is
    private field car:Car
    
    # 新生成器实例不许包含一个在后续组装过程中使用的空产品对象
    constructor CarBuilder() is
        this.reset()
    method reset() is
        this.car = new Car()
    
    # 所有的生成步骤都会与同一个产品实例进行交互
    mehod setSeats(...) is
        // 设置汽车座位数量
    method setEngin(...) is
        // 安装指定引擎
    method setTripComputer(...) is
        //安装行车电脑
    method setGPS(...) is
        //安装GPS
        
    # 具体生成器需要提醒提供获取方法:
    // 生成器实例通常会在 `getProduct（获取产品）`方法主体末尾调用重置方法。
    // 但是该行为并不是必需的，你也可让生成器等待客户端明确
    // 调用重置方法后再去处理之前的结果。
    method getProduct():Car is
        product = this.car
        this.reset()
        return product
        
class CarManulBuilder implements Builder is
    private field manul: Manual
    constructor CarManulBuilder() is
        this.reset()
    method reset() is 
        this.manual = new Manual()
    
    mehod setSeats(...) is
        // 添加关于汽车座椅功能的文档
    method setEngin(...) is
        // 添加关于指定引擎的介绍
    method setTripComputer(...) is
        // 添加关于行车电脑的介绍
    method setGPS(...) is
        // 添加关于GPS的介绍
    
    method getProduct():Manual is
        //返回使用手册并重置生成器
```
### 主管
> 主管只负责按照特定顺序执行生成步骤。
> 客户端可以直接控制生成器，严格意义上不是必须。但实现使用同一生成器对象来封装多种构造产品。
```
class Director is 
    private field builder:Builder
    
    method setBUilder(build:Builder）
        this.builder = builder
    
    method ocnstrucSportsCar(build:Builder) is
        builder.reset()
        builder.setSeats(2)
        builder.setEngin(new SportEngine())
        builder.setTripComputer(ture)
        builder.setGPS(ture)
        
    method constructSUV(builder:Builder) is
        ...
    
```

### 客户端代码
> 创建生成器对象 并传递给主管director，然后执行构造过程
> 最终结果要从生成器对象中获取
```
class Application is
    method makeCar() is
        director - new Director()
        CarBuilder builder = new CarBUilder()
        director.constructSportsCar(builder)
        Car car = builder.getProduct()
        
        CarManulBUilder builder = new CarManualBUIlder()
        director.constructSpotsCar(builder)
        
        # 最终产品要从生成器对象中获取，主管不知道具体生成器和产品存在，也不会对其产生依赖
        Manusl manual = builder.getProduct()
```

## 适用场景
1. 避免"重叠构造函数（telescoping constructor）"出现
2. 使用代码创建不同形式的产品，这些产品制造过程相似只有细节上的差异，主管类负责管理制造步骤的顺序
3. 使用生成器构造组合树或其他复杂对象

