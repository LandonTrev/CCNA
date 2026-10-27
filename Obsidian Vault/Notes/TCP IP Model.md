### Introduction
There are many different protocols: TCP, IP, UDP, HTTP
In the TCP IP model protocols are grouped into different layers that describe what they do.

<img src="../Images/Pasted%20image%2020261022192526.png" width="149">
### Protocols and Standards

```
Protocol: A set of rules defining how data should be communicated between devises over a network
	The languages that computers use to communicate
```

 Since the early days of computer networking there have been several attempts to define the functions needed for computers to communicate with each other.
	 Often by a specific Vendor (IBM) to be used with their own products
	 When these companies took a proprietary approach, enabling communications between different vendors' products was difficult.

*Common Issue back in the day* due to different protocols being developed to fit the products of one company
![Pasted image 20261022193150](../Images/Pasted%20image%2020261022193150.png)

```
Standard: An agreed upon specification that describes how a protocol or technology should work.
  - Vendor-neutral standards, devices of all types can communicate with each other.
  -A macbook can access a website hosted on a web server running linux
  - A PC running Windows can send an email that can be read on a smartphone running Android
```


### History 

- The US Department of Defense ARPA (Advanced Research Projects Agency) funded ARPANET, which cam online in 1969 to connect mainframes at universities and labs.
- The protocol NCP (Network Control Program) was used originally.

- Vint Cerf and Bob Kahn began developing TCP (Transmission Control Program)
	- Later divided into two protocols still used today:
		- Transmission Control Protocol (TCP)
		- Internet Protocol (IP)


TCP/IP was dominant over other vendor-proprietary solutions at the time because it was published as a set of open standards that any vendor could implement, and it could run over many different types of networks.

### Who defines the standards?

- Most networking standards are developed by independent standards organizations with participation from engineers at many companies.

![287](../Images/Pasted%20image%2020261027171251.png)
**IEEE (Institute Electrical and Electronics Engineers)**
- Develops many of the technologies used on local area networks:
	- Ethernet (802.3)
	- Wi-Fi (802.11)

![209](../Images/Pasted%20image%2020261027171527.png)
**IETF (Internet Engineering Task Force)**
- Open community that defines protocols used on the Internet
	- TCP, IP, UDP, HTTP, DNS, etc.

- Publishes standards in documents called RFCs (Request for Comments).

### Layered Models

Networks do a lot of different jobs when moving data from one computer to another
- Physical transmission signals
- Local delivery on LAN
- Routing traffic between networks
- End to end conversations
- Applications
A model lets us group related jobs into layers
- Each Layer has a specific role
- Each layer uses the services of the layer below and provides services to the layer above

Protocols live (mostly) at one layer.
- Examples later: IP, TCP, HTTP, etc. 
- Together they form a stack of protocols that work as a team (the network stack)

![418](../Images/Pasted%20image%2020261027172331.png)


### Sending a Letter (Analogy)

![700](../Images/Pasted%20image%2020261027172605.png)

- Remember your understanding of frames and packets in this scenario. Frames are the envelope in this case carrying a packet (letter). In this example, this is not the point being made rather it is about the function of each layer in association. There are some similarities between this and sending a letter in the mail.

![](../Images/Pasted%20image%2020261027181202.png)

Each of these layers has its own dedicated job.
- Layers work together to deliver the message, but each one focuses on its own task.

What happens inside one layer doesn't change the job of the other layers
- Changing the content of the letter doesn't change the delivery itself. 
- Changing the delivery path doesn't affect the letter itself.
![524](../Images/Pasted%20image%2020261027182751.png)

### The TCP/IP Model

```
This section will review the layers of the TCP/IP model. 
Note: This is a top down approach.
```

![](../Images/Pasted%20image%2020261027182930.png)

#### **Application Layer**:
PC1 is running a web client application such as chrome. SRV1 is hosting a web and file server. PC1's user wants to access a webpage hosted on server. So Chrome needs to send a request to the web server on SRV1. That's the role of the application layer. 

- Includes protocols for communication between applications processes; create and interpret the data. 

==🟡*Problem:*== There is multiple processes running on SRV1. A web server and file server process. So how can PC1 ensure it's request reaches the correct process on SRV1. This is the role of the transport layer. 

#### **Transport Layer:** 
Each process on SRV1 has an associated transport port number. 80 for the web server and 21 for the file server. A port in this scenario is a number used to identify a process running on a host.

