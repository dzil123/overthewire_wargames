from util import *

shell = open_ssh()

# 'check' is a suid binary that opens 'sh' as the next user if we guess the password
proc = shell.system("./check")
# go into gdb, see what is the parameter to the strcmp call
proc.sendline("sex")  # yes this is the password
# it drops us into a shell

proc.send("cat /etc/leviathan_pass/leviathan2")
proc.clean(0.5)
proc.sendline()
pwd = proc.recvline()

write(password(), pwd)
