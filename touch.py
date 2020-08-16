from sys import argv
from time import time
from os import utime, stat


for name in argv[1:]:
  open(name, 'a')
  st_info = stat(name)
  utime(name, (st_info.st_atime, time()))
