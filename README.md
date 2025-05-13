# panw_pa_rn_meraki_integration
Python code to automate the creation of the Palo Alto Prisma Accesss remote network integration with Meraki MX devices

## Overview

Prisma Access provides a flexible way to effectively secure Cisco Meraki SD-WAN deployments. By delivering security from the cloud and closer to the branch networks, Prisma Access lets you optimize networking and security with the same protections that you have at corporate headquarters.

![image alt text](images/scr01.png)

As with other SD-WAN deployments, you secure the Cisco Meraki SD-WAN by onboarding a remote network using IPSec tunnels between the Cisco Meraki SD-WAN and Prisma Access. Using Prisma Access, you can secure SD-WAN devices at a branch, at a data center, or both. You can onboard a remote network using IPSec tunnels between the Cisco Meraki SD-WAN device and Prisma Access automatically using this scripts. See the product requirements below for eligible devices that support this automation. 

Palo Alto Prisma Access:
1) Update your Prisma Access to version 2.1 Preferred or a later version.
2) Migrate remote networks to the aggregate bandwidth model.
3) Activate bandwidth license per compute location.

Cisco Meraki
1) Physical Cisco Meraki (MX or Z) devices with a minimum version of 15.12 in Cisco Meraki Hub or Spoke networks.
2) Cisco Meraki devices should be in Appliance or Combined type networks
3) Cisco Meraki networks that have enabled the VPN Mode in the Site-to-Site VPN configurations

