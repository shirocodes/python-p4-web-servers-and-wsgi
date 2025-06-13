#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

# function is decorated with the Request.application method, which tells it to run any code inside of the function in the browser 
# at the location we specify with our development server.
@Request.application 
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )