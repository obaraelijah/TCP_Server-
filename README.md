
#  TCP Server for N Clients

This code implements a TCP server that can accept and hold a maximum of N clients (where N is configurable). Clients are assigned ranks based on first-come-first-serve, with rank 0 being the highest rank. Clients can send commands to the server that the server distributes among the clients. Only a client with a lower rank can execute a command of a higher rank client, while higher rank clients cannot execute commands by lower rank clients, resulting in these commands being rejected. If a client disconnects, the server re-adjusts the ranks and promotes any client that needs to be promoted to avoid any gaps in the ranks.

## Getting Started
To run this code, you will need a machine with Python 3 installed.

1. Clone this repository
2. Open a terminal in the directory where you cloned the repository
3. Run the following command to start the server:
`python Tcp.py
`

 You can also modify the code to change the maximum number of clients N that the server can accept, as well as the IP address and port number to bind the server to.

## Code Description
The code uses the socket module in Python to create a TCP server. A threading module is used to handle multiple clients concurrently. Each client is handled in its own thread, allowing the server to handle multiple clients at the same time. The code also uses a lock to ensure that only one thread can modify the shared data structures at a time.

The code listens for incoming connections and accepts them. If the number of clients has not reached the limit N, the server accepts the connection, assigns a rank to the client, and adds the connection to the list of clients. If the number of clients has reached the limit, the server rejects the connection.

For each client, the code listens for messages and handles two types of commands:

The EXEC command, where a client can request another client to execute a command.
The ERROR command, which is returned if the client sends an unknown command.
If a client disconnects, the code removes the client's connection and rank and adjusts the ranks of the remaining clients to avoid any gaps. The connection is then closed.


## Documentation

[Documentation](https://www.educative.io/answers/how-to-implement-tcp-sockets-in-c)


## Authors

- [Elijah obara samson](https://www.github.com/obaraelijah)


