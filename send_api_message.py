def send(message):
	import json
	import os
	import requests
	payload={"body": message}
	data_json=json.dumps(payload)
	headers={'Content-Type': 'application/json', 'Accept':'application/json', 'Accept-Encoding':'gzip, deflate','Connection':'keep-alive','Content-Length':'23','Host':'hackcave.ryver.com','User-Agent':'HTTPie/0.9.2'}
	url=os.environ['NOTIFICATION_URL']
	response = requests.post(url, data=data_json, headers=headers)
	#print response.status_code 
	

