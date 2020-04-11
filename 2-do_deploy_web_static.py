#!/usr/bin/python3
''' point 2 deploy '''
import os
from fabric.api import *
''' os.paht = routes to directories and files, create folders '''
''' fabric.api = create tgz files '''
''' datetime = in order to get current date and time '''


def do_deploy(archive_path):
    ''' function to deploy archive '''
    if not os.path.exists(archive_path):
        return False
    else:
        env.hosts = ['35.231.52.206', '54.226.104.83']
        with Connection(env.hosts[0]) as c:
            c.put("{}".format(archive_path), "/tmp/")
