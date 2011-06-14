#!/usr/bin/env python
import os, sys, glob, fnmatch
from exceptions import ImportError

#join and normalize paths
def opj(*args):
    path = os.path.join(*args)
    return os.path.normpath(path)

#recursive walker for package data files
def find_data_files(srcdir, *wildcards, **kw):
    # get a list of all files under the srcdir matching wildcards,
    # returned in a format to be used for install_data
    def walk_helper(arg, dirname, files):
        if '.svn' in dirname:
            return
        names = []
        lst, wildcards = arg
        for wc in wildcards:
            wc_name = opj(dirname, wc)
            for f in files:
                filename = opj(dirname, f)

                if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                    names.append(filename)
        if names:
            lst.extend( names )

    file_list = []
    recursive = kw.get('recursive', True)
    if recursive:
        os.path.walk(srcdir, walk_helper, (file_list, wildcards))
    else:
        walk_helper((file_list, wildcards),
                    srcdir,
                    [os.path.basename(f) for f in glob.glob(opj(srcdir, '*'))])
    return file_list

#the recursive walker returns full paths, but we need to get rid of the
#package top dir
files = find_data_files('narcissist/project_template/', '*.*')
files = ['/'.join(os.path.normpath(fn).split("/")[1:]) for fn in files]

dist_kwargs = {
    'name': 'narcissist',
    'version': '0.1',
    'description': 'Deployable personal info web app / web service aggregator.',
    'author': 'Dejan Noveski',
    'author_email': 'dr.mote@gmail.com',
    'url': '',
    'packages': ['narcissist',
              'narcissist.services',],
    'package_data': {"narcissist": files},
    'scripts': ['narcissist/narcissist_create'],
    'requires': [
      "flask (>=0.6)",
    ],
    'platforms': 'any',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
}

try:
    from setuptools import setup
    dist_kwargs["install_requires"] = ["flask>=0.6", "argparse"]
    setup(**dist_kwargs)
except ImportError:
    from distutils.core import setup
    setup(**dist_kwargs)