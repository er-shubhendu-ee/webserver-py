import socket

# quary types
#quary = 'q?'
quary_type_0='device_id_0'
quary_type_1='device_id_1'
quary_type_2='device_id_2'
action_id_0='action=0'
action_id_1='action=1'
action_id_2='action=2'

# accepts quary string, seperator and return quary value
def quary_parameter_value(quary_string = '0', request_string = '0', seperator = '0'):
    quary = quary_string
    if quary in request_string:
        value_index=0
        action_value1='0'
        action_id_start_index=request_string.find( 'action=')
        print ( 'action_id_start_index',action_id_start_index, '\n')
        if action_id_start_index!=-1:
            action_value_start_index=action_id_start_index+len('action=')
            value_index=action_value_start_index
            print( 'index value',value_index)
            print ( 'character at' ,value_index, ',',request_string[value_index])
            print( 'request_string:', request_string)
            while ( request_string[ value_index] != seperator):
                action_value1=action_value1+request_string[value_index]
                value_index+=1
                print ( 'index value', value_index)
                print ( 'action value', action_value1)
    else:
        action_value1=-1
    return action_value1

#  host and port definitio
HOST, PORT = '', 8888

# creating a socket for connection
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set socket options
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# binding the socket to host and port
listen_socket.bind((HOST, PORT))

# start listening
listen_socket.listen(1)

# print status
print ('Serving HTTP on port %s ...' % PORT)

# work for ever
while True:

# if there is an incoming connection, accept it for processing
    client_connection, client_address = listen_socket.accept()

# receive the request string, string is in byte format
    request = client_connection.recv(2048)

# print request string, data type and byte quantity
    print( request,'\n')
    print( type( request),'\n') 
    print( 'bytes received : ',len( request))


# http error 404:
    http_response=' http error 404: not found.'


# testing extracting quary parameter values from the request string received
    request_string=request.decode('utf-8')
    quary_value = quary_parameter_value( 'q?', request_string, ' ')
    print( 'quary value: ',quary_value)

# handle quary and set rsponse data as string
    if quary_type_0.encode('utf-8') in request:
        http_response = 'device_id_0 received'
    elif quary_type_1.encode('utf-8') in request:
        http_response = 'device_id_1 received'
    elif quary_type_2.encode('utf-8') in request:
        http_response = 'device_id_2 received'
    else:
        http_response = 'no device_id received'
    if action_id_0.encode('utf-8') in request:
        http_response = http_response + ' ' + 'action_id_0 received'
    elif action_id_1.encode('utf-8') in request:
        http_response = http_response + ' ' + 'action_id_1 received'
    elif action_id_2.encode('utf-8') in request:
        http_response = http_response + ' ' + 'action_id_2 received'
    else:
        http_response = http_response + ' ' + 'no action received'    

# format response string in byte formation and send to the client       
    client_connection.sendall(http_response.encode('utf-8'))

# close the connection and print bytes sent
    client_connection.close()
    print( 'bytes sent : ',len( http_response),'\n','\n','\n')


