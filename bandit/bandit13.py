from util import *

shell = open_ssh()
shell.download("sshkey.private", password())
