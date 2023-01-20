import atexit
from ftplib import FTP
import os

import rpi_tools.ftp_cli.ftp_config as ftp_config


class FTP_IF:
    def __init__(self, config=None):
        if config is None:
            self.config = ftp_config.default
        else:
            self.config = config
        ftp_server = self.config['server']
        user = self.config['user']
        passwd = self.config['passwd']

        self.ftp = FTP(ftp_server)
        self.ftp.login(user, passwd)
        atexit.register(self.ftp.quit)

    def get(self, localf, remotef):
        self.ftp.retrbinary("RETR " + remotef ,open(localf, 'wb').write)

    def put_stream(self, stream, remotef):
        self.ftp.storlines(f"STOR {remotef}", stream)

    def put(self, localf, remotef):
        self.ftp.storbinary(f"STOR {remotef}", open(localf, "rb"), 1024)

    def list(self):
        self.ftp.retrlines("LIST")



if __name__ == "__main__":
    ftp_cli = FTP_IF()
    ftp_cli.list()
    # local_fname = "/tmp/note_kjhlzl.txt"
    # remote_fname = "/files/test.txt"
    # ftp_cli.put(local_fname, remote_fname)
