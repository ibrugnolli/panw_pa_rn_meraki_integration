
### Prisma Access Egress Public IP Addresses API Key #####
X_PAN_KEY = "_put_your_prisma_access_egress_ip_api_key_here_"

### Meraki dashboard/tenant information ###
meraki_api_key = "__put_you_meraki_api_key_here"
meraki_org_id = "_put_your_meraki_tenant_org_ID_"
network_tag = "Branch01"
pa_subnets = ["192.168.255.0/24","10.10.1.0/24","10.11.1.0/24", "10.12.1.0/24", "10.101.1.0/24", "10.102.1.0/24", "34.160.111.145/32", "100.127.0.0/16"]

### Prisma Access API Information ###
pa_service_account_username = "_your_service_account_username@panserviceaccount.com"
pa_service_account_password = "_your_service_account_password"
pa_tenant_service_group_id = "tsg_id:_your_tenant_service_group_id_"

### Prisma Access API - Remote Networks IKE Gateway Parameters ###
ike_gw_name = "BRANCH01_IKE_GW"
ike_secret = "_put_your_ike_secret_"
remote_branch_fqdn_id = "abc@meraki.net"
prisma_access_fqdn_id = "def@paloaltonetworks.com"

### Prisma Access API - Remote Networks IPSEC Gateway Parameters ###
ipsec_tunnel_name = "BRANCH01_IPSEC_GW"

### Prisma Access API - Remote Networks Gateway Parameters ###
rn_name = "BRANCH01_RN_GW"
rn_subnets = ["192.168.130.0/24"]
#rn_region = "eu-central-1"
#rn_spn_name = "europe-central-avocado"
rn_region = "sa-east-1"
rn_spn_name = "south-america-east-willow"

### Prisma Access Remote Network Service IP address ###
#public_ip_address="130.41.150.196"
#public_ip_address="34.100.8.12"
