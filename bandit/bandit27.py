from util import *

shell = open_ssh()

with clone_git(shell) as path:
    pwd = shell.download_data(f"{path}/README").split()[-1]

write(password(), pwd)
