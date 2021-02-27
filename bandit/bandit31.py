from util import *

shell = open_ssh()

with clone_git(shell) as path:
    shell.system(f"rm {path}/.gitignore")
    shell.upload_data("May I come in?", f"{path}/key.txt")

    proc = shell.system(f"cd {path}; git add .; git commit -m'c'; git push")
    auth_git(proc)

    proc.recvuntil("Here is the password")
    proc.recvuntil("\n")
    pwd = proc.recvlineS().split()[-1]

write(password(), pwd)
