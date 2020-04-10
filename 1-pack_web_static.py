#!/usr/bin/python3
''' point 1 create tgz '''
import os.path
import datetime
from fabric.api import local
''' os.paht = routes to directories and files, create folders '''
''' fabric.api = create tgz files '''
''' datetime = in order to get current date and time '''


def do_pack():
    ''' function to pack in tgz file '''
    if not os.path.exists('./versions'):
        os.mkdir('versions')
    if os.path.exists('./web_static'):
        now = datetime.datetime.now()
        b = "web_static_"
        ny = now.year
        nm = now.month
        nd = now.day
        nh = now.hour
        nmi = now.minute
        ns = now.second
        e = ".tgz"
        n = "{}{}{}{}{}{}{}{}".format(b, ny, nm, nd, nh, nmi, ns, e)
        tgzfile = local('tar -cvzf versions/{} web_static'.format(n))
        if tgzfile.failed:
            return None
        return 'versions/{}'.format(n)
