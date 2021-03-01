from util import *

shell = open_ssh()

# the binary asks for a 4 digit pin
# go into gdb, read the parameter to the cmp instruction
proc = shell.system("./leviathan6 7123")

proc.send("cat /etc/leviathan_pass/leviathan7")
proc.clean(0.5)
proc.sendline()
pwd = proc.recvline()

write(password(), pwd)
