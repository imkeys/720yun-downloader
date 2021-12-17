import os
import sys
import datetime

root = os.getcwd()
dir = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

print('---------------------')
print(root)
print(sys.argv)
print(dir)
print(os.listdir())
print(os.path.join(os.getcwd(),os.listdir()[1]))
print('---')
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))