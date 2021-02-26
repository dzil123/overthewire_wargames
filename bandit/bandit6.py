from util import *

shell = open_ssh()
filename = (
    shell.system("find / -user bandit7 -group bandit6 -type f 2>/dev/null")
    .recvlineS()
    .strip()
)
shell.download(filename, password())
