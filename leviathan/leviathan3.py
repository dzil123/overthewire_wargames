from util import *

shell = open_ssh()

# the premise appears to be identical to leviathan1
# go into gdb, read the strcmp parameter
proc = shell.system("./level3")
proc.sendline("snlprintf")

proc.send("cat /etc/leviathan_pass/leviathan4")
proc.clean(0.5)
proc.sendline()
pwd = proc.recvline()

write(password(), pwd)
