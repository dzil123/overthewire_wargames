from util import *

shell = open_ssh()
shell.download_file("CONGRATULATIONS", password())
