# Execute `certbot renew`

import random
import time
import subprocess

time.sleep(random.random()*60)

command = ['/usr/local/bin/certbot', 'renew']

try:
    subprocess.check_call(command)
except:
    print('cerbot renew error.')