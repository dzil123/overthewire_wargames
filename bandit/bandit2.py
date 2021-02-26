from util import *

shell = open_ssh()
shell.download("spaces\\ in\\ this\\ filename", password())
