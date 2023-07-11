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
    archive_path = "versions/web_static_{}.tgz".format(dtf)

    local("mkdir -p versions")

    local("tar -cvzf {} web_static".format(archive_path))

    if exists(archive_path):
        return archive_path
    else:
        return None
