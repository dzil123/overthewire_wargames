from util import *

shell = open_ssh()

proc = shell.shell()
proc.sendline("$0")
proc.send("cat /etc/bandit_pass/bandit33")
proc.clean(0.5)
proc.sendline()

pwd = proc.clean(0.5).split()[0]

write(password(), pwd)
