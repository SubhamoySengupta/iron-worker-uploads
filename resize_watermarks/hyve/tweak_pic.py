from __future__ import division
from PIL import Image
from PIL.Image import alpha_composite


Image.MAX_IMAGE_PIXELS = 262144000  # ~250MB earlier was ~85 MB


class image_resizer:
    def __init__(self, file_name):
        self.IMAGE = Image.open(file_name)
        self.IMAGE_NAME = file_name
        self.WIDTH, self.HEIGHT = self.IMAGE.size
        self.Extension = file_name.split('.')[1]
        self.ASPECT_RATIO = self.WIDTH / self.HEIGHT

    def get_dimensions(self, input_params):
        if input_params['type'] == 'photos':
            if self.WIDTH > 1500:
                self.DIMENSION = '__w-200-400-600-800-1000-1200-1400__'
            elif self.WIDTH > 1300:
                self.DIMENSION = '__w-200-400-600-800-1000-1200__'
            elif self.WIDTH > 1100:
                self.DIMENSION = '__w-200-400-600-800-1000__'
            elif self.WIDTH > 900:
                self.DIMENSION = '__w-200-400-600-800__'
            elif self.WIDTH > 700:
                self.DIMENSION = '__w-200-400-600__'
            elif self.WIDTH > 500:
                self.DIMENSION = '__w-200-400__'
            elif self.WIDTH > 300:
                self.DIMENSION = '__w-200__'
            else:
                self.DIMENSION = '__w__'
        else:
            if self.WIDTH > 1500:
                self.DIMENSION = '__w-200-800-1000-1200-1400__'
            elif self.WIDTH > 1300:
                self.DIMENSION = '__w-200-800-1000-1200__'
            elif self.WIDTH > 1100:
                self.DIMENSION = '__w-200-800-1000__'
            elif self.WIDTH > 900:
                self.DIMENSION = '__w-200-800__'
            elif self.WIDTH > 300:
                self.DIMENSION = '__w-200__'
            else:
                self.DIMENSION = '__w__'

        input_params['image_dimension'] = 'w'
        if self.DIMENSION == '__w__':
            input_params['image_sizes'] = []
        else:
            input_params['image_sizes'] = self.DIMENSION.replace('__', '')[2:].split('-')
        input_params['link_code'] = self.DIMENSION

    def resize(self, input_params):
        try:
            input_params['image_sizes'].append(self.WIDTH)
            for size in input_params['image_sizes']:
                dummy_image = self.IMAGE
                if size == self.WIDTH:
                    if size >= 1600:
                        resized_image = dummy_image.resize(self.get_size('1600', input_params['image_dimension']), Image.LANCZOS)
                    else:
                        resized_image = dummy_image
                else:
                    resized_image = dummy_image.resize(self.get_size(size, input_params['image_dimension']), Image.LANCZOS)
                if resized_image.mode != 'RGBA' and resized_image.format != 'PNG':
                        resized_image = resized_image.convert('RGBA')
                if resized_image.size[0] >= 1600 and resized_image.format != 'PNG':
                    mark = Image.open("watermarks/hyve_watermark_1600.png")
                    if input_params['type'] == 'photos':
                        resized_image = self.addWatermark_center(resized_image, mark)
                    else:
                        resized_image = self.addWatermark_sidelines(resized_image, mark)
                elif resized_image.size[0] >= 1400 and resized_image.size[0] < 1600 and resized_image.format != 'PNG':
                    mark = Image.open("watermarks/hyve_watermark_1400.png")
                    if input_params['type'] == 'photos':
                        resized_image = self.addWatermark_center(resized_image, mark)
                    else:
                        resized_image = self.addWatermark_sidelines(resized_image, mark)
                elif resized_image.size[0] >= 1200 and resized_image.size[0] < 1400 and resized_image.format != 'PNG':
                    mark = Image.open("watermarks/hyve_watermark_1200.png")
                    if input_params['type'] == 'photos':
                        resized_image = self.addWatermark_center(resized_image, mark)
                    else:
                        resized_image = self.addWatermark_sidelines(resized_image, mark)
                elif resized_image.size[0] >= 1000 and resized_image.size[0] < 1200 and resized_image.format != 'PNG':
                    mark = Image.open("watermarks/hyve_watermark_1000.png")
                    if input_params['type'] == 'photos':
                        resized_image = self.addWatermark_center(resized_image, mark)
                    else:
                        resized_image = self.addWatermark_sidelines(resized_image, mark)
                elif resized_image.size[0] >= 800 and resized_image.size[0] < 1000 and resized_image.format != 'PNG':
                    mark = Image.open("watermarks/hyve_watermark_800.png")
                    if input_params['type'] == 'photos':
                        resized_image = self.addWatermark_center(resized_image, mark)
                    else:
                        resized_image = self.addWatermark_sidelines(resized_image, mark)
                elif resized_image.size[0] >= 600 and resized_image.size[0] < 800 and resized_image.format != 'PNG':
                    mark = Image.open("watermarks/hyve_watermark_600.png")
                    if input_params['type'] == 'photos':
                        resized_image = self.addWatermark_center(resized_image, mark)
                    else:
                        resized_image = self.addWatermark_sidelines(resized_image, mark)
                elif resized_image.size[0] >= 400 and resized_image.size[0] < 600 and resized_image.format != 'PNG':
                    mark = Image.open("watermarks/hyve_watermark_400.png")
                    if input_params['type'] == 'photos':
                        resized_image = self.addWatermark_center(resized_image, mark)
                    else:
                        resized_image = self.addWatermark_sidelines(resized_image, mark)
                if size == self.WIDTH:
                    if self.Extension is 'jpg' or self.Extension is 'JPG':
                        resized_image.save(
                                            self.IMAGE_NAME,
                                            'jpeg',
                                            optimize=True,
                                            progressive=input_params['progressive'],
                                            quality=input_params['compression']
                                          )
                    else:
                        resized_image.save(
                                            self.IMAGE_NAME,
                                            optimize=True,
                                        )
                else:
                    if self.Extension is 'jpg' or self.Extension is 'JPG':
                        resized_image.save(
                                            size + '-' + self.IMAGE_NAME,
                                            'jpeg',
                                            optimize=True,
                                            progressive=input_params['progressive'],
                                            quality=input_params['compression']
                                          )
                    else:
                        resized_image.save(
                                            size + '-' + self.IMAGE_NAME,
                                            optimize=True,
                                          )

        except:
            print 'An error occured while resizing'

    def get_size(self, size, dimension):
        if dimension == 'h':
            return int(int(size) * self.ASPECT_RATIO), int(size)
        elif dimension == 'w':
            return int(size), int(int(size) / self.ASPECT_RATIO)

    def addWatermark_center(self, resizedIm, mark):
        layer = Image.new('RGBA', resizedIm.size, (0, 0, 0, 0))
        position = (int(resizedIm.size[0] / 2 - mark.size[0] / 2), int(resizedIm.size[1] / 2 - mark.size[1] / 2))
        layer.paste(mark, position)
        return alpha_composite(resizedIm, layer)

    def addWatermark_sidelines(self, resizedIm, mark):
        layer = Image.new('RGBA', resizedIm.size, (0, 0, 0, 0))
        mark = mark.rotate(270)
        position = (int(resizedIm.size[0] - mark.size[0]), int(resizedIm.size[1] - mark.size[1]))
        layer.paste(mark, position)
        mark = mark.rotate(180)
        position = (0, 0)
        layer.paste(mark, position)
        mark = mark.rotate(-90)
        position = (int(resizedIm.size[0] / 2 - mark.size[0] / 2), int(resizedIm.size[1] / 2 - mark.size[1] / 2))
        layer.paste(mark, position)
        return alpha_composite(resizedIm, layer)
