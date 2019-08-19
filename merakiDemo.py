
from meraki_sdk.meraki_sdk_client import MerakiSdkClient

meraki_apikey = '15da0c6ffff295f16267f88f98694cf29a86ed87'  ##this is the demo key from Meraki
client = MerakiSdkClient(meraki_apikey)

def getOrgs():
	orgs = client.organizations.get_organizations()
	return orgs

def getDeviceStatus(orgs):
	for x in orgs:
		id = x['id']
		result = client.organizations.get_organization_device_statuses(id)
		for s in result:
			print ("%s,%s" %(s['status'], s['serial']))
	#return null

orgsRtn = getOrgs()
getDeviceStatus(orgsRtn)

