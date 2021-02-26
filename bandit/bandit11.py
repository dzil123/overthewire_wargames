from util import *

rot13 = bytes.maketrans(
    b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    b"NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
)

shell = open_ssh()
pwd = shell.download_data("data.txt").translate(rot13).split()[-1]
write(password(), pwd)
