from util import *

get_pass_prev()

shell = open_ssh_raw(keyfile=password_prev())

proc = shell.system("diff passwords.old passwords.new")
proc.recvuntil("> ")
pwd = proc.recvline()

write(password(), pwd)
