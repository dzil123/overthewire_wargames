from util import *

shell = open_ssh()
filename = (
    shell.system("find inhere -type f -not -executable -size 1033c").recvlineS().strip()
)
shell.download(filename, password())
