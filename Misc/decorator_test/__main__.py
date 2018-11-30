from retrying_qslogger.retrying_qslogger import retry
import random

class best_of():
    deploy = 'z1234'
    def __init__(self):
        deploy = '1234ss'

    def set_deploy(self):
        deploy = 'cderfv'

    @retry(stop_max_attempt_number=10, wait_fixed=1000)
    def abcd(self, inp):
        inp = random.random() * inp
        try:
            if inp > 10:
                print 'exception'
                raise Exception('yay')
            else:
                print 'no exception'
        except Exception as e:
            print ('aaa')
            raise e

myClass = best_of()
myClass.set_deploy()
myClass.abcd(30)
pass