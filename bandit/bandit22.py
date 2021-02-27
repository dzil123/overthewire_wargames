from util import *

# recreation of /usr/bin/cronjob_bandit23.sh
username = "bandit23"
filename = md5sumhex(f"I am user {username}\n".encode())
path = f"/tmp/{filename}"

shell = open_ssh()
pwd = shell.download_data(path)

write(password(), pwd)
