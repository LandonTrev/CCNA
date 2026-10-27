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













