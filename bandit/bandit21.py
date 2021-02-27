from util import *

shell = open_ssh()

script = shell.download_data("/usr/bin/cronjob_bandit22.sh")

# find 'cat password > path/to/file' in the script (don't hardcode filename)
path = re.search(r"\>\s*([/\w]*)", str(script)).group(1)

pwd = shell.download_data(path)

write(password(), pwd)
