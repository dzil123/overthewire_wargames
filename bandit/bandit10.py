from util import *

shell = open_ssh()
pwd = shell.system("base64 -d data.txt").recvline().split()[-1]
write(password(), pwd)
