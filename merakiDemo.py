
from meraki_sdk.meraki_sdk_client import MerakiSdkClient


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
meraki_apikey = input("Enter your API key:")#'15da0c6ffff295f16267f88f98694cf29a86ed87'  ##this is the demo key from Meraki
client = MerakiSdkClient(meraki_apikey)

orgsRtn = getOrgs()
getDeviceStatus(orgsRtn)