- Provides end-to-end communication between application processes such as the web client application (chrome) and the web server on SRV1 using port numbers.

#### **Internet Layer:**

The internet address of SRV1 is 10.1.1.1. By addressing SRV1's IP address, PC1 tells the routers in the path which host the message should be delivered to. This is the entire point of the internet layer, it provides communication between hosts, from the source host to the destination host, using IP addresses and routers. 

- Provides end-to-end communication between hosts across networks using IP addresses and routers. 

**Think "IP Addresses and Routers"**

A host in this case is just a device connected to the network that can send a receive data.
#### **Local Network Layer:**
There are several devices in between PC1 and SRV1. We need to ensure the message is properly passed along between them. That is the goal of the Local Network Layer. Using protocols at this layer, such as Ethernet, each device sends the message to the next device on the local network.

- Provides hop-to-hop delivery within a local network using MAC addresses and switches.

**Switch:** Connects devices in a LAN and passes messages between them.
#### **Physical Layer:**
All of these cables and the transceivers on the devices that transmit and receive signals.

- Sends bits as electrical, optical, or radio signals over the physical medium.

![](../Images/Pasted%20image%2020261027190209.png)


### Layer 1: The Physical Layer

- Is responsible for sending and receiving bits as electrical, optical, or radio signals over the medium.
- Defines things like cables, connector, signal levels, and link speeds.
	Examples: 
	- Copper UTP Cables, fiber-optic cables, Wi-Fi radios and antennas, network interface cards (NICs).

### Layer 2: The Local Network Layer 
![](../Images/Pasted%20image%2020261027191352.png)
- Provides hop-to-hop delivery of messages on a local network.
	- A hop is one step along the path between two devices:
		- From one router or host, to the next router or host in the path.
	- Switches don't count: a switch just extends the local network, allowing multiple devices to connect.

- Uses MAC (Media Access Control) addresses to identify interfaces.
	- PC1 sends message to the MAC of R1's G1 interface (NIC).
	- R1 sends the message to the MAC of R2's G1 interface (NIC).
	- R2 sends the message to the MAC of SRV1's interface (NIC).

- Protocol's at this layer include: 
	- Ethernet (IEEE 802.3)
	- Wi-Fi (IEEE 802.11)

### Layer 3: The Internet Layer
- Provides end-to-end delivery between hosts across multiple networks.
	- Internet = internetwork (between networks)

- Uses IP addresses to identify hosts in the network.
	- When PC1 sends a message to SRV1, it addresses it to SRV1's IP address.

- Routers operate mainly at this layer, using the message's destination IP address to forward the message toward its final destination host. 

- Protocols at this layer include: 
	- IP (IPv4, IPV6)
	- ICMP (Internet Control Message Protocol)

### Layer 4: The Transport Layer

- Provides end-to-end communication between application processes.

- Uses port numbers to identify the processes on each host.
	- When the web client on PC1 wants to send a request to the web sever running on SRV1, it addresses the message to port 80. 

- Runs mainly on the communicating hosts; routers normally operate based on IP (Layer 3), not on transport layer information.

- Protocols at this layer include:
	- UDP (User Diagram Protocol): simple and efficient
	- TCP (Transmission Control Protocol): More robust features beyond basic message addressing.

### Layer 5: The Application Layer
- Where network communications meet applications. 
	- Usually called layer 7 

- Defines how application processes format, send, and interpret data.

- Protocols at this layer define message formats and rules for specific tasks, such as:
	- Browsing web pages (HTTP/HTTPS)
	- Transferring files (FTP, TFTP)
	- Sending/receiving email (SMTP, POP3, IMAP)

- Network infrastructure devices (routers, switches) dont care about Application-layer details
	- They just move messages across the network
	- Only the communication hosts interpret the data.


### Encapsulation and Decapsulation

**Encapsulation:**

![639](../Images/Pasted%20image%2020261027193728.png)

**Decapsulation:**
![638](../Images/Pasted%20image%2020261027193918.png)


Each device has its own network stack.
![635](../Images/Pasted%20image%2020261027194050.png)


### Protocol Data Units

![636](../Images/Pasted%20image%2020261027194451.png)


### Adjacent-layer interaction

![](../Images/Pasted%20image%2020261027195137.png)

### Same-layer Interaction
![571](../Images/Pasted%20image%2020261027195216.png)

![573](../Images/Pasted%20image%2020261027195340.png)