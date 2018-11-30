import time
from cloudshell.core.logger import qs_logger


def timeit(method):

    def timed(*args, **kw):


        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed

class Foo(object):

    @timeit(qqq='abc')
    def foo(self):
        time.sleep(1.2)

@timeit
def f1():
    time.sleep(1)
    print 'f1'

a = Foo()
a.foo()
pass