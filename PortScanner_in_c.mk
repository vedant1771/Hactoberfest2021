Creating a PortScanner in C
Picture a bay where lots of private boats are docked. The location is called a seaport, literally a port at or on the sea. Everyone wanting to dock there, requesting landing services uses the same port. Seaports work with berth numbers assigned to individual boats. The port name and the berth number combine into the “who, what, and where” of boat identification.

The concept of ip address and port is similar. Here the sea_port_name is similar to the IP address while the latter matches with the network_port_no.

Ports are numbered for consistency and programming. The most commonly used and best known ports are those numbered 0 to 1023 dedicated for Internet use, but they can extend far higher for specialized purposes. Each port set or range is assigned specialized jobs or functions, and that’s generally all they do. Usually, all identical system services or functions use the same port numbers on the receiving servers and they remain consistent what-so-ever may be the situation.

When a criminal targets a house for a burglary, typically the first thing he or she checks is if there is an open window or door through which access to the home can be gained. Security technicians often use devices/softwares, known as port-scanners, that enable them to scan all the ports to audit computers for vulnerabilities. Any time there are open ports on one’s personal computer, there is potential for the loss of data, the occurrence of a virus, and at times, even complete system compromise.

Developing a port-scanner is not so difficult as it may seem. The end result of the scanner will be as follows:




INPUT : IPv4 address, Port Range
FUNCTION : Enter an IP address and a port range 
           where the program will then attempt to
           find open ports on the given computer 
           by connecting to each of them. On any 
           successful connection ports, mark the 
           port as open.
OUTPUT : Status of port (open/closed)
The Three step Process for creating a Port Scanner

Step 1: Creating the main()

We create a main() function that takes in the required arguments (server_ip, start_port, end_port). The server IP must be IPv4, though we can extend it to accept IPv6 as well. Try it yourself !!

int main(int argc, char *argv[])
{
    if (argc < 4)
    {
        printf ("Please enter the server IP address"
                " and range of ports to be scanned\n");
        printf ("USAGE: %s IPv4 First_Port Last_Port\n", 
                argv[0]);
        exit(1);
    }
    char tIP[16] = {0};
    strcpy(tIP, argv[1]); // Copy the IPv4 address
    char First_Port[6] = {0};
    strcpy(First_Port, argv[2]); // Copy the start_port
    char Last_Port[6] = {0};
    strcpy(Last_Port, argv[3]); // Copy the end_port

    // Start port-scanner
    port_scanner(tIP, First_Port, Last_Port);
    return 0;
}
Step 2: Creating the port_scanner()

Create a new function, port_scanner(). We traverse through all the ports in range provided and then check against each one of them.
Create a “struct addrinfo hints” and initialize it with proper values.
struct addrinfo hints;
memset(&hints, 0, sizeof(hints));
hints.ai_family = AF_INET;
hints.ai_socktype = SOCK_STREAM;
‘hints’ is an optional pointer to a struct addrinfo, as defined by . This structure can be used to provide hints concerning the type of socket that the caller supports or wishes to use. – from the FreeBSD man page.

Initialize a pointer for the server_address that we will obtain from the server.
Now, call “getaddrinfo(tIP, tport, &hints, &serv_addr)” with proper parameters. The getaddrinfo() function allocates and initializes a linked list of addrinfo structures, one for each network address that matches node and service, subject to any restrictions imposed by hints, and returns a pointer to the start of the list in the 4th paraments, in this case “serv_addr”. The items in the linked list are linked by the ai_next field.
Additional  Info:
There are several reasons why the linked list may have more than one addrinfo structure, including: the network host is multihomed, accessible over multiple protocols (e.g., both AF_INET and AF_INET6); or the same service is available from multiple socket types (one SOCK_STREAM address and another SOCK_DGRAM address, for example).
Normally, the application should try using the addresses in the order in which they are returned.

Step 3: Connecting against the sockets

Traverse through all the addrinfo received in the linked list, and create a socket. The values for the “socket()” are present in the addrinfo struct obtained above. (Each node of the linked_list is traversed using the pointer “temp”.)




sockfd = socket(temp->ai_family, temp->ai_socktype, 
                temp->ai_protocol);
if (sockfd < 0) 
{
     printf("Port %d is NOT open.\n", port);
     continue; 
}
If the socket creation fails, then try using the values in other nodes. Once socket creation succeeds, try connecting to it using the “connect()”. If the connection is a success, then congratulations, the socket is OPEN, else try with the other addrinfo nodes. If none of them works from the linked_list, then the socket is CLOSED. Here is the code for the same,

status = connect(sockfd, temp->ai_addr, 
                 temp->ai_addrlen);
if (status<0) 
{
    printf("Port %d is NOT open.\n", port);
    close(sockfd);
    continue;
}

printf("Port %d is open.\n", port);
close(sockfd);
The “freeaddrinfo()” function frees the memory that was allocated for the dynamically allocated linked list “serv_addr”. It is a good practice to use this instead of “free()”.

The full source code for this tutorial can be downloaded from here.

Note: The code for this program is not long, but how the addresses are derived using getaddrinfo is very important. Almost all networking applications in c have similar first 2 steps. The 3rd step depends on the purpose of the application.

For more info regarding the struct returned by freeaddrinfo, read this documentation and details of the arguments of socket, go through this documentation.
