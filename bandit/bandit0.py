from util import *

shell = open_ssh("bandit0")
shell.download("readme", password())
