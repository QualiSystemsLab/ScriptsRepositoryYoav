import random
from retrying_qslogger.retrying_qslogger import retry
import os

@retry(stop_max_attempt_number=5)
def do_something_unreliable():
    if random.randint(0, 10) > 0:
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"

env_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "..")
shell_name = os.path.basename(os.path.abspath(env_folder))
print do_something_unreliable()