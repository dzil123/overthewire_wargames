from util import *

shell = open_ssh()
pwd = shell.system("grep data.txt -ae '=== .*$'").recvline().split(b"=")[-1].strip()
write(password(), pwd)
