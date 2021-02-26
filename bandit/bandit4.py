from util import *

shell = open_ssh()
filename = (
    shell.system("find inhere -exec file {} \\;")
    .recvline_containsS("ASCII text")
    .split(":")[0]
)
shell.download(filename, password())
