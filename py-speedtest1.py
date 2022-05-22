#!/usr/bin/env python

# test internet speed

import speedtest

def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])
    
print("starting internet speed test")
 
# Speed test
st = speedtest.Speedtest()
 
# Download Speed
ds = st.download()
print(humansize(ds))

# Upload Speed
ds = st.upload()
print(ds)
print(humansize(ds))

print("internet speed test is over")

# ~ starting internet speed test
# ~ 23.41 MB
# ~ 215308988.6536271
# ~ 205.33 MB
# ~ internet speed test is over
