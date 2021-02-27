from util import *

shell = open_ssh()
shell.download("bandit26.sshkey", password())
