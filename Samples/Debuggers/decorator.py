from cloudshell.core.logger import qs_logger

class Elephant:

    def __init__(self, fnc):
        self._fnc = fnc
        self._memory = []

    def __call__(self, *args, **kwargs):
        retval = self._fnc(cls, *args, **kwargs)
        self._memory.append(retval)
        return retval

    def memory(self):
        return self._memory



class decorator_test(object):
    def __init__(self):
        self.logger = qs_logger.get_qs_logger(
            log_group='decorator_test1',
            log_category='decorator_test2',
            log_file_prefix='decorator_test3'
        )

    @Elephant
    def get_text(self, name):
        self.logger.info('1234')
        return "Hello" + name

dec_test = decorator_test()
print dec_test.get_text(' lalala')
print dec_test.get_text(' lalawwwwwla')
# print(dec_test.get_text.memory())


