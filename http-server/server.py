"""HTTP Server"""
import random
from socket import *
from genericpath import isfile

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', 8080))

print(f'Listening on {serverSocket.getsockname()}...')
print('Press Ctrl+C to close the server\r\n')

serverSocket.listen(5)
print('Waiting for a client to connect...\r\n')

while True:
    try:
        clientSocket, address = serverSocket.accept()
        print(f'Client connected: {address}')
        clientSocket.settimeout(3)
        request = clientSocket.recv(5000).decode().split(' ')

    except timeout:
        clientSocket.close()
        continue

    except KeyboardInterrupt:
        print('\r\nServer closed...\r\n')
        serverSocket.close()
        break

    try:
        httpVerb = request[0]
        requestedfileName = request[1][1:]
        print(f'Request from localhost: {httpVerb} /{requestedfileName} HTTP/1.1')

    except IndexError:
        clientSocket.send('HTTP/1.1 400 Bad Request\r\n\r\n'.encode())
        clientSocket.close()

    def createNewFileName(newFileName):
        newFileName = newFileName.split('.')
        fileExtension = newFileName[1]
        newFileName = newFileName[0]
        return f'{newFileName}-{random.randint(0, 5000)}.{fileExtension}'

    def getFile(fileName):
        with open(fileName, 'r') as file:
            return file.read()

    def writeFile(newClientFile, fileContents):
        with open(newClientFile, 'w') as file:
            return file.write(fileContents)

    if httpVerb == 'GET':
        if isfile(requestedfileName):
            try:
                clientSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
                clientSocket.send(getFile(requestedfileName).encode())
                print(f'File sent to the client: {requestedfileName}\r\n')
                clientSocket.close()

            except Exception as e:
                print(f'Error: {e}')
                clientSocket.send('HTTP/1.1 500 Internal Server Error\r\n\r\n'.encode())
                clientSocket.close()

        else:
            try:
                clientSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
                clientSocket.send(getFile('index.html').encode())
                print(f'File sent to the client: index.html\r\n')
                clientSocket.close()

            except Exception as e:
                print(f'Error: {e}')
                clientSocket.send('HTTP/1.1 500 Internal Server Error\r\n\r\n'.encode())
                clientSocket.close()

    elif httpVerb == 'PUT':
        try:
            clientSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
            writeFile(createNewFileName(requestedfileName),
                      clientSocket.recv(5000).decode())
            print(f'File saved: {createNewFileName(requestedfileName)}\r\n')
            clientSocket.close()

        except Exception as e:
            print(f'Error: {e}')
            clientSocket.send('HTTP/1.1 500 Internal Server Error\r\n\r\n'.encode())
            clientSocket.close()

    else:
        clientSocket.send('HTTP/1.1 400 Bad Request\r\n\r\n'.encode())
        clientSocket.close()