# Socket [参考了scoket](http://blog.csdn.net/rebelqsp/article/details/22109925)
socket起源于Unix,“一切皆文件”  
文件用【打开】【读写】【关闭】模式来操作  
socket就是该模式的一个实现   
socket即是一种特殊的文件，一些socket函数就是对其进行的操作（读/写IO、打开、关闭）  
浏览器地址栏中输入URL---->打开一个套接字--->连接到url,并读取响应的页面然后然后显示出来   
任何网络通讯都是通过 Socket 来完成的 
socket和file的区别： 
    1. file模块是针对某个指定文件
    2.  socket模块是针对 服务器端 和 客户端Socket 进行  

创建一个socket服务端:
```python
    import socket

    #创建流套接字描述符
    sk = socket.socket()
    #命名套接字（参数1.协议，2.本地地址，3.本地端口）
    sk.bind(("127.0.0.1",8080))
    #监听客户端socket请求
    sk.listen(5)

    conn,address = sk.accept()
    sk.sendall(bytes("hello world",encoding='utf-8'))
```

```python
    import socket

    obj = socket.socket()
    obj.connect(("127.0.0.1",8080))

    ret = str(obj.recv(1024),encoding = "utf-8")
    print(ret)
```

`bind(address)`:套接字绑定到地址,address地址的格式取决于地址族,AF_INET下，以元组（host,port）的形式表示地址  
`listen(backlog)`:开始监听传入连接,backlog指定在拒绝连接之前，可以挂起的最大连接数量backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5  
`accept()`:接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。接收TCP 客户的连接（阻塞式）等待连接的到来  
`connect(address)`:连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。  
``  


Python 提供了两个基本的 socket 模块 
1. Socket，它提供了标准的 BSD Sockets API
2. SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

## Socket模块功能  
`**套接字格式**`：  
socket(family,type[,protocal])给定的地址族,套接字类型,协议编号（默认为0）  
`功能`：创建套接字。
`socket类型`:
socket.AF_UNIX--->只能够用于单一的Unix系统进程间通信  
socket.AF_INET--->服务器之间网络通信  
socket.AF_INET6--->IPv6  
socket.SOCK_STREAM--->流式socket , for TCP  
socket.SOCK_DGRAM--->数据报式socket , for UDP  
socket.SOCK_RAW--->原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。  
socket.SOCK_SEQPACKET--->可靠的连续数据包服务   
SOL_SOCKET: 基本套接口  

`创建TCP Socket：`:s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
`创建UDP Socket：`:s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  

### Socket 函数
`注意点:`
1. TCP发送数据时，已建立好TCP连接，所以不需要指定地址。UDP是面向无连接的，每次发送要指定是发给谁。  
2. 服务端与客户端不能直接发送列表，元组，字典。需要字符串化repr(data)  
>**服务端socket函数**  

`s.bind(address)`:将套接字绑定到地址, 在AF_INET下,`参数`:以元组（host,port）的形式表示地址.  

`s.listen(backlog)`:监听TCP传入连接。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了  

`s.accept()`:接受TCP连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。   

`s.getsockname()`:返回套接字自己的地址。通常是一个元组(ipaddr,port)

>**客户端socket函数** 

`s.connect(address)`:连接到address处的套接字。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。 

`s.connect_ex(adddress)` :功能与connect(address)相同，但是成功返回0，失败返回errno的值。  

>**公共socket函数** 

`s.recv(bufsize[,flag])`:接受TCP套接字的数据。数据以字符串形式返回，`参数`：bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。  

`s.sendall(string[,flag])`:完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。  

`s.setsockopt(level,optname,value)`:设置给定套接字选项的值。  


### socket编程思路  \
TCP服务端:  
1. 创建套接字，绑定套接字到本地IP与端口
`# socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.bind()`
2. 开始监听连接                   #s.listen()  
3. 进入循环，不断接受客户端的连接请求              #s.accept()  
4. 然后接收传来的数据，并发送给对方数据         #s.recv() , s.sendall()
5. 传输完毕后，关闭套接字                     #s.close()  

### Socket编程之服务端代码：  
```python
    import socket #socket模块
    importcommands #执行系统命令模块
    HOST = '10.0.0.245'
    PORT = 50007
    s=scoket.socket(scoket.AF_INET,socket.SOCK_STREAM)#定义socket类型，网络通信，tcp
    s.bind((HOST,PORT))#套接字绑定的IP与端口
    s.lisent(1)#开始监听tcp
    while 1:
        conn,addr = s.accept()#接受tcp连接，并返回新的套接字与IP地址
        print 'Connected by',addr
        while 1:
            data = conn.recv(1024)#把接受的数据实例化
            cmd_status,cmd_result = commands.getstatusoutput(data) #commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息  
            if len(cmd_result.strip())==0:#如果输出结果长度为0，则告诉客户端完成，此用法针对于创建文件或目录，创建成功不会有输出信息
                conn.sendall('Done.')
            else:
                conn.sendall(cmd_result)
    conn.close()
```
### Socket编程之客户端代码：
```python
    import socket
    HOST ='10.0.0.245'
    PORT = 500007
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #定义socket类型，网络通信，TCP
    s.connect((HOST,PORT))#要连接的IP与端口
    while 1:
        cmd = raw_input("please input cmd:")#与人交互，输入命令
        s.sendall(cmd)#将命令发送到对端
        data = s.recv(1024)#把接受到的数据定义为变量
        print data #输出变量
    s.close()#关闭连接

```

