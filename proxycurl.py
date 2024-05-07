import requests

api_key = 'IG2NJ8UN31etU6ocTAOC0Q'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/resolve'
params = {
    'company_domain': 'accenture.com',
    'company_name': 'Accenture',
    'company_location': 'sg',
    'enrich_profile': 'enrich',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)
print(response.json())