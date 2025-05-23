# panw_pa_rn_meraki_integration
Python codes to automate the creation of the Palo Alto Prisma Accesss remote network integration with Meraki MX devices

## Overview

Prisma Access provides a flexible way to effectively secure Cisco Meraki SD-WAN deployments. By delivering security from the cloud and closer to the branch networks, Prisma Access lets you optimize networking and security with the same protections that you have at corporate headquarters.

![image alt text](images/scr01.png)

As with other SD-WAN deployments, you secure the Cisco Meraki SD-WAN by onboarding a remote network using IPSec tunnels between the Cisco Meraki SD-WAN and Prisma Access. Using Prisma Access, you can secure SD-WAN devices at a branch, at a data center, or both. You can onboard a remote network using IPSec tunnels between the Cisco Meraki SD-WAN device and Prisma Access automatically using this scripts. See the product requirements below for eligible devices that support this automation. 

## Why connecting our Meraki devices to PANW Prisma Access

Integrating a Cisco Meraki MX device with Palo Alto Networks Prisma Access can provide a powerful combination of branch-level connectivity with best in class cloud-delivered security. Here’s why organizations might choose to do this:

A) Enhanced Security 

Meraki MX provide a legacy SD-WAN and very basic security (like stateful firewall, content filtering, and IPS). But Prisma Access offers best in class, enterprise-grade, next-gen security capabilities, such as:

1. Advanced Threat Prevention (ATP)
2. Cloud-based URL filtering with real-time updates
3. Data Loss Prevention (DLP)
4. Zero Trust Network Access (ZTNA)

So, traffic from Meraki MX can be routed to Prisma Access for deep inspection and policy enforcement.


B) Cloud-Native Security for Remote and Branch Users

Meraki MX handles local connectivity and routing, but by integrating it with Prisma Access:

1. Remote branches gain access to a consistent cloud-based security layer
2. You get uniform security policies across distributed sites and mobile users
This centralizes security management and compliance.

C) Scalability and Flexibility
Prisma Access is built for scale — it's hosted in the cloud, so:
1. There's no need to deploy hardware firewalls at every site
2. You can easily onboard new branches using Meraki MX and point them to Prisma Access
3. It supports dynamic scaling as your traffic or user base grows

D) Hybrid and Secure SD-WAN
Meraki MX can still establish SD-WAN tunnels to multiple destinations and include VPN tunnels to no Meraki peers, like Prisma Access. You can configure:

IPSec tunnels from Meraki MX to Prisma Access
Dual/multi-path routing with failover and load balancing
Site-to-site VPN to Prisma Access for secure transport to the cloud

This enables a hybrid WAN architecture that combines performance optimization and security.

E) Centralized Visibility, Management and Automation
Prisma Access GUI offers centralized logging, reporting, and security policy enforcement — complementing the Meraki Dashboard which provides network-level monitoring.
Also, both solutions provide secure API's to automate the deployment and parameters updates.

## Requirements

Palo Alto Prisma Access:
1) Update your Prisma Access to version 2.1 Preferred or a later version.
2) Migrate remote networks to the aggregate bandwidth model.
3) Activate bandwidth license per compute location.

Cisco Meraki
1) Physical Cisco Meraki (MX or Z) devices with a minimum version of 15.12 in Cisco Meraki Hub or Spoke networks.
2) Cisco Meraki devices should be in Appliance or Combined type networks
3) Cisco Meraki networks that have enabled the VPN Mode in the Site-to-Site VPN configurations

## How to Use

1. Clone repository with `git clone https://github.com/ibrugnolli/panw_pa_rn_meraki_integration`
2. Change directory to `panw_pa_rn_meraki_integration`
3. Edit `pa_env.py`
* Update the variable `X_PAN_KEY`, with the Egress Public IP Addresses API Key.
* Example: `X_PAN_KEY = "_your_api_key__"`
  
![image alt text](images/scr05.png)

* Update the variable `meraki_api_key`, with the Meraki Dashboard API key.
* Example: `meraki_api_key = "_your_api_key__"`
  
![image alt text](images/scr02.png)
![image alt text](images/scr03.png)
![image alt text](images/scr04.png)

* Update the variable `meraki_org_id`, with the Meraki Dashboard Organization ID.
* Example: `meraki_org_id = "_your_org_id__"`

![image alt text](images/scr06.png)

* Update the variable `network_tag`, with the Meraki network tag.
* Example: `network_tag = "Branch01"`

* Update the variable `pa_subnets`, with the ipv4 subnets you need to reach in the Prisma Access enviroment.
* Example: `pa_subnets = ["192.168.255.0/24","10.10.1.0/24","10.11.1.0/24"]`


* Update the variable `pa_service_account_username` and `pa_service_account_password` , with the Prisma Access account service information.

![image alt text](images/scr07.png)
![image alt text](images/scr08.png)

* Update the variable `pa_tenant_service_group_id` , with the Prisma Access tenant service group ID information.

![image alt text](images/scr09.png)

* Update informations regarding the IKE parameters, including `ike_gw_name` , `ike_secret`, `remote_branch_fqdn_id`, `prisma_access_fqdn_id`

* Update information regarding the IPSEC parameter `ipsec_tunnel_name`.

* Update informations regarding the Remote Network parameters, including `rn_name` , `rn_subnets`, `rn_region`, `rn_spn_name`

4. Run the script to create the IKE Gateway:
```
python3 pa_create_ikegw.py
```

5. Run the script to create the IPSEC Tunnel:
```
python3 pa_create_ipsec_tunnel.py
```

5. Run the script to create the Remote Network:
```
python3 pa_create_rn.py
```

6. Run the script to push the configuration:
```
python3 pa_push_rn_verify.py
```

7. Run the script retrieve the egrees Public IP Address:
```
python3 pa_egress_ip.py
```

8. Run the script to configure the Meraki MX:
```
python3 meraki_vpn_create_pa.py
```

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/ibrugnolli/panw_pa_rn_meraki_integration)
[![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/codeexchange/devenv/ibrugnolli/panw_pa_rn_meraki_integration/)

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10578/badge)](https://www.bestpractices.dev/projects/10578)

