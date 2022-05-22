# Python语法

## 1. [变量与运算符](https://github.com/keweizhang/Notes/blob/main/Python/py_Variables.md)

### 1.1 变量

python内定义变量无需指定变量的数据类型

可以一行定义多个变量`a, b = 3, 4`，当用于交换变量的值时，非常方便

:information_source: 其原理是`tuple`的封装与解封

### 1.2 运算符

#### 数值运算符

|作用|运算符|作用|运算符|
|---|---|---|---|
|四则运算符|`*`  `/`  `+`  `-`|整除取商|`//`|
|简写运算符|`*=`  `/=`  `-=`  `+=`|取余运算|`%`|

:information_source: 同时得到商和余数的函数`divmod(a,b)`，返回的是一个结果为`(div, mod)`的`tuple` 

#### 关系运算符

| 运算符 | 含义  |运算符 | 含义  |
| ------ | --------------------------- |---|---|
| `<`  | Is less than                | `>`  | Is greater than             |
| `<=` | Is less than or equal to    | `>=` | Is greater than or equal to |
| `==` | Is equal to                 | `!=` | Is not equal to             |

#### 逻辑运算符

python使用关键字进行逻辑运算

| 关键字 | 含义 | 关键字 | 含义 | 关键字 | 含义 |
| ------ | ---- |---|---|---|---|
| `and`  | 与   | `or`   | 或   | `not`  | 非   |

`and` 和 `or` 也称作短路运算符：它们的参数从左向右解析，一旦结果可以确定就停止

#### 强制类型转换

| 函数  | 含义 |函数  | 含义 |
| ------ | --- |---- | --- |
| `float(string)` | 字符串 -> 浮点值 | `str(integer)`  | 整数值 -> 字符串 |
| `int(string)`   | 字符串 -> 整数值 |`str(float)`    | 浮点值 -> 字符串 |

   
## 2. 数据类型

