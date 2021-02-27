from util import *

shell = open_ssh()

# the password is visible in the latest commit diff

with clone_git(shell) as path:
    proc = shell.system(f"cd {path}; git show | grep -e '-- password'")
    pwd = proc.recvallS().split()[-1]

write(password(), pwd)
