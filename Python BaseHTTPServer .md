Python BaseHTTPServer 模块
BaseHTTPServer:
	包含两个类HTTPServer和BaseHTTPRequestHandler
HTTPServer:
    继承SocketServer.TCPServer，用于获取请求，并将请求分配给应答程序处理

BaseHTTPRequestHandler:
    继承SocketServer.StreamRequestHandler，对http连接的请求作出应答（response）

Http Server的处理流程：
	









常用方法/属性：

BaseHTTPRequestHandler.path                    #包含的请求路径和GET请求的数据
BaseHTTPRequestHandler.command                 #请求类型GET、POST...
BaseHTTPRequestHandler.request_version         #请求的协议类型HTTP/1.0、HTTP/1.1
BaseHTTPRequestHandler.headers                 #请求的头
BaseHTTPRequestHandler.responses               #HTTP错误代码及对应错误信息的字典
BaseHTTPRequestHandler.handle()                #用于处理某一连接对象的请求，调用handle_one_request方法处理
BaseHTTPRequestHandler.handle_one_request()    #根据请求类型调用do_XXX()方法，XXX为请求类型
BaseHTTPRequestHandler.do_XXX()                #处理请求
BaseHTTPRequestHandler.send_error()            #发送并记录一个完整的错误回复到客户端,内部调用send_response()方法实现
BaseHTTPRequestHandler.send_response()         #发送一个响应头并记录已接收的请求
BaseHTTPRequestHandler.send_header()           #发送一个指定的HTTP头到输出流。 keyword 应该指定头关键字，value 指定它的值
BaseHTTPRequestHandler.end_headers()           #发送一个空白行，标识发送HTTP头部结束
BaseHTTPRequestHandler.wfile    #self.connection.makefile('rb', self.wbufsize) self.wbufsize = -1 应答的HTTP文本流对象，可写入应答信息
BaseHTTPRequestHandler.rfile    #self.connection.makefile('wb', self.rbufsize) self.rbufsize = 0  请求的HTTP文本流对象，可读取请求信息