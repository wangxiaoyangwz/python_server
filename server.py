import socket
 
HOST, PORT = '', 8888
#WEB服务器创建一个监听socket然后开始循环接受新连接 
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#创建套接字，类型 网络通信，tcp
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#设置给定套接字选项的值。SOL_SOCKET: 基本套接口
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)#监听传入的连接
print 'Serving HTTP on port %s ...' % PORT
#开始循环接受新连接
while True:
    client_connection, client_address = listen_socket.accept()#接收连接，返回客户端新的套接字，客户端地址
    #客户端初始化一个TCP连接
    request = client_connection.recv(1024)#客户端套接字，接受tcp数据，以字符串形式返回
    print request
 
    http_response = """
HTTP/1.1 200 OK
Hello, World!
"""
	#服务器响应
    client_connection.sendall(http_response)#发送tcp数据，发送到连接的服务器套接字，成功None
    client_connection.close()#关闭客户端的套接字


#服务器套接字accept（）接受tcp连接---->数据---->客户端socket--->服务器socket--->关闭