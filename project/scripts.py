import importlib, os, sys
import nose

def runtests():
    modnames = []
    dirs = set()
    for modname in sys.argv[1:]:
        modnames.append(modname)

        mod = importlib.import_module(modname)
        fname = mod.__file__
        dirs.add(os.path.dirname(fname))

    modnames = list(dirs) + modnames

    nose.run(argv=modnames
             # + ['-v']
             # + ['-a', 'safe']
    )

#######################################################
# doesn't work:

import inspect

from .testing import TestCase

from nose.suite import ContextSuite

def runsuite():
    funcs = [m[1] for m in
             inspect.getmembers(TestCase, inspect.ismethod)]
    print funcs
    nose.run(suite=ContextSuite(
        tests=funcs,
        context=TestCase))
