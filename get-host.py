#!/usr/bin/env python3

# узнать имя и IP-адрес данного компьютера
# 2021-05-15 1.1
# Mikhail (myke) Kolodin

import socket

hostname = socket.gethostname()
IPaddr = socket.gethostbyname (hostname)

print ("Computer Name:", hostname)
print ("IP address:   ", IPaddr)

# ~ Computer Name:mykem
# ~ IP address:127.0.1.1
