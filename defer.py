"""
    Golang style error handling.
"""
import inspect
import sys


def panic(err):
    raise Exception(err)


def defer(func):
    for f in inspect.stack():
        if '__defers__' in f[0].f_locals:
            f[0].f_locals['__defers__'].append(func)
            break


def recover():
    val = None
    for f in inspect.stack():
        loc = f[0].f_locals
        if f[3] == '__exit__' and '__suppress__' in loc:
            val = loc['exc_value']
            loc['__suppress__'].append(True)
            break
    return val


class DefersContainer:
    def __init__(self) -> None:
        # List for sustain refer in shallow clone
        self.defers = []

    def append(self, defer):
        self.defers.append(defer)

    def __enter__(self):
        pass
    
    def __exit__(self, exc_type, exc_value, traceback):
        __suppress__ = []
        for d in reversed(self.defers):
            try:
                d()
            except:
                __suppress__ = []
                exc_type, exc_value, traceback = sys.exc_info()
        return __suppress__


def defers_collector(func):
    def __wrap__(*args, **kwargs):
        __defers__ = DefersContainer()
        with __defers__:
            func(*args, **kwargs)
        return __wrap__

