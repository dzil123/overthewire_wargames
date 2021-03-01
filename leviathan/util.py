import contextlib
import importlib
import inspect

import pwnlib
from pwn import *

PASSWORD_FILE = "leviathan{}.out"

# setting log level disables other stuff I dont want to disable, so I just nop this function instead
ssh.checksec = lambda *args: ""


def get_challenge(stack=1):
    return int(
        re.search(r"leviathan(\d+)\.py$", inspect.stack()[stack].filename).group(1)
    )


def password(c=None):
    if c is None:
        c = get_challenge(2)
    return PASSWORD_FILE.format(c)


def get_pass(c=None):
    if c is None:
        c = get_challenge(2)
    filename = password(c)

    def _read():
        return read(filename).strip()

    try:
        return _read()
    except FileNotFoundError:
        importlib.import_module(f"leviathan{c}")
        return _read()


def open_ssh_raw(c=None, *args, **kwargs) -> pwnlib.tubes.ssh.ssh:
    if c is None:
        c = get_challenge(2)

    log.info("Running challenge #%s", c)
    return ssh(f"leviathan{c}", "leviathan.labs.overthewire.org", 2223, *args, **kwargs)


def open_ssh(password=None, c=None) -> pwnlib.tubes.ssh.ssh:
    if c is None:
        c = get_challenge(2)

    if password is None:
        password = get_pass(c - 1)

    return open_ssh_raw(c, password)


@contextlib.contextmanager
def temp_dir(shell):
    path = shell.system("mktemp -d").recvallS().strip().rstrip("/")

    try:
        yield path
    finally:
        shell.system(f"rm -fdr {path}")
