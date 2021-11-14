# -*- coding:latin-1 -*-
from oops import oops


def safe(func, *args):
    try:
        func(*args)
    except Exception:
        import sys
        print(sys.exc_info())


safe(oops)

