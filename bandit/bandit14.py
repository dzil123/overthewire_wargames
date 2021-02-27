from util import *

shell = open_ssh_key()
pwd_prev = shell.download_data("/etc/bandit_pass/bandit14")

# proc = shell.system("nc localhost 30000")
proc = shell.remote("localhost", 30000)
proc.sendline(pwd_prev)
proc.recvuntil("Correct!")
pwd = proc.recvall().strip()

write(password(), pwd)
