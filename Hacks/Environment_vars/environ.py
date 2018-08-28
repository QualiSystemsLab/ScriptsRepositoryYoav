import os
environ = os.environ.data
for k in environ:
    print 'Key: {0} , Value:{1}'.format(k, environ.get(k))
pass