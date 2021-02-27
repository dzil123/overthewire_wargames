from util import *

shell = open_ssh()

script = "cat .git/objects/pack/pack*.idx | git show-index | cut -d' ' -f2 | "
script += "xargs -l git cat-file blob 2>/dev/null | grep -v 'just an epmty file' "

with clone_git(shell) as path:
    proc = shell.system(f"cd {path}; {script}")
    pwd = proc.recvallS().strip()

write(password(), pwd)
