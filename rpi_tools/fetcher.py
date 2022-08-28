import logging
import sys

from .ftp_cli import FTP_IF
from .settings import HOME

log = logging.getLogger()
log.setLevel(logging.INFO)

def get_notes():
    get_file('all_notes.txt')

def get_file(fname):
    ftp_if = FTP_IF()
    ftp_if.get(HOME/"ftp"/fname, f"files/{fname}")

if __name__ == "__main__":
    get_notes()
    #get_file(sys.argv[1])
