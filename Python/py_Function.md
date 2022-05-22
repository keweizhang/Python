## 4 函数

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



