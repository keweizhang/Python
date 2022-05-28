# [`os`模块](https://docs.python.org/zh-cn/3/library/os.html?highlight=os#module-os)

## 1 检查文件是否存在

### 1.1 文件或文件夹是否存在
`os.path.exists()`方法
```python
# 判断文件是否存在
os.path.exists(test_file.txt)
# True

os.path.exists(test_dir)
#True
```
:information_source: `os.path.exists()`方法对文件和文件夹的判定结果是一样的

:warning: 对于文件和文件夹的检查可能存在误判。假设想检查文件`test_data`是否存在，但是路径下有个叫`test_data`的文件夹，可能会误判为文件存在

### 1.2 只检查文件是否存在
`os.path.isfile()`方法

```python
os.path.isfile("test-data")

# 文件test-data不存在将返回False，反之返回True。
```

### 1.3 判断文件权限

使用os.access()方法判断文件是否可进行读写操作,该方法通过判断文件是否存在和各种访问模式的权限返回`True`或者`False`

语法：`os.access(path, mode)`

|mode操作模式|含义|mode操作模式|含义|
|---|---|---|---|
|`os.F_OK`|文件是否存在|`os.R_OK`|检查文件是否可读|
|`os.W_OK`|文件是否可以写入|`os.X_OK`|文件是否可以执行|

```python
if os.access("/file/path/foo.txt", os.F_OK):
    print "Given file path is exist."

if os.access("/file/path/foo.txt", os.R_OK):
    print "File is accessible to read"

if os.access("/file/path/foo.txt", os.W_OK):
    print "File is accessible to write"

if os.access("/file/path/foo.txt", os.X_OK):
    print "File is accessible to execute"
```

