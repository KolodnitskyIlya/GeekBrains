import sys, os

def ping():
    print('pong')

def hello(name):
    print('Hello', name)

def get_info():
    print(os.listdir())

command = sys.argv[0]

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[1]
    hello(name)

# python3 example.py ping
# pong

# python3 example.py list
# ['params.py', 'example.py', 'no_params.py']

# python3 example.py name Max
# Hello Max

