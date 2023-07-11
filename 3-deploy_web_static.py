#!/usr/bin/python3
""" script that creates and distributes an archive to your web servers"""
from fabric.api import env
from os.path import exists


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['34.229.137.176', '100.26.155.24']


def deploy():
    """function that that creates and distributes
        an archive to your web servers
    """

    c_archive = do_pack()
    if not exists(c_archive):
        return False
    else:
        result = do_deploy(c_archive)
        return result
