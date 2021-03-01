import contextlib
import importlib
import inspect

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


def open_ssh_key() -> pwnlib.tubes.ssh.ssh:
    c = get_challenge(2)
    c_prev = c - 1

    get_pass(c_prev)
    return open_ssh_raw(c, keyfile=password(c_prev))


def get_port() -> int:
    return randint(40_000, 60_000)


@contextlib.contextmanager
def force_term_size(*, w=None, h=None):
    old_height = term.height

    def do_resize():
        if w is not None:
            term.width = term.term.width = w
        if h is not None:
            term.height = term.term.height = h

            # this is copy pasted from pwnlib.term.term.update_geometry
            # without it "AttributeError: 'Cell' object has no attribute 'end'"
            cells = term.term.cells
            if cells and cells[-1].end[0] < 0:
                delta = min(old_height - h, 1 - cells[-1].end[0])
                for cell in cells:
                    cell.end = (cell.end[0] + delta, cell.end[1])
                    cell.start = (cell.start[0] + delta, cell.start[1])

    do_resize()

    old_on_winch = term.term.on_winch

    old_update_geometry = term.term.update_geometry
    term.term.update_geometry = lambda: None

    old_redraw = term.term.redraw
    term.term.redraw = lambda: None

    try:
        term.term.on_winch = [do_resize] + old_on_winch[:]

        for handler in term.term.on_winch:
            handler()

        term.term.handler_sigwinch(None, None)

        yield
    finally:
        term.term.on_winch = old_on_winch

        term.term.update_geometry = old_update_geometry
        term.term.redraw = old_redraw

        term.term.handler_sigwinch(None, None)


@contextlib.contextmanager
def temp_dir(shell):
    path = shell.system("mktemp -d").recvallS().strip().rstrip("/")

    try:
        yield path
    finally:
        shell.system(f"rm -fdr {path}")


@contextlib.contextmanager
def clone_git(shell):
    c = get_challenge(3)
    repo_path = f"ssh://bandit{c}-git@localhost/home/bandit{c}-git/repo"

    with temp_dir(shell) as path:
        proc = shell.system(f"cd {path}; git clone {repo_path}")
        auth_git(proc, c - 1)

        yield f"{path}/repo"


def auth_git(proc, c=None):
    if c is None:
        c = get_challenge(2) - 1

    proc.sendline("yes")
    proc.sendline(get_pass(c))
