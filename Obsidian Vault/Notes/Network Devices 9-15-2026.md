
# **What is a network?**

```
A computer network is a digital telecommunications network which allows nodes to share resources.
```

![[Examples of Nodes.png]]
# Common Examples of Nodes

- **Router**
- **Switch**
- **Firewall**
- **Endpoints/End hosts**
	- **Server**: A server is a device that provides functions or services for clients.
	- **Client**: A client is a device that accesses a service made available by a server.

**Building a Network:** 
![[Simple Network.png|345]]
This example features two nodes (CLIENTS) connected via a cable to communicate with one another and share resources. As simple as this example is, this represents a network.

- In this case lets say PC1 requests an image from PC2. PC1 in this case would be the client while PC2 would be represented as the Server.

**Another Example:**

![[Pasted image 20260915180259.png|501]]
# Switches

Switches are used to forward traffic within a LAN (Local Area Network)

![[Pasted image 20260915181202.png|497]]

Switches can not communicate over the internet without a router or something to route with. They feature MAC addresses which are logged in a MAC Address table by looking at the source MAC address of each frame that arrives and recording which port it came in on. (LAYER 2)

**Some examples of CISCO switches:**
![[Pasted image 20260915181555.png|453]]

# Routers
**How routers aid in routing local traffic from clients and servers connected to a switch over the internet**.
- Routers are used to provide connectivity between LAN's
![[Pasted image 20260915181715.png|452]]
Examples:
CISCO ISR

Although routers can provide basic security measures. What we should really be using is a physical firewall. Firewalls can be placed outside of your router but also can be placed within your network.
It is congruent in the sense that both setups are meant to protect the end hosts connected to the network. Firewalls must be configured with security rules to determine which traffic is allowed or denied. If an attacker try's to access anything in our networks then the firewall should be configured to block this traffic.

# Firewalls

- Some examples of cisco firewalls include the asa5500-x and the firepower 2100
- Firewalls monitor and control network traffic based on configured rules
- These can be placed inside the network or outside of the network depending on the configuration of the enterprise
- Some firewalls are known as Next-Generation Firewalls when they include more modern and advanced filtering capabilities.

**There are different types of firewalls:**

Network Firewalls: 
	Are hardware devices that filter traffic between networks

Host-based Firewalls:
	Software applications that filter traffic entering and exiting a host machine, like a desktop or PC. Almost all PC's have a standard software firewall even those in networks with network firewalls.

# Quiz:
![[Pasted image 20260915185435.png]]
The network device appropriate here would be a networking switch which allows endpoints and end hosts to communicate locally by forwarding traffic over a LAN. These End Points/Clients/Servers would plug into a **networking switch** but with the amount of 30 PC's you may need two 24 port switches or a larger 48 port switch. A router wouldn't be used here because routers connect separate networks rather than end hosts within a LAN

![[Pasted image 20260915191252.png]]
In this situation the friends phone that sent the message to my personal phone using airdrop would represent a server. Lets first recall what a server is; a server is a device that provides services or functions for clients. Our device, the one receiving the image is the client. A client by definition is a device that accesses services hosted by a server. 

**Example in my ESXI Home Lab:** 
The domain controller in VLAN 10 would be defined as a server as it offers many services to its clients such as dhcp, dns, and domain services like active directory. The clients on vlan20 or client01 would be a client of the DC01.

![[Pasted image 20260915192426.png]]
My computer is acting as a client while YouTube is acting as the server. My computer is receiving a service from YouTube servers therefore it is functioning as a client. 

![[Pasted image 20260915192726.png]]

A router would be the appropriate device. Switches are used to connect hosts within the same LAN, but routers are what connect two separate networks together such as two department LANS located in different locations or something like the company network and the internet.