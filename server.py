import socket


quary_type_0='device_desc_0'
quary_type_1='device_desc_1'
quary_type_2='device_desc_2'
action_id_0='action=0'
action_id_1='action=1'
action_id_2='action=2'

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print ('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(2048)
    print (request,'\n')
    if quary_type_0.encode('utf-8') in request:
        http_response = 'device_desc_0 received'
    elif quary_type_1.encode('utf-8') in request:
        http_response = 'device_desc_1 received'
    elif quary_type_2.encode('utf-8') in request:
        http_response = 'device_desc_2 received'
    else:
        http_response = 'no device_desc received'

    if action_id_0.encode('utf-8') in request:
        http_response = http_response + ' ' + 'action_id_0 received'
    elif action_id_1.encode('utf-8') in request:
        http_response = http_response + ' ' + 'action_id_1 received'
    elif action_id_2.encode('utf-8') in request:
        http_response = http_response + ' ' + 'action_id_2 received'
    else:
        http_response = http_response + ' ' + 'no action received'    
        
    client_connection.sendall(http_response.encode('utf-8'))
    client_connection.close()
