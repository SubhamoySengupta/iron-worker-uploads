import boto
from boto.s3.key import Key
import boto.s3.connection
import os


class connect_S3:
	def __init__(self, credentials):
		try:
			self.connection = boto.s3.connect_to_region(
					credentials['region'],
					aws_access_key_id=credentials['aws_access_key_id'],
					aws_secret_access_key=credentials['aws_secret_access_key'],
					is_secure=True,
					calling_format=boto.s3.connection.OrdinaryCallingFormat()
				)
			print 'Connection to AWS S3 is successful'
		except:
			print 'Could not connect to AWS'

	def connect_to_aws_bucket(self, bucket_name):
		try:
			self.bucket = self.connection.get_bucket(bucket_name)
			print 'Connected to bucket', bucket_name
		except:
			print 'Couldnot connect to bucket', bucket_name

	def download_file(self, input_params):
		try:
			key_name = input_params['keys'] + '__' + input_params['image_dimension']
			key_name += '-' + '-'.join(input_params['image_sizes']) + '__/' + input_params['image_name']
			key = self.bucket.get_key(key_name)
			key.get_contents_to_filename(input_params['image_name'])
		except:
			print 'Error occured, could not download file'

	def upload_files(self, input_params):
		try:
			image_name = input_params['image_name']
			for size in input_params['image_sizes']:
				key_name = input_params['keys'] + '/'
				# if int(size) < 301:
				# 	key_name += '__' + input_params['image_dimension'] + '__/' + image_name
				# else:
				key_name += input_params['image_dimension'] + size + '/' + image_name
				key = self.bucket.new_key(key_name)
				if image_name.split('.')[1] == 'jpg' or image_name.split('.')[1] == 'JPG' or image_name.split('.')[1] == 'jpeg':
					key.set_metadata("Content-Type", 'image/jpeg')
				elif image_name.split('.')[1] == 'png' or image_name.split('.')[1] == 'PNG':
					key.set_metadata("Content-Type", 'image/png')
				key.set_contents_from_filename(size+'-'+image_name)
				key.set_acl('public-read')
				os.remove(size+'-'+image_name)
			os.remove(image_name)
		except:
			print 'An error occured, could not upload file(s) to S3'
