import logging
import logging.config
import sys

from .settings import FTP_PATH, LOGGING_CONFIG

log = logging.getLogger('root')

'''
    python -m ftp_tools.ftp_handler [ "note" | "file" ] <filepath>
'''

def handle_note(note_fname):
    log.info(f"handling note {note_fname}")
    with open(note_fname) as f:
        note = f.read()
    log.debug(f"{note=}")
    with open(FTP_PATH/'files/all_notes.txt', 'a') as f:
        f.write(note)
    log.info(f"wrote {note_fname} to {FTP_PATH/'files.all_notes.txt'}")


def handle_file(file_fname):
    log.info(f"handling file {file_fname}")


def handler(event):

    if event['type'] == "note":
        handle_note(event['input'])
    elif event['type'] == 'file':
        handle_file(event['input'])
    else:
        log.error(f"unexpected input type: {event}")
        raise TypeError()


def main():
    logging.config.dictConfig(LOGGING_CONFIG)
    log.debug(f"ftp handler args: {sys.argv=}")

    etype = sys.argv[1]
    fname = sys.argv[2]
    event = {
            "type": etype,
            "input": fname,
            }
    log.info(f"ftp handler invoked with {event=}")
    handler(event)

if __name__ == "__main__":
    main()
