重复使用import语句时，不会重新加载被指定的模块，只是把对该模块的`内存地址`给引用到本地变量环境。  
### __import__
但__import__是一个函数，并且只接收字符串作为参数,iport语句就是调用这个函数进行导入工作的  
import sys <==>sys = __import__('sys')  
[参考](http://blog.csdn.net/five3/article/details/7762870)