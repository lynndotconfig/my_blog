import datetime
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer


def is_even(n):
    return n % 2 == 0


def today():
    today = datetime.datetime.today()
    return xmlrpclib.DateTime(today)


def add(x, y):
    return x + y + 0j


server = SimpleXMLRPCServer(("localhost", 8111))
print "Listening port 8111"
server.register_function(is_even, "is_even")
server.register_function(today, "today")
server.register_function(add, "add")
server.serve_forever()
server.serve_forever()
