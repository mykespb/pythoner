#!/usr/bin/env python3
# Mikhail (myke) Kolodin
# testing redis and redis-queue (rq)
# from http://python-rq.org/ etc
# 2016-02-04 2018-05-05 1.4

import redis
import requests
from redis import Redis
from rq import Queue

# test redis itfself

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
x = r.get('foo')
print (x)

q = Queue(connection=Redis())

from rq_my_module import count_words_at_url
result = q.enqueue (count_words_at_url, 'http://nvie.com')
print (result)


# my_module.py is:

#~ #!/usr/bin/env python3

#~ import requests
#~ from redis import Redis
#~ from rq import Queue

#~ # test redis queue (rq))

#~ def count_words_at_url(url):
    #~ resp = requests.get(url)
    #~ return len(resp.text.split())

# in parallel, the worker runs:

#~ $ rq worker
#~ *** Listening for work on default
#~ Got count_words_at_url('http://nvie.com') from default
#~ Job result = 818
#~ *** Listening for work on default
