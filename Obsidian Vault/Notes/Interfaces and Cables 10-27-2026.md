Front of a Switch. Each port is an interface.

What do the words above it mean: 10/100/1000Base-T Ports Ports are Auto-MDIX

### Interfaces
![298](Pasted%20image%2020261017203322.png)

RJ-45 Ports (RJ = Registered Jack)

#### What is ethernet?
- Ethernet is a collection of network protocols/standards
- For the purpose of this lesson, we will focus on types of cabling as defined by ethernet standards

#### Why do we need network protocols/standards?

- There are industry standards in place such as the size of an ethernet jack and the port on a switch. 
- Logical standards like IP or internet protocol.
#### Bits and Bytes

What is a bit? 
A bit is a value represented by 0 or 1. Its how computers work, and each of these values is something the computer interprets.

What is a byte? 
A byte is 8 bits. 

**Speed is measured in bits pers second, not bytes per second.**
![445](Pasted%20image%2020261017204320.png)


### Ethernet standards
Defined in the IEEE 802.3 standard in 1983
IEEE = Institute of Electrical and Electronics Engineers.

![622](Pasted%20image%2020261017204521.png)


Copper cables are **UTP Cables** (Unshielded, Twisted, Pair)
**Unshielded** means the cables have no metallic shield which can make them vulnerable to electric interference
**Twisted** |  Twist Protects against EMI (Electromagnetic Interference)
**Pair**       |

4 Pairs = 8 Total.

8 pins in the RJ45 port. 

![453](Pasted%20image%2020261017205211.png)


PC's and routers transmit (Tx) data on pins 1 and 2
and receive (Rx) on pins 3 and 6. 
**This allows the two devices to send and receive data with no issues.** 

Switches are the opposite.

Sometimes it is the case where you want to connect a device to something other than a switch. Like a switch to a switch or a router to a router. 

The answer is a different kind of cable. 

**Straight Through Cable**

**Crossover Cable**
There is new a feature called AUTO MDIX. Allows devices to automatically detect which pins their neighbor is transmitting data on and then adjust which pins they use to transmit and receive data.


In faster networking: (1 gigabit per second)1000Base-T 10GBase-T (10 gigabit per second)

We use all 8 pins or all 4 pairs. Each pair bidirectional. Which is part of the reason they can operate at much faster speeds.

### Fiber Optic Connections

100 meters is okay within a LAN but for bigger networks something extra is needed...

Insert an sfp-tranciever (Small Form-Factor Pluggable)

Connect a fiber optic cable. These cables send light over glass fibers. 
Two connectors on each end for transmitting and receiving data

The copper UPT cables use separate wires within the cable to transmit and receive.

Fiber uses separate cables to transmit and receive data.

![422](Pasted%20image%2020261017211358.png)

![Pasted image 20261017211723](Pasted%20image%2020261017211723.png)

- **Multimode fiber:** wider core, many angles (“modes”), LED transmitters. It’s cheaper and reaches farther than UTP, but not as far as single-mode.
- **Single-mode fiber:** narrow core, one angle, laser transmitters. It’s the most expensive option and reaches the farthest.
- **Standards:** 1000BASE-LX (802.3z) runs 550 m on MMF and 5 km on SMF. 10GBASE-SR is MMF to 400 m. 10GBASE-LR is SMF to 10 km. 10GBASE-ER is SMF to 30 km. The 10G standards are all 802.3ae.
### QUIZ


![Pasted image 20261017213449](Pasted%20image%2020261017213449.png)

The problem here is older routers without AUTO MDIX cannot be connected using a UTP cable. Routers send or transmit data on pins 1 and 2 while they receive on 3 and 6. Since both ends would be expecting to transmit and receive on the same pins they would not be able to communicate. So in this sense something called a crossover cable might have to be used to connect each router together.


![Pasted image 20261017213947](Pasted%20image%2020261017213947.png)

Since they are 150 meters apart this completely removes UTP cables from the situation as by ethernet standard 100 meters is the max. Although single mode fiber supports distances over 150 meters if they want to keep costs down multi-node fiber would be appropriate in this case.


![Pasted image 20261017214256](Pasted%20image%2020261017214256.png)

They have to use single mode fiber as multi mode fiber does not support distances of 3 km.

![Pasted image 20261017214727](Pasted%20image%2020261017214727.png)

A. Because of the AUTO-MDIX.
















