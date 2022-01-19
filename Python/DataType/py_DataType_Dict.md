## 字典 dict

### 定义

无序键值对`key:value`的集合，同一个字典内的键必须是互不相同的

### 创建

#### 手动创建

`{}`内用`,`分隔`key:value` 键值对

其中`key`必须为字符串，也可以用指向字符串的变量，则新创建的字典`key`为变量内容

```python
b = {'a':1,'b':2,'c':3}
```

空字典为 `a = {}`

#### 元组转化

函数`dic()`可以将包含键值对的元组转化为字典

```python
cc = [('1',1),('2','jiqw'),('3',1372)]        
dict(cc)

{'1': 1, '2': 'jiqw', '3': 1372}
```

### 增

直接索引新key，并赋值新的value，`dictName[newKey] = newValue`

### 删

`del dictName[key]` 语句删除字典中的特定键

`.pop(key)` 方法删除字典中的特定键，同时返回对应删除`key`的`value`

#### 改

索引key 再赋值即可

#### 查

索引`key`进行查找，对于不存在的key会报错

`.get(key,default)`方法可以获得key对应的value，如果不存在，则返回default值，缺省时什么都不返回

创建默认值

`.setdefault(key,defaultValue)` 方法用来创建默认值，如果key 存在，则返回已有值

