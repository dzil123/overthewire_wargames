from util import *

path = "/tmp/file.log"

shell = open_ssh()

# the binary prints out the hardcoded path
shell.system(f"ln -s /etc/leviathan_pass/leviathan6 {path}")
pwd = shell.system("./leviathan5").readlineS()

write(password(), pwd)
