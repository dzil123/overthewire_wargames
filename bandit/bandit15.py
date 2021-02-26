from util import *

pwd_prev = get_pass_prev()
shell = open_ssh()

proc = shell.system("openssl s_client -connect localhost:30001")

proc.sendline(pwd_prev)
proc.recvuntil("Correct!")
pwd = proc.recvall().split()[0]

write(password(), pwd)
