import xml.etree.ElementTree as ET

from util import *

pwd_prev = get_pass_prev()
shell = open_ssh()

proc = shell.system("nmap -oX - -p 31000-32000 localhost")
xml = proc.recvall().strip()


xml = ET.fromstring(xml)
for port in xml.find("host").find("ports").iter("port"):
    if port.find("state").get("state") != "open":
        continue

    port = port.get("portid")

    with shell.system(f"openssl s_client -connect localhost:{port}") as proc:
        proc.clean(0.5)
        if not proc.connected("in"):
            continue  # the port did not respond to ssl connection

        proc.sendline(pwd_prev)

        if not proc.recvuntil("Correct!", timeout=0.5):
            continue  # "...the others will simply send back to you whatever you send to it"

        log.info("Found on port %s", port)
        pwd = proc.recvuntil("closed", True).strip()
        break

else:
    log.critical("Could not find correct port")
    exit()

write(password(), pwd)
