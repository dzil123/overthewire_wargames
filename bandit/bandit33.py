from util import *

shell = open_ssh()
shell.download("README.txt", password())
