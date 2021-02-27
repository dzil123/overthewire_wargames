from util import *

shell = open_ssh()
path = shell.system("mktemp -d").recvallS().strip().rstrip("/")

repo_path = "ssh://bandit29-git@localhost/home/bandit29-git/repo"
proc = shell.system(f"cd {path}; git clone {repo_path}")
proc.sendline("yes")
proc.sendline(get_pass_prev())

script = f"cd {path}/repo; cat .git/objects/pack/pack*.idx | git show-index | cut -d' ' -f2"
script += " | xargs -l git cat-file blob 2>/dev/null | grep password "

proc = shell.system(script)

for line in proc.recvallS().split("\n"):
    if "no passwords in production" in line:
        continue
    pwd = line.split()[-1]
    break

write(password(), pwd)

shell.system(f"rm -fdr {path}")
