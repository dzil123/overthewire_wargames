import importlib
import inspect
import logging
import re

import pwnlib
from pwn import *

PASSWORD_FILE = "bandit{}.out"

# setting log level disables other stuff I dont want to disable, so I just nop this function instead
ssh.checksec = lambda *args: ""


def get_challenge(stack=1):
    return int(re.search(r"bandit(\d+)\.py$", inspect.stack()[stack].filename).group(1))


def password(c=None):
    if c is None:
        c = get_challenge(2)
    return PASSWORD_FILE.format(c)


def password_prev():
    """ not to be called from util """
    return password(get_challenge(2) - 1)


def get_pass(c=None):
    if c is None:
        c = get_challenge(2)
    filename = password(c)

    def _read():
        return read(filename).strip()

    try:
        return _read()
    except FileNotFoundError:
        importlib.import_module(f"bandit{c}")
        return _read()


def get_pass_prev():
    """ not to be called from util """
    return get_pass(get_challenge(2) - 1)


def open_ssh_raw(c=None, *args, **kwargs) -> pwnlib.tubes.ssh.ssh:
    if c is None:
        c = get_challenge(2)

    log.info("Running challenge #%s", c)
    return ssh(f"bandit{c}", "bandit.labs.overthewire.org", 2220, *args, **kwargs)


def open_ssh(password=None, c=None) -> pwnlib.tubes.ssh.ssh:
    if c is None:
        c = get_challenge(2)

    if password is None:
        password = get_pass(c - 1)

    return open_ssh_raw(c, password)
