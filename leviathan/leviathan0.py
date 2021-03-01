from util import *

shell = open_ssh("leviathan0")

pwd = shell.system("grep .backup/bookmarks.html -e password").recvallS()
pwd = re.search("the password for leviathan1 is (\w+)", pwd).group(1)

write(password(), pwd)
