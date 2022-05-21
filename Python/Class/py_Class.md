# 1.5 类

定义语法：`class className():`

:information_source: 根据约定，在Python中，首字母大写的名称指的是类

## 1.5.1 属性和方法
类中的函数称为方法，有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。

### 方法`__init__()`

方法`__init__()`是一个特殊的方法，其中定义了这个`类`需要的所有属性

当根据`类`创建新`实例`时，Python都会自动运行它。

约定该方法名称的开头和末尾各有两个下划线，以避免发生方法名称冲突。

:information_source: 方法`__init__()`定义时必须包含形参 `self` 且必须位于其他形参的前面

### 属性

定义为`属性`的变量都有前缀`self`，这类变量都可供类中的所有方法使用，还可以通过类的任何实例来访问这些变量

类中的每个属性都必须有初始值，可以是0或空字符串。

当在方法`__init__()`内指定初始值后，该属性就被设置了默认值，定义和实例化时就无需包含为它提供初始值的形参

:information_source: 创建实例时，会自动创建该属性并给定默认值

### 访问属性和方法

来创建实例时，`__init__()`方法将自动传入实参`self`。

每个与类相关联的方法在定义时需要给定形参`self`，在调用时都自动传递实参`self`，它是一个指向实例本身的引用，让实例能够访问类中的`属性`和`方法`

类中定义的方法和属性在实例化后可以被实例直接访问，格式为`myDog.name`, `myDog.roll_over()`

```python
# 创建类
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 给定属性默认值

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# 根据类创建实例
# instanceName = className(parameters)
my_new_car = Car('audi', 'a4', 2016)   
```

### 修改实例属性

:information_source: 可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。
 
直接修改：通过访问实例的方式直接将属性值替换为新的值

方法修改：在类中定义专门的修改属性的方法，通过调用该方法，使得修改过程更规范更好理解

## 1.5.2 继承

编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用`继承`。

1. 原有的类称为父类，而新类称为子类。
2. 子类继承其父类的所有属性和方法，同时还可以定义自己的属性和方法。
3. 创建子类时，父类必须包含在当前文件中，且位于子类前面

### 获得父类的所有属性和方法

定义：必须将父类名称包含在括号内`class subClassName(superClassName):`

子类的方法`__init__()`将完成接受父类所有属性和方法的任务，特殊函数`super()`访问父类的`__init__()`方法，并将所有属性关联到子类

### 给子类定义属性和方法
直接在子类内添加即可，注意添加的属性需要在`super()`函数之后

```python
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 添加子类独特属性
        self.battery_size = 70
    
    # 定义子类专属方法
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

# 创建实例
my_tesla = ElectricCar('tesla', 'model s', 2016)  
my_tesla.battery_size = 80
my_tesla.describe_battery()      
```

### 重写父类的方法

对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。

在子类中定义一个与要覆写的父类方法同名的方法，Python将不会考虑这个父类方法，而只关注在子类中定义的相应方法

### 将实例用作属性

使用代码模拟实物时，随着给类添加的细节越来越多，类的属性和方法清单以及文件都越来越长。在这种情况下，可能需要将类的一部分作为一个独立的类提取出来，通过将大型类拆分成多个协同工作的小类，提高程序的灵活性和可读性

例如，不断给ElectricCar类添加细节时，很多专门针对汽车电瓶的属性和方法可以提取出来，放到另一个名为`Battery`的类中。而在`ElectricCar`类中定义一个`battery`属性，并关联到`Battery`实例，`self.battery = Battery()`

## 1.5.3 导入类

导入类是一种有效的编程方式，通过将类定义移到一个模块中，并导入该模块，可以在使用其所有功能的同时，使得主程序文件变得整洁而易于阅读

**在一个模块中存储多个类**：理论上同一个模块中的类之间应存在某种相关性，但可根据需要在一个模块中存储任意数量的类，但要注意父类要在子类之前

**导入多个类**：可根据需要在程序文件中导入任意数量的类。导入多个类时，用逗号分隔了各个类。`from car import Car, ElectricCar`

**导入整个模块**：可以导入整个模块，`import car`，再使用句点表示法访问需要的类。由于创建类实例的代码都包含模块名，因此既可以避免命名冲突，也可以提高阅读性

**导入模块中的所有类**：语法为`from module_name import *`。不推荐使用这种导入方式，其原因有二。首先，只看文件开头的import语句不清楚使用了哪些类，其二可能引发命名冲突

## 1.5.4 类的编码风格

1. 命名：**类名**应采用**驼峰命名法**，即将类名中的每个单词的首字母都大写，而不使用下划线。**实例名**和**模块名**都采用**小写格式加下划线**
2. 文档：对于**每个类**，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。**每个模块**也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
3. 格式化：可使用空行来组织代码，一般使用一个空行来分隔类中的方法，使用两个空行来分隔模块中的类
4. 导入顺序：先导入标准库模块，再添加一个空行，然后导入自定义模块。这种做法让人更容易明白程序使用的各个模块都来自何方








