#!/usr/bin/python3
""" script that generates a .tgz archive from the
    contents of the web_static folder
"""
from datetime import datetime
from fabric.api import local
from os.path import exists


def do_pack():
    """ function that generates a .tgz archive """

    dtf = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{dtf}.tgz"

    if not exists("versions"):
        local("mkdir versions")

    local(f"tar -cvzf {archive_path} web_static")

    if exists(archive_path):
        return archive_path
    else:
        return None
