from util import *

get_pass_prev()

shell = open_ssh_raw(keyfile=password_prev())
pwd_prev = shell.download_data("/etc/bandit_pass/bandit14")

# proc = shell.system("nc localhost 30000")
proc = shell.connect_remote("localhost", 30000)
proc.sendline(pwd_prev)
proc.recvuntil("Correct!")
pwd = proc.recvall().strip()

write(password(), pwd)
