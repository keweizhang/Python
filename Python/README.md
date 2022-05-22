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

| 运算符 | 含义 |运算符 | 含义 |
| ------ | ---- |---|---|
| `and`  | 与   | `or`   | 或   |
| `not`  | 非   |

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

## 5. 类

## 6. 文件

## 7. 异常

### 1.8 关键字
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

## 2-常用操作

[遍历](https://github.com/keweizhang/Notes/blob/main/Python/Operation/pyTraversal.md)


