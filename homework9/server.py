import re
import socket
from http import HTTPStatus


def get_headers(text):
    headers = re.findall(r'\n(.*?)\r', text)
    headers_list = []
    for header in headers:
        if header != '' and header is not None:
            split_values = re.split(': ', header)
            headers_list.append({split_values[0]: split_values[1]})
    return headers_list


def get_free_port_and_connect(port=1024, max_port=65535):
    s = socket.socket()
    while port <= max_port:
        try:
            srv_addr = ('', port)
            s.bind(srv_addr)
            print(f'starting on {srv_addr}')
            return s
        except OSError:
            port += 1
    raise IOError('no free ports')


sock = get_free_port_and_connect()
sock.listen(1)

while True:
    print('waiting for a connection')
    conn, raddr = sock.accept()
    print(sock)
    print(conn)

    print('connection from', raddr)
    while True:
        data = conn.recv(2056)
        text = data.decode('utf-8')
        print(f'received {repr(text)}')
        if text:
            method = re.search(r'(GET|POST|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE) ', text)
            headers_list = get_headers(text)
            try:
                status_code = re.search(r'\\?status=(.*) HTTP', text)
                if status_code is not None and status_code != '':
                    status = int(status_code.group(1))
                    if isinstance(HTTPStatus(status), HTTPStatus):
                        value = str(HTTPStatus(status).value)
                        text = HTTPStatus(status).phrase
                    else:
                        value = '200'
                        text = 'OK'
                else:
                    value = '200'
                    text = 'OK'
            except ValueError:
                value = '200'
                text = 'OK'

            status_line = f'HTTP/1.1 {value} {text}'
            request_method = f'<p>Request Method: {method.group(1)}<p>\r\n'
            request_source = f'<p>Request Source: {raddr}<p>\r\n'
            request_code = f'<p>Response Status Code: {value}<p>\r\n'

            response = '\r\n\r\n'.join([
                status_line,
                request_method,
                request_source,
                request_code
            ])
            sent_bytes = conn.send(response.encode('utf-8'))
            for header in headers_list:
                for key, value in header.items():
                    dict = '<p>{} : {}<p>\r\n'.format(key, value)
                    conn.send(dict.encode('utf-8'))
            print('data was sent')
        else:
            print(f'no data from {raddr}')
            break
    conn.close()
