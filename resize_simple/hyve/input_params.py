import sys, json

def get_data_from_payload(code):
	#return trim_payload(dict(url='//hyve-users/48926244749714594/looks/__w-200-400__/-4jpU2Hw0znbssf5OR-Nsflnp-SBYKJv-462815299182993961.jpg'))
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
	if '__w-' not in link:
		sys.exit(0)
	link = link[2:] #remove // from front
	bucket, link = link.split('/')[0], link[link.find('/'):]
	bucket_keys, image_link = link[:link.find('__')], link[link.find('__'):]
	image_name, image_link = image_link[image_link.find('__/'):], image_link[:image_link.find('__/')]
	image_name, image_link = image_name[3:], image_link[2:] 
	image_dimension, image_sizes = image_link[:1], image_link[2:].split('-')
	response = dict(	
						bucket = bucket, 
						keys = bucket_keys, 
						image_name = image_name, 
						image_dimension = image_dimension, 
						image_sizes = image_sizes,
						progressive = True,
						compression = 95
					)
	#extra options
	if 'progressive' in payload and type(payload['progressive']) is str:
		response['progressive'] = eval_bool(payload['progressive'])
	if 'compression' in payload and type(payload['compression']) is int:
		response['compression'] = payload['compression']
	return response

def eval_bool(value):
	if value == 'True':
		return True
	else:
		return False
