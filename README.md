# HTTP Client-Server Implementation with Sockets
This project showcases an implementation of a simple HTTP client and server implemented using sockets in Python. The server can handle the client's `HTTP/1.0 GET and PUT` requests. It's a lightweight, pared-down version of `HTTP/1.0`.

## Overview

The program has two main components: an `HTTP client` and an `HTTP server`.

The client, upon execution, sends an HTTP request to the server. The server parses the request, performs the required operation, and sends an appropriate response back to the client. All requests and responses are logged for debugging and review.

The HTTP client and server are designed to run on the same machine. However, they can also run on different machines, provided the IP address and port number are correctly configured.

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

**server.py:** Contains the implementation of the HTTP server. The server listens for connections on localhost and port 8080. It supports GET and PUT methods and can handle file requests and uploads.

**client.py:** Contains the implementation of the HTTP client. The client can send GET and PUT requests to the server, download the requested files and upload files to the server.

**index.html:** The home page of the server. If a client requests a file that doesn't exist, the server will return this page as a default response.

**server-code.html:** Displays the server's source code.

**client-code.html:** Displays the client's source code.

## How it works

**Server**

The server constantly listens for client connections on the specified port. When a client connection is accepted, the server reads the HTTP request and constructs a valid HTTP response, including the status line, headers, and the requested file in the response body (for GET requests) or a status message (for PUT requests).

When terminated, the server closes all open sockets and frees allocated memory, ensuring a graceful shutdown.

**Client**

The client initiates communication by sending an HTTP request to the server. The client is designed to send GET and PUT requests to the server. The command-line arguments dictate the server name or IP address, the server port, the `HTTP method (GET or PUT),` and the path of the requested or uploaded file on the server.

**GET Method**

The GET method fetches the specified file from the server. If the file is found on the server, the server responds with a "200 OK" message, followed by the file content. The server responds with the corresponding error message if the file is not found or the request is invalid.

**PUT Method**

The PUT method uploads a file to the server. Upon receiving a PUT request, the server expects to receive a file and saves it to disk. If the file is successfully received and saved, the server sends the client a "200 OK File Created" response.

## How to run

-   Start the server by executing the command `python3 server.py` in the terminal.
-   Run the client with the desired HTTP method and file name using the command `python3 client.py <host name> <port number> <http verb> /<file name>`.
    - To fetch index.html from the server, you would enter `python3 client.py localhost 8080 GET /index.html`.
-   The server will listen to the client's request, process it, and send the appropriate file back to the client.
-   The client will then display a confirmation message upon successfully retrieving the file, and the server will simultaneously log the request and response in a log file.

## Notes
This project is a basic implementation of HTTP/1.0 using socket programming in Python. It should not be used as a production-grade HTTP server due to its simplicity and lack of many standard features and security measures in modern HTTP servers.