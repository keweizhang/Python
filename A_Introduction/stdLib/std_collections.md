# [`collections`模块](https://docs.python.org/zh-cn/3/library/collections.html) 

这个模块实现了特定目标的容器，以提供Python标准内建容器 `dict` , `list` , `set` , 和 `tuple` 的替代选择

## 1. `OrderedDict`类

1. `OrderedDict`实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。兼具了 `字典` 和 `列表` 的优势
2. 该类的实例相当于有序列表，不再通过花括号赋值

### 1.1 创建
1. 直接赋值
```python
dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
print(dic)

#输出：OrderedDict([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])
```

2. 由列表生成

`.fromkeys()`方法可以把指定列表中的值作为字典的`key`来生成一个字典，可以同时赋初值

:information_source: `.fromkeys()`方法并没有改变对象的值，需要通过赋值来达到目的

:warning: 赋初值时只能给定同一个值

```python
dic = OrderedDict()
keys = ['tom','lucy','sam']
values = [175, 180, 178]
print(dic.fromkeys(keys))
print(dic.fromkeys(keys,20))
print(dic.fromkeys(keys,values))
print(dic)

# 输出
# OrderedDict([('tom', None), ('lucy', None), ('sam', None)])
# OrderedDict([('tom', 20), ('lucy', 20), ('sam', 20)])
# OrderedDict([('tom', [175, 180, 178]), ('lucy', [175, 180, 178]), ('sam', [175, 180, 178])])
# OrderedDict()
```

3. 复制已有对象

使用`.copy()`方法直接复制
```python
new_dic = dic.copy()
print(new_dic)

# 输出：OrderedDict([('tom', 20), ('lucy', 20), ('sam', 20)])
```

### 1.2 增
与创建时的赋值方法一致，新的值会排在有序字典的最后

### 1.3 删
1. 根据键删除：`.pop(key)`方法在字典中删除指定`key`对应的的`key-value`

:information_source: 该操作会有返回，返回内容是对应的`value`

```python
k = dic.pop('k2')
print(k,dic)

# 输出：v2 OrderedDict([('k1', 'v1'), ('k3', 'v3')])
```
2. 栈弹出：`.popitem()`按照后进先出原则，删除最后加入的元素

:information_source: 该操作会有返回，返回内容是键值对`key-value`

```python
print(dic.popitem(),dic)
print(dic.popitem(),dic)

# 输出：('k3', 'v3') OrderedDict([('k1', 'v1'), ('k2', 'v2')])
#      ('k2', 'v2') OrderedDict([('k1', 'v1')])
```

3. 使用`.clear()`方法可以直接删除有序字典的全部内容
```python
dic.clear()
print(dic)

#输出：OrderedDict()
```
### 1.4 改

2. 键值对移至最后
```python
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
dic.move_to_end('k1')
print(dic)

# 输出：OrderedDict([('k2', 'v2'), ('k3', 'v3'), ('k1', 'v1')])
```

### 1.5 查

1. 获取键：`.keys()`方法返回由键`key`组成的有序列表
```python
print(dic.keys())

# 输出：odict_keys(['k1', 'k2'])
```
2. 获取值：`.values()`方法返回由值`value`组成的有序列表
```python
print(dic.values())

# 输出：odict_values(['v1', 'v2', 'v3'])
```

3. 获取键值对：`.items()`方法返回由`(key,value)`键值对为组成元素的列表
```python
print(dic.items())

#输出：odict_items([('k1', 'v1'), ('k2', 'v2')])
```

4. 获取指定键对应的值：方法`.setdefault()`获取指定`key`的`value`，如果`key`不存在，则创建
```python
dic = OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
val1 = dic.setdefault('k3')
print(val1,dic)
val2 = dic.setdefault('k5')
print(val2,dic)
# 输出
# v3 OrderedDict([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])
# None OrderedDict([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3'), ('k5', None)])
```

### 1.6 整体用法示例

```python
from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
```

```
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```

