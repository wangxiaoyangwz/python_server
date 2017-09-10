# Python split()方法  
Python split()通过指定分隔符对字符串进行`切片`，如果参数num 有指定值，则仅分隔 num 个子字符串  

>str.split(str="", num=string.count(str)).  

参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。  

返回值
返回分割后的字符串列表  

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );
print str.split(' ', 1 );
以上实例输出结果如下：
['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']  

当不带参数时，默认是以空格作为参数，不管空格在哪，或者有几个 全部被镐掉了