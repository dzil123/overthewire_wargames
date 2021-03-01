from util import *

shell = open_ssh()

# the binary prints the password as binary
pwd = shell.system("./.trash/bin").readlineS()
pwd = unbits(int(c) for c in "".join(pwd.split()))

write(password(), pwd)
