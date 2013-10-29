import importlib
import inspect
import os
import sys

from .testing import TestCase

import nose
from nose.suite import ContextSuite

def runtests():
    files = []
    dirs = set()
    for modname in sys.argv[1:]:
        files.append(modname)

        mod = importlib.import_module(modname)
        fname = mod.__file__
        dirs.add(os.path.dirname(fname))

    print "files:"
    for f in files: print '  %s' % f
    print "dirs:"
    for f in dirs: print '  %s' % f
    files = list(dirs) + files
    print "  all: %s" % files
    print "=" * 20
    nose.run(argv=files + ['-v'],)

def runsuite():
    funcs = [m[1] for m in
             inspect.getmembers(TestCase, inspect.ismethod)]
    print funcs
    nose.run(suite=ContextSuite(
        tests=funcs,
        context=TestCase))
