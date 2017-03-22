# https://ruslanspivak.com/lsbaws-part1/
import logging
import socket

logging.basicConfig(filename='{}.log'.format('webserver1'), level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

# For more reading about socket programming, see
# An Introductory 4.3BSD Interprocess Communication Tutorial, by Stuart Sechrest
# An Advanced 4.3BSD Interprocess Communication Tutorial, by Samuel J. Leffler et al,

logger.info("Serving HTTP on port {} ... ".format(PORT))
http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode('utf-8')
    logger.info(request)
    client_connection.sendall(bytes(http_response, 'utf-8'))
    client_connection.close()
