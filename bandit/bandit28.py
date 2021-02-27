from util import *

shell = open_ssh()
path = shell.system("mktemp -d").recvallS().strip().rstrip("/")

repo_path = "ssh://bandit28-git@localhost/home/bandit28-git/repo"
proc = shell.system(f"cd {path}; git clone {repo_path}")
proc.sendline("yes")
proc.sendline(get_pass_prev())

proc = shell.system(f"cd {path}/repo; git show | grep -e '-- password'")
pwd = proc.recvallS().split()[-1]

write(password(), pwd)

shell.system(f"rm -fdr {path}")
