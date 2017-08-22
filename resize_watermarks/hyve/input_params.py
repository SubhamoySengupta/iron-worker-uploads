import sys, json

def get_data_from_payload(code):
	#return trim_payload('//hyve-users/12345/photos/__w-160-240-360-480-720-1080__/1.png')
	payload_file = None
	payload = None
	for i in range(len(code)):
	    if code[i] == "-payload" and (i + 1) < len(code):
	        payload_file = code[i + 1]
	        with open(payload_file,'r') as f:
	            payload = json.loads(f.read())
	            return trim_payload(payload)
	        break

def get_credentials():
	cred_file = open('credentials.txt', 'r')
	response = {}
	try: 
		for line in cred_file.readlines():
			strings = line.split('=')
			if len(strings) == 2:
				response[strings[0].strip()] = strings[1].strip()

		if len(response) == 0:
			return False
		else:
			return response
	except:
		return None

def trim_payload(payload):
	link = payload['url']
	if '__w-' in link:
		sys.exit(0)
	link = link[2:] #remove // from front
	bucket = link.split('/')[0]
	
	output_bucket = bucket[:bucket.find('-')] + '-' + link.split('/')[1]
	slug = link.split('/')[2]
	Type = link.split('/')[3]
	image_name = link.split('/')[4]
	
	response = dict(	
						bucket = bucket, 
						output_bucket = output_bucket,
						slug = slug,
						image_name = image_name,
						progressive = True,
						compression = 80,
						type = Type
					)
		
	#extra options
	if 'progressive' in payload and type(payload['progressive']) is str:
		response['progressive'] = eval_bool(payload['progressive'])
	if 'compression' in payload and type(payload['compression']) is int:
		response['compression'] = payload['compression']
	if 'type' in payload:
		response['type'] = payload['type']
	return response 

def eval_bool(value):
	if value == 'True':
		return True
	else:
		return False
