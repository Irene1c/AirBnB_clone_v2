#!/usr/bin/python3
""" script that distributes an archive to your web servers"""
from fabric.api import env, run, put
from os.path import exists

env.hosts = ['34.229.137.176', '100.26.155.24']


def do_deploy(archive_path):
    """function that distributes an archive to your web servers"""

    if exists(archive_path):
        try:
            put(local_path=archive_path, remote_path='/tmp/')
            n_path = archive_path.split('/')
            n_file = n_path[1]
            new = n_file.split('.')
            n_dir = new[0]
            folder = '/data/web_static/releases/{}'.format(n_dir)
            run('mkdir -p {}'.format(folder))
            run('tar -xzf /tmp/{} -C {}'.format(n_file, folder))
            run('rm /tmp/{}'.format(n_file))
            run('mv {}/web_static/* {}'.format(folder, folder))
            run('rm -rf {}/web_static'.format(folder))
            run('rm -rf /data/web_static/current')
            run('ln -s {} /data/web_static/current'.format(folder))
            return True
        except Exception as f:
            return False
    else:
        return False
