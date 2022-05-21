# 异常 `Exceptions`

Python使用被称为`异常` `exceptions` 的特殊对象来管理程序执行期间发生的错误。每当发生错误时，它都会创建一个`异常对象`。

通过处理异常，告诉程序发生异常时怎么办，而不是直接崩溃

## `try-except` 处理异常

最简单的异常处理包括`try-except`，完整结构包括以下内容：
```python
try:
    # 执行代码块
    pass
except:
    # 控制如何处理异常
    pass
else:
    # 当try代码块成功运行后执行
    pass
finally:
    # 无论如何都会执行的代码块
    pass
```

### 工作方式

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
    print('The answer is: '+str(c))
finally:
    print('无论如何都会执行')
```

## `raise` 抛出异常

如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的不带任何参数的 `raise` 语句就可以再次把它抛出

更多是使用 `raise` 语句抛出一个自定义的异常

语法：`raise 异常类型(异常说明)`

### 自定义抛出异常的情况

下面的例子，在符合条件时抛出的异常名为`Exceltion`，异常描述为`'x 不能大于 5。x 的值为: 10'`

```python
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
```
```python
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
Exception: x 不能大于 5。x 的值为: 10
```

### 自定义异常的内容
`raise` 唯一的一个参数指定了要被抛出的异常

:information_source: 该参数必须是一个**异常的实例**或者是**异常的类**（也就是 `Exception` 的子类）

可以通过增加说明，代替原有的错误说明，或者直接使用自定的错误对象
```python 
raise TypeError('输入的不是数字，请再次尝试输入！')
```

### 自定义错误对象
一般情况下，自定的异常类都继承自类`Exception`，一般以`Error`作为命名结尾

```python
class NewError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
```

## `assert`

用于判断一个表达式，在表达式条件为 `false` 的时候触发异常。

断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况

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








