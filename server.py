# Title: XML-RPC
# Author: Seth Olmstead
# PY Version: 3.7.2
import sys
import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

server_name = sys.argv[1]       # server name
port = sys.argv[2]              # port

if not server_name or not port:
    sys.exit('required param missing')

# server procedures
def name():
    return server_name

def help():
    return ['servertime()', 'add(x,y)', 'sub(x,y)', 'mult(x,y)', 'div(x,y)']

def servertime():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y is 0:
        return 'Infinity'
    return x / y

# server invocation
server = SimpleXMLRPCServer((server_name, int(port)))
print("Listening on port " + str(port) + "...")
print(name())
print('help -', help())

# register server functions
server.register_function(servertime, "servertime")
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(mult, "mult")
server.register_function(div, "div")


server.serve_forever()
