from boa.abi import *


@abi_entry_point(String, Array, Any)
def main(operation, args):
    if operation == 'add':
        a = args[0]
        b = args[1]
        return add(a, b)
    else:
        return False


@abi_entry_point(Integer, Integer, Integer)
def add(a, b):
    return a + b
