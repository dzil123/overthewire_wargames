from util import *

shell = open_ssh()
shell.download("inhere/.hidden", password())
