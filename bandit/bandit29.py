from util import *

shell = open_ssh()

# I don't really understand the theory behind this
# this reads out all the packed objects inside the pack.idx file using 'git show-index'
# then 'git cat-file blob' will print out each object if it is a file (not a tree/commit/etc)
script = "cat .git/objects/pack/pack*.idx | git show-index | cut -d' ' -f2 | "
script += "xargs -l git cat-file blob 2>/dev/null | grep password | grep -v 'no passwords in production'"

with clone_git(shell) as path:
    proc = shell.system(f"cd {path}; {script}")

    for line in proc.recvallS().split("\n"):
        pwd = line.split()[-1]
        break

write(password(), pwd)
