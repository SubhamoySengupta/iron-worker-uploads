from __future__ import division
from PIL import Image


Image.MAX_IMAGE_PIXELS = 262144000  # ~250MB earlier was ~85 MB


class image_resizer:
	def __init__(self, file_name):
		self.IMAGE = Image.open(file_name)
		self.IMAGE_NAME = file_name
		self.WIDTH, self.HEIGHT = self.IMAGE.size
		self.Extension = file_name.split('.')[1]
		self.ASPECT_RATIO = self.WIDTH / self.HEIGHT

	def resize(self, input_params):
		try:
			for size in input_params['image_sizes']:
				resized_image = self.IMAGE.resize(self.get_size(size, input_params['image_dimension']), Image.LANCZOS)
				if self.Extension is 'jpg' or self.Extension is 'JPG':
					resized_image.save(
										size+'-'+self.IMAGE_NAME,
										optimize=True,
										progressive=input_params['progressive'],
										quality=input_params['compression']
										)
				else:
					resized_image.save(
										size+'-'+self.IMAGE_NAME,
										transparency=0
										)
		except:
			print 'An error occured while resizing'

	def get_size(self, size, dimension):
		if dimension == 'h':
			return int(int(size) * self.ASPECT_RATIO), int(size)
		elif dimension == 'w':
			return int(size), int(int(size) / self.ASPECT_RATIO)
