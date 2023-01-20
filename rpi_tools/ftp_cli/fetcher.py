import logging
import sys

from .common import random_chars
from .ftp_if import FTP_IF
from .settings import HOME

log = logging.getLogger()
log.setLevel(logging.INFO)

def get_notes():
    get_file('all_notes.txt')

def get_file(fname):
    ftp_if = FTP_IF()
    ftp_if.get(HOME/"ftp"/fname, f"/files/{fname}")
    prefix = random_chars(4)
    ftp_if.rename(f"/files/{fname}", f"/archive/{prefix}_{fname}")

def list_files():
    ftp_if = FTP_IF()
    ftp_if.list("files")

if __name__ == "__main__":
    get_file('todo')
