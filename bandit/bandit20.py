from util import *

port = get_port()

shell = open_ssh()
conn = shell.listen_remote(port)
proc = shell.system(f"./suconnect {port}")

conn.sendline(get_pass_prev())
proc.recvall()
proc.wait_for_close()

pwd = conn.recvall().strip()

write(password(), pwd)
