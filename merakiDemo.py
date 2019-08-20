
##https://pypi.org/project/meraki-sdk/#uplink_settings_controller
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

def getUplinkLossLatency(orgs):
	for x in orgs:
		id = x['id']
		result = client.organizations.get_organization_uplinks_loss_and_latency(id)
		print (result)
		#for s in result:
		#	print (s)#("%s,%s" %(s['status'], s['serial']))
	#return null
meraki_apikey = input("Enter your API key:")#'15da0c6ffff295f16267f88f98694cf29a86ed87'  ##this is the demo key from Meraki
if meraki_apikey == '':
		meraki_apikey = '15da0c6ffff295f16267f88f98694cf29a86ed87'
		print ("!!!!No Key Specified!!!! --Using demo key.")
client = MerakiSdkClient(meraki_apikey)

orgsRtn = getOrgs()
getDeviceStatus(orgsRtn)
getUplinkLossLatency(orgsRtn)
