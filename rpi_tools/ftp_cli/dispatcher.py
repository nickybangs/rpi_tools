import io
import logging
import sys

from .common import random_chars
from .ftp_if import FTP_IF

log = logging.getLogger()
log.setLevel(logging.INFO)

def send_note(note):
    ftp_if = FTP_IF()
    suffix = random_chars(6)
    note_name = f"/notes/note_{suffix}.txt"
    bio = io.BytesIO()
    bio.write(note.encode())
    bio.seek(0)
    log.info(f"note name = {note_name}, note={note}")
    ftp_if.put_stream(bio, note_name)

# send both misc files and files with an expected prefix + random chars
def send_file(fname):
    remotef = fname.split('/')[-1]
    ftp_if = FTP_IF()
    ftp_if.put(fname, f"files/{remotef}")
