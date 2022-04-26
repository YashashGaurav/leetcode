# testing timeit()
import timeit

import_module = "import random"

testcode1 = ''' 
def test(): 
    ''.join(reversed("hello world"))
'''

testcode2 = ''' 
def test(): 
    "hello world"[::-1]
'''

print(timeit.timeit(stmt=testcode1, setup=import_module))