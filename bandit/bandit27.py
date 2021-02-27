from util import *

shell = open_ssh()
path = shell.system("mktemp -d").recvallS().strip().rstrip("/")

repo_path = "ssh://bandit27-git@localhost/home/bandit27-git/repo"
proc = shell.system(f"cd {path}; git clone {repo_path}")
proc.sendline("yes")
proc.sendline(get_pass_prev())

pwd = shell.download_data(f"{path}/repo/README").split()[-1]

write(password(), pwd)

shell.system(f"rm -fdr {path}")
