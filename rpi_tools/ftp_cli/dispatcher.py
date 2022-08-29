import io
import logging
import random
import sys

from .ftp_if import FTP_IF

log = logging.getLogger()
log.setLevel(logging.INFO)

def random_char():
    return chr(random.randint(ord('a'), ord('z')))

def random_chars(num):
    return ''.join([random_char() for i in range(num)])

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

if __name__ == "__main__":
    # send_note(sys.argv[1])
    send_file(sys.argv[1])
