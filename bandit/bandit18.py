from util import *

shell = open_ssh()
shell.download("readme", password())
