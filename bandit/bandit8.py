from util import *

shell = open_ssh()
pwd = shell.system("cat data.txt | sort | uniq -u").recvlineS().strip().split()[-1]
write(password(), pwd)
