"""HTTP Client"""
from socket import *
import random
import sys
from genericpath import isfile

clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    hostName = sys.argv[1]
    port = int(sys.argv[2])
    httpVerb = sys.argv[3]
    fileName = sys.argv[4]
except IndexError:
    print(f'Expected: python3 client.py <host name> <port> <http verb> <file name>')
    sys.exit()

request = f'{httpVerb} /{fileName} HTTP/1.1\r\n\r\n'
print(f'Request: {request.strip()}')

clientSocket.connect((hostName, port))

def createNewFileName(newFileName):
    newFileName = newFileName.split('.')
    fileExtension = newFileName[1]
    newFileName = newFileName[0]
    return f'{newFileName}-{random.randint(0, 5000)}.{fileExtension}'

def getFile(fileName):
    with open(fileName, 'r') as file: return file.read()

def writeFile(newClientFile, fileContents):
    with open(newClientFile, 'w') as file: return file.write(fileContents)

if httpVerb == 'GET':
    try:
        clientSocket.send(request.encode())
        requestHeader = clientSocket.recv(5000).decode().strip()
        print(f'Response: {requestHeader}')

        if requestHeader == 'HTTP/1.1 200 OK':
            fileContents = clientSocket.recv(5000).decode()
            fileName = createNewFileName(fileName)
            writeFile(fileName, fileContents)
            print(f'File received from the server: {fileName}\r\n')
            clientSocket.close()
            sys.exit()

        else:
            print('Bad request\r\n')
            clientSocket.close()
            sys.exit()

    except Exception as e:
        print(e)
        clientSocket.close()
        sys.exit()

elif httpVerb == 'PUT':
    try:
        if isfile(fileName):
            clientSocket.send(request.encode())
            clientSocket.send(getFile(fileName).encode())
            print(f'Response: {clientSocket.recv(5000).decode()}\r\n')
            clientSocket.close()
            sys.exit()

        else:
            print(f'File not found: {fileName}\r\n')
            clientSocket.close()
            sys.exit()

    except Exception as e:
        print(e)
        clientSocket.close()
        sys.exit()

else:
    print('Invalid HTTP verb\r\n')
    clientSocket.close()
    sys.exit()