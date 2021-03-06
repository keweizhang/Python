# 测试代码

对于简单的程序，可以自己手动输入或者直接运行以验证程序没有问题。但是大型程序或者需要合作的程序，必须经过测试，这就需要我们根据不同的情况来输入不同的测试用例，特别是对于边界条件等特殊情况需要进行测试。

使用Python模块`unittest`中的工具可以辅助测试代码工作，即将需要测试的用例写为测试代码，使得这些测试可以重复使用，这对于还处于开发中需要不断修改的程序会省去很多手动输入不同测试用例的时间；对于大型程序则必须用测试代码来容纳一系列测试

原理就是基于模块`unittest`创建对象，将测试输入和预期的正确输出都存在对象内，用`断言`语句进行判定



## 测试函数

Python标准库中的模块unittest提供了代码测试工具。单元测试用于核实函数的某个方面没
有问题；测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。全覆盖式测
试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。对于大型项目，要实现全覆盖可
能很难。通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。



## 测试对象



