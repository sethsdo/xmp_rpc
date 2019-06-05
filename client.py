# Title: XML-RPC
# Author: Seth Olmstead
# PY Version: 3.7.2

import xmlrpc.client
import datetime
import sys
import os.path

host_address = sys.argv[1]           # read file name of from first arg
host_port = sys.argv[2]              # text to search for
param_one = sys.argv[3]              # param_one
param_two = sys.argv[4]              # param_two

if not host_address or not host_port or not param_one or not param_two:
    sys.exit('required param missing')

# create server proxy
proxy = xmlrpc.client.ServerProxy('http://'+str(host_address)+':'+str(host_port)+'/')

# proxy server procedures
add = proxy.add(int(param_one), int(param_two))
sub = proxy.sub(int(param_one), int(param_two))
mult = proxy.mult(int(param_one), int(param_two))
div = proxy.div(int(param_one), int(param_two))
servertime = proxy.servertime()
converted = datetime.datetime.strptime(servertime.value, "%Y%m%dT%H:%M:%S")

# print results
print(str(param_one) + ' * ' + str(param_two) + ' is ' + str(mult))
print(str(param_one) + ' + ' + str(param_two) + ' is ' + str(add))
print(str(param_one) + ' - ' + str(param_two) + ' is ' + str(sub))
print(str(param_one) + ' / ' + str(param_two) + ' is ' + str(div))
print(converted.strftime('%H:%M:%S'))
