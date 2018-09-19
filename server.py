import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print ('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(2048)
    print (request)
    for i in range(0,10):
        print (request[i])
    quary_type='device_desc'
    quary_id_1='q=0'
    quary_id_2='q=1'
    if quary_type.encode('utf-8') in request:
        http_response='true:device_desc'
        if quary_id_1.encode('utf-8') in request:
            http_response='at 0'
            client_connection.sendall(http_response.encode('utf-8'))
            client_connection.close()
        elif quary_id_2.encode('utf-8') in request:
            http_response='at 1'
            client_connection.sendall(http_response.encode('utf-8'))
            client_connection.close()
        else:
            http_response='out of bound'
            client_connection.sendall(http_response.encode('utf-8'))
            client_connection.close()
    else:
        http_response = 'false:device_desc'
        client_connection.sendall(http_response.encode('utf-8'))
        client_connection.close()
