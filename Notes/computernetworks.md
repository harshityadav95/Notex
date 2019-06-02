# Computer Networks 
#### [<--Back to Home](../Readme.md)

##### IPv4 
* Unicasting , Multicasting , Research
* Ethernet Address or Mac Address is 48 Bit

### Claas A

* 0.0.0.0 is DHCP address
* 127.0.0 is Loop Back Address 
* 0XXXXXXX.--------.--------.--------
* 2^7 avialable bits - 2 Bits since DHCP and loopback address
* 2^24  avaialable for the host bits 

### Class B

* 10XXXXXX.XXXXXXXX.--------.--------
* 2^14 Bits for Network ID
* 2^16 -2 Hosts // for DBA and Network ID

### Class C

* 110XXXXX.XXXXXXXX.XXXXXXXX.--------
* 2^21 Network Id are avaialble  
* 2^8-2 host id available  

### Class D - Used for Multicasting

* 1110XXXX.XXXXXXXX.XXXXXXXX.XXXXXXXX

### Class E - Used for Research

* 11110000.XXXXXXXX.XXXXXXXX.XXXXXXXX

* Add 255 in the End its the Direct Broadcast address 
* For Network ID host Bits are Zero

### Notes
* IP Address + Subnet Mask ID = Network ID  
* Direct Broadcast Address can be used in the destination only for scope in Local Area, all the Host Bits will be 1
* Subnetting Borrowing the Bits from the Host ID  
* Supernetting the Bits are borrowed from the network bits in the Power of 2 Only







