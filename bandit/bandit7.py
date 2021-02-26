from util import *

shell = open_ssh()
pwd = shell.system("grep data.txt -e millionth").recvlineS().strip().split()[-1]
write(password(), pwd)
