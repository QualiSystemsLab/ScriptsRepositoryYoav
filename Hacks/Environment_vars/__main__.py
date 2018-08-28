import os

def print_all_env_vars():
    environ = os.environ.data
    for k in environ:
        print 'Key: {0} , Value:{1}'.format(k, environ.get(k))


if __name__ == "__main__":
    print_all_env_vars()
