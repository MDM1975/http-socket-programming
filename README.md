# Socket Programming in Python

This project showcases an implementation of simple socket programming in Python, creating a client-server model where the client can send HTTP requests to the server and receive the appropriate response.

## Overview

The architecture of this program is primarily composed of two components: a client and a server, both of which are hosted on the same machine and implemented using Python's built-in `socket module`. The server constantly listens on `port 8080` for incoming connections, while the client is responsible for initiating communication with the server.

The client sends HTTP requests to the server, which parses the request, determines the appropriate file to return, and sends it back to the client. Additionally, all communication between the client and server are logged for review and debugging purposes. You can interact with the localhost server through a web browser by entering `localhost:8080` in the address bar or directly from the command line.

## Project Structure

```
http-server/
    |__ server.py
    |__ index.html
    |__ server-code.html
    |__ client-code.html
http-client/
    |__ client.py
    |__ client-text.txt
```

**server.py:** Contains the implementation of the HTTP server. The server listens for connections on localhost and port 8080. It supports GET and PUT methods and can handle file requests and file uploads.

**client.py:** Contains the implementation of the HTTP client. The client can send GET and PUT requests to the server, download the requested files, and upload files to the server.

**index.html:** The home page of the server. If a client requests a file that doesn't exist, the server will return this page as a default response.

**server-code.html:** Displays the server's source code.

**client-code.html:** Displays the client's source code.

## How it works

**Server (server.py):** The server is programmed to listen continuously for incoming connections on `port 8080`. When a request is received, the server parses it to determine the HTTP method `(GET, POST, etc.)`, and the requested file. It then sends the requested file back to the client if available, or a default file in case the requested file isn't found. All requests and responses are recorded in a server-side log file for future reference.

**Client (client.py):** The client initiates communication by sending an HTTP request to the server. The client can specify the HTTP method and the file it wishes to access. Once the server sends back the file, the client displays a confirmation message indicating the successful retrieval of the file.

## How to run

-   Start the server by executing the command `python3 server.py` in the terminal.
-   Run the client with the desired HTTP method and file name using the command `python3 client.py <host name> <port number> <http verb> /<file name>`.
    -   For example, to fetch index.html from the server, you would enter `python3 client.py localhost 8080 GET /index.html`.
-   The server will listen for the client's request, process it, and send the appropriate file back to the client.
-   The client will then display a confirmation message upon successful retrieval of the file, and the server will simultaneously log the request and response in a log file.