|数据类型|简要说明|数据类型|简要说明|
|----|----|---|---|
|[字符串](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_Str.md)|熟悉常用方法|[格式化字符串](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_StrFormat.md)和[格式化符](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_StrFormator.md)|用于格式化输出|
|[列表](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_List.md)|内部元素可以不同类型|[集合](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_Set.md)|无序不重复|
|[元组](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_Tuple.md)|无序的列表|[字典](https://github.com/keweizhang/Notes/blob/main/Python/DataType/py_DataType_Dict.md)|无序键值对的集合|


## 3. [结构](https://github.com/keweizhang/Notes/blob/main/Python/py_Structure.md)

### 3.1 `if-else`分支结构

|关键字|用法|关键字|用法|
|---|---|---|---|
|`if condition:`|根据`condition`逻辑值判定是否要执行代码块||
|`elif`|用于多个条件的判断|`else:`|用于全部剩余情况的判断|
|`in`|配合判定元素是否存在|`is`|配合判定是否相同|

:information_source: 判断的优雅方式为`if x:`，而不是 `if x == True:` 

:information_source: 判定条件可以为逻辑值或者表达式，当结果为`True`、`非0`、`非空`时判定为真

:information_source: `is`判定需要满足`值`和`地址`都相同，`==`只需要值相同。整数的地址一样，浮点数不同

```python
if condition1:
    expression1
elif condition2:
    expression2
else:
    expression3
```

### 3.2 循环结构

|关键字|用法|关键字|用法|
|---|---|---|---|
|`while`|循环直到条件改变||
|`for`|循环给定的可迭代对象|`in`|提取可迭代对象的元素
|`continue`|跳过剩余代码进入下一次循环|`break`|跳出当前整体循环|

:information_source: `continue` 和 `break` 通常配合`if`语句使用

#### `while`循环

适用于循环次数不确定，但条件确定的情况

```python
# 对 condition 进行判定，需要配合用来改变条件的 increacement语句
while condition:
    expression
    increacement
# 用 break 判定，以结束循环
while True:
    expression
    if condition:
        break
```

也可以直接 `while True:`，在循环体内提供判定条件，再`break` 结束循环

#### `for`循环结构

适用于循环次数或者内容确定的情况

```python
for elem in elements: 
    exprestion
```

`elem` 为临时变量，可以在`for`循环内调用，`elements` 可以为**任何可迭代的数据对象**

:information_source: 如果需要循环规律数列，可以配合`range()`函数使用

## 4. [函数](https://github.com/keweizhang/Notes/blob/main/Python/py_Function.md)

|关键字|作用|关键字|作用|
|---|---|---|---|
|`def`|定义函数的句柄|`return`|返回值到函数体外|

### 4.1 定义

**语法：**`def func_name(args):` 定义了函数名为 `func_name` 且参数为`args`的函数

:information_source: 约定函数名一般只包含小写字母和下划线

**文档字符串：**用位于函数定义句柄下，三引号括起的字符串描述函数作用，Python使用它们来生成函数说明文档

**实参：**指函数体外定义使用的参数，调用函数时，实参的值需要通过传参的方式在函数内使用

**形参：**指函数体内定义及使用的参数，作用域仅限函数内部，调用函数时，用于接收实参的值

### 4.2 返回值

`return`：将函数内的值作为函数的返回，用于函数体外，放在函数体最后一行

返回多个值：实质返回的是 `tuple`，赋予多个变量的过程是**元组拆封**

函数可返回任何类型的值，包括列表和字典等较复杂的数据结构

示例：
```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
```

### 4.3 传递参数

python中有多种类型参数：

1. 定义顺序：必选参数、默认参数（可选参数）、可变参数、命名关键字参数和关键字参数
2. 位置实参也可以像关键字实参一样调用
3. 传递`列表`可在函数内方便处理多个情况。直接传递的列表在函数内会修改列表本身，如想保留原列表，可使用切片。`funcName(listA(:))` 会处理列表副本，但同时会增加时间损耗

|参数类型|用法|特点|
|---|---|---|
|位置参数|调用时，根据定义位置将每个实参关联到每个形参|调用时参数顺序很重要|
|关键字实参|定义方法与位置实参相同，调用格式为 `形参=实参`|无需考虑实参顺序|
|默认参数|定义时赋值 `defaultPar = value`，调用时可省略该参数|避免调用时每次都输入常用参数|
|可选参数|定义时给空值，函数体内`if`语句分情况讨论|函数调用更灵活|
|任意数量的实参|定义格式：`*args`，所有未定义实参将存入`元组`内|无需在定义时考虑所有参数|
|任意数量的关键字实参|定义格式：`**args`，所有未定义关键字实参将存入`字典`类形参内；调用时可以直接传入`字典`类实参|1. 无需在定义时考虑所有参数；2.无法确定到底传入了哪些关键字，需要`if..in..`语句判断|
|命名关键字参数|定义时用`*,`占位，后续参数就是命名关键字参数；调用时**必须**用`形参=实参`的格式||

示例：
```python
# 位置实参，关键字实参，默认参数，可选参数
# 定义
def get_formatted_name(first_name, last_name, middle_name='', title = 'Doctor'):
    """返回整洁的姓名"""
    # 默认参数和可选参数的区别在可选参数是空值
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    print('Dear '+ title + ' ' + full_name.title()) 

# 调用
# 以下三种等效
get_formatted_name('Tony', 'Stark')
get_formatted_name('Tony', 'Stark', title = 'Doctor')
get_formatted_name(first_name = 'Tony', last_name = 'Stark', title = 'Doctor')
# 默认参数和可选参数无视调用顺序
get_formatted_name('Tony', 'Stark', title = 'Iron Man', middle_name='J')

# 输出
# Dear Doctor Tony Stark
# Dear Doctor Tony Stark
# Dear Doctor Tony Stark
# Dear Iron Man Tony J Stark
```

```python
# 任意数量实参
# 定义
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings) # toppings是一个tuple

# 调用
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

```python
# 任意数量关键字实参
# 定义
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # 将传入的任意数量关键字实参解析，实质为解析字典
    for key, value in user_info.items():
        profile[key] = value
    return profile

# 调用
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# 等效调用：先定义字典，再调用
extra = {'location':'princeton', 'field':'physics'}
user_profile = build_profile('albert', 'einstein', **extra)
```

```python
# 命名关键字参数
# 定义
def person(name, age, *, city, job):
    print(name, age, city, job)

# 调用
person('Jack', 24, city='Beijing', job='Engineer')
```

## 5. [类](https://github.com/keweizhang/Notes/blob/main/Python/Class/py_Class.md)

定义语法：`class className():`

:information_source: 根据约定，在Python中，类的名称采用驼峰命名法，其首字母一般大写

### 5.1 属性和方法

类中的函数称为方法，有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用的方式

#### 方法`__init__()`

方法`__init__()`是一个特殊的方法，其中定义了这个`类`需要的所有属性，当根据`类`创建新`实例`时，Python都会自动运行它。

约定该方法名称的开头和末尾各有两个下划线，以避免发生方法名称冲突。

:information_source: 方法`__init__()`定义时必须包含形参 `self` 且必须位于其他形参的前面

```python
# 创建类
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 给定属性默认值
```

#### 属性

定义为`属性`的变量都有前缀`self`，这类变量都可供类中的所有方法使用，还可以通过类的任何实例来访问这些变量

实例化时类中的每个属性都必须有初始值，可以是0或空字符串，一般为给定形参。当在方法`__init__()`内指定初始值后，该属性就被设置了默认值，`__init__()`句柄中和实例化时就无需包含该形参

:information_source: 创建实例时，会自动创建该属性并给定默认值

#### 访问属性和方法

创建实例时，`__init__()`方法将自动传入实参`self`。

每个与类相关联的方法在定义时需要给定形参`self`，在调用时都自动传递实参`self`，它是一个指向实例本身的引用，让实例能够访问类中的`属性`和`方法`

类中定义的方法和属性在实例化后可以被实例直接访问，格式为`myDog.name`, `myDog.roll_over()`


#### 修改实例属性

:information_source: 可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。
 
直接修改：通过访问实例的方式直接将属性值替换为新的值

方法修改：在类中定义专门的修改属性的方法，通过调用该方法，使得修改过程更规范更好理解

### 5.2 继承

编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用`继承`。原有的类称为**父类**，而新类称为**子类**。子类继承其父类的所有属性和方法，同时还可以定义自己的属性和方法。

语法：必须将父类名称包含在括号内`class SubClassName(SuperClassName):`

创建子类时，父类必须包含在当前文件中，且位于子类前面

**获得父类的所有属性和方法：**子类的方法`__init__()`将完成接受父类所有属性和方法的任务，特殊函数`super()`访问父类的`__init__()`方法，并将所有属性关联到子类

**定义子类独有的属性和方法：**直接在子类内添加即可，注意添加的属性需要在`super()`函数之后

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
```

**重写父类的方法：**在子类中定义一个与要覆写的父类方法同名的方法，在实例化时就只会考虑子类中的方法

**将实例用作属性：**在给定属性初始值时，设定为某个类的实例化

使用代码模拟实物时，随着给类添加的细节越来越多，类的属性和方法清单以及文件都越来越长。在这种情况下，可能需要将类的一部分作为一个独立的类提取出来，通过将大型类拆分成多个协同工作的小类，提高程序的灵活性和可读性

例如，不断给ElectricCar类添加细节时，很多专门针对汽车电瓶的属性和方法可以提取出来，放到另一个名为`Battery`的类中。而在`ElectricCar`类中定义一个`battery`属性，并关联到`Battery`实例，`self.battery = Battery()`

### 5.3 导入类

导入类是一种有效的编程方式，通过将类定义移到一个模块中，并导入该模块，可以在使用其所有功能的同时，使得主程序文件变得整洁而易于阅读

**在一个模块中存储多个类**：理论上同一个模块中的类之间应存在某种相关性，但可根据需要在一个模块中存储任意数量的类，但要注意父类要在子类之前

**导入多个类**：可根据需要在程序文件中导入任意数量的类。导入多个类时，用逗号分隔各个类。`from car import Car, ElectricCar`

**导入整个模块**：可以导入整个模块，`import car`，再使用句点表示法访问需要的类。由于创建类实例的代码都包含模块名，因此既可以避免命名冲突，也可以提高阅读性

**导入模块中的所有类**：语法为`from module_name import *`。不推荐使用这种导入方式，一方面根据import语句不清楚使用了哪些类，另一方面可能引发命名冲突

### 5.4 类的编码风格

1. 命名：**类名**应采用**驼峰命名法**，即将类名中的每个单词的首字母都大写，而不使用下划线。**实例名**和**模块名**都采用**小写格式加下划线**
2. 文档：对于**每个类**，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。**每个模块**也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
3. 格式化：可使用空行来组织代码，一般使用一个空行来分隔类中的方法，使用两个空行来分隔模块中的类
4. 导入顺序：先导入标准库模块，再添加一个空行，然后导入自定义模块。这种做法让人更容易明白程序使用的各个模块都来自何方


## 6. [文件](https://github.com/keweizhang/Notes/blob/main/Python/Files/py_File.md)

函数 `open()` 接受文件名参数来打开指定文件，函数 `close()` 用来关闭文件

关键字 `with` 在访问文件后会自动将其关闭，可以避免因为程序错误导致`close()`未执行而带来的文件未关闭错误

### 6.1 读取

#### 全部读取

使用方法`.read()`操作打开的文件对象，并将其结果作为一整个长长的字符串存储在变量中

:information_source: `.read()`到达文件末尾时会返回一个空字符串，`print()`等操作时会多出一个空行，可以使用`.rstrip()`方法剔除


#### 逐行读取

使用`for`循环，遍历文件对象的每一行

:information_source: 每行末尾都有一个换行符，可以使用`.rstrip()`方法剔除

#### 读取为各行组成的列表

使用`.readlines()`方法，直接将文件对象转为该文件的每一行内容组成的列表

使用关键字`with`时，`open()`返回的文件对象只在`with`代码块内可用，但保存为列表后，可以供后续数据处理使用

:warning: 不论哪种读取方式，得到的都是字符串，如果是需要处理的数值，必须进行类型转换

```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    # 全部读取
    contents = file_object.read()
    # 逐行读取
    for line in file_object:
        print(line.rstrip())
    # 逐行读取为列表
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

### 6.2 写入

#### 写入方法
 `.write()` 将字符串写入文本，需要在打开文本时指定为写入或者追加模式

`open()`函数的参数：
|参数|含义|参数|含义|
|---|---|---|---|
|`'r'`|只读模式（默认）|`'w'`|写入模式，如果文件不存在会自动创建|
|`'r+'`|读取和写入|`'a'`|追加模式，如果文件不存在会自动创建|

:warning: 如果以写入（`'w'`）模式打开了已经存在的文件，内容会覆写，最好有判断文件是否存在的语句。常用为`os.path.isfile(filename)`

:information_source: 当写入多行时，需要注意在每行末尾设置好换行符

```python
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```

## 7. [异常](https://github.com/keweizhang/Notes/blob/main/Python/Exceptions/py_Exceptions.md)

Python使用被称为`异常` `exceptions` 的特殊对象来管理程序执行期间发生的错误。每当发生错误时，它都会创建一个`异常对象`。

通过处理异常，告诉程序发生异常时怎么办，而不是直接崩溃

|关键字|作用|关键字|作用
|----|----|----|----|
| `try` | 尝试运行可能抛出异常的代码块 | `raise`| 抛出异常（可自定义）
| `except` | 处理异常，规范发生异常时的程序反馈 | `assert` | 直接根据主动设置的判断条件返回错误提示，而不是等异常发生时|
| `else` | 当`try`代码块没有异常抛出时执行| `pass` |可以用在错误发生时直接忽略，不给任何反馈而跳过|
| `finally` | 是否发生异常都要执行 ||

### 7.1 `try-except` 处理异常

最简单的异常处理包括`try-except`，完整结构包括以下内容：

||工作流程|
|---|--|
|`try:`|程序会首先执行 `try` 下的代码块|
|`except:`|如果**没有异常**，忽略 `except` 子句|
||如果**发生异常**，那么 `try` 子句余下的部分将被忽略|
||如果**异常的类型没有匹配**到，那么对应的 `except` 子句将被执行|
||如果异常没有与任何的 `except` 匹配，那么这个异常将会传递回上层 `try`，也就是依然会抛出错误|
||可以在最后单独用一个不指定错误名的 `except:` 子句，用来忽略异常的名称
|`else:`|必须放在所有的 `except` 子句之后，将在 `try` 子句没有发生任何异常的时候执行|
|`finally:`|无论是否发生异常都将执行最后`finally`子句下的内容|


:information_source: 可以包含多个`except`子句，分别来处理不同的特定异常，但最多只有一个分支会被执行

:information_source: 一个`except`子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组

:information_source: 使用 `else` 子句比把所有的语句都放在 `try` 子句里面要好。比如只把容易出错的用户输入放入`try`子句

```python
try:
    c = a/b
except TypeError:
    print("您输入的不是数字，请再次尝试输入！")
except (ZeroDivisionError, NameError, ValueError): 
    print('发生了三个中的某个错误')
except:
    print('发生了一个未被特别处理的错误')
else:
    print('The answer is: ' + str(c))
finally:
    print('这里无论如何都会执行')
```

### 7.2 `raise` 抛出异常

如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的不带任何参数的 `raise` 语句就可以再次把它抛出

更多是使用 `raise` 语句抛出一个自定义的异常

语法：`raise 异常类型(异常说明)`

**自定义抛出异常的情况**：可以配合`if`语句设置异常抛出的时机


#### 自定义异常

`raise` 唯一的一个参数指定了要被抛出的异常

:information_source: 该参数必须是一个**异常的实例**或者是**异常的类**（也就是 `Exception` 的子类）

**自定义异常内容**：可以通过增加说明，代替原有的错误说明，或者直接使用自定的错误对象

```python 
raise TypeError('输入的不是数字，请再次尝试输入！')
```

**自定义错误对象**：

一般情况下，自定的异常类都继承自类`Exception`，一般以`Error`作为命名结尾

```python
class NewError(Exception):
    def __init__(self, message):
        self.message = message
```

### 7.3 `assert`断言

用于判断一个表达式，在表达式条件为 `false` 的时候触发异常。

断言可以在条件不满足的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况

语法：`assert [判断条件], [异常说明]`

```python
assert expression [, arguments]
```

等价于：

```python
if not expression:
    raise AssertionError
```

用法举例
```python
>>> assert 1==2, '1 不等于 2'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: 1 不等于 2
```











## 8. 关键字
|关键字|作用|关键字|作用|关键字|作用|
|----|----|----|----|----|----|
| `True` | 布尔类型 `真` | `False` | 布尔类型 `假` | `None` |特殊数据类型 `空`|
| `and` | 逻辑 `与` | `or` | 逻辑 `或` | `not` | 逻辑 `非` |

|关键字|作用|关键字|作用
|----|----|----|----|
| `in` | 判断元素存在和遍历 | `with` | 自动处理异常，常用在文件读写 |
| `as` | 名称代替或赋值 |||


#### 常用在异常处理中的关键字
|关键字|作用|关键字|作用
|----|----|----|----|
| `try` | 判断元素存在和遍历 | `raise`| 抛出异常（可自定义）
| `except` | 处理异常，规范发生异常时的程序反馈 | `assert` | 直接根据主动设置的判断条件返回错误提示，而不是等异常发生时|
| `else` | 当`try`代码块没有异常抛出时执行| `pass` |可以用在错误发生时直接忽略，不给任何反馈而跳过|
| `finally` | 是否发生异常都要执行 ||



## 9. 代码测试

## 2-常用操作

[遍历](https://github.com/keweizhang/Notes/blob/main/Python/Operation/pyTraversal.md)


