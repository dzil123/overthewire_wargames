from util import *

shell = open_ssh_key()

proc = shell.system("diff passwords.old passwords.new")
proc.recvuntil("> ")
pwd = proc.recvline()

write(password(), pwd)
