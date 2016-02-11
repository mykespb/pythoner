#!/usr/bin/env python3
# myke py-flup1.py
# test of flup server OK

from html import escape

def application(environ, start_response):

    envvar = ['%s=%s' % (key, value) for key, value in sorted(environ.items())]

    body = ('<html><body><h2>h€lló wörld (python3 fcgi)</h2><pre>' + escape('\n'.join(envvar)) + '</pre></body></html>').encode()
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf-8'), ('Content-Length', str(len(body)))]
    start_response(status, headers)

    return [body]

if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(application).run()


#~ h€lló wörld (python3 fcgi)

#~ CONTEXT_DOCUMENT_ROOT=/var/www
#~ CONTEXT_PREFIX=
#~ DOCUMENT_ROOT=/var/www
#~ GATEWAY_INTERFACE=CGI/1.1
#~ HTTP_ACCEPT=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
#~ HTTP_ACCEPT_ENCODING=gzip, deflate, sdch
#~ HTTP_ACCEPT_LANGUAGE=ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4
#~ HTTP_CONNECTION=keep-alive
#~ HTTP_COOKIE=_ym_uid=1446682061546023946; orguidview=fOxobruU; rid=to6vzBJN; _ym_isad=0; q=IQZvAzmq; tz=+03; uid=10000000; orguid=10000000; orgid=10000000
#~ HTTP_HOST=localhost
#~ HTTP_UPGRADE_INSECURE_REQUESTS=1
#~ HTTP_USER_AGENT=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36
#~ HTTP_X_COMPRESS=null
#~ PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
#~ PATH_INFO=
#~ QUERY_STRING=
#~ REMOTE_ADDR=127.0.0.1
#~ REMOTE_PORT=52873
#~ REQUEST_METHOD=GET
#~ REQUEST_SCHEME=http
#~ REQUEST_URI=/test/py-flup1.py
#~ SCRIPT_FILENAME=/var/www/test/py-flup1.py
#~ SCRIPT_NAME=/test/py-flup1.py
#~ SERVER_ADDR=127.0.0.1
#~ SERVER_ADMIN=webmaster@localhost
#~ SERVER_NAME=localhost
#~ SERVER_PORT=80
#~ SERVER_PROTOCOL=HTTP/1.1
#~ SERVER_SIGNATURE=<address>Apache/2.4.7 (Ubuntu) Server at localhost Port 80</address>

#~ SERVER_SOFTWARE=Apache/2.4.7 (Ubuntu)
#~ wsgi.errors=<_io.TextIOWrapper name='<stderr>' mode='w' encoding='ANSI_X3.4-1968'>
#~ wsgi.input=<_io.TextIOWrapper name='<stdin>' mode='r' encoding='ANSI_X3.4-1968'>
#~ wsgi.multiprocess=True
#~ wsgi.multithread=False
#~ wsgi.run_once=True
#~ wsgi.url_scheme=http
#~ wsgi.version=(1, 0)

