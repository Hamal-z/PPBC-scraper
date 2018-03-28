# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from PIL import Image
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO


class PpbcPipeline(object):
    def process_item(self, item, spider):
        return item


class PicscrapyPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for x in item.get(self.images_urls_field, []):
            yield Request(x, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        return '/pic/{}/{}.jpg'.format(item['category_name'], item['title'])

    def thumb_path(self, request, thumb_id, response=None, info=None):

        item = request.meta['item']
        return 'thumbs/{}/{}.jpg'.format(item['category_name'], item['title'])

    def item_completed(self, results, item, info):
        return item

    def convert_image(self, image, size=None):
        if image.format == 'PNG' and image.mode == 'RGBA':
            background = Image.new('RGBA', image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert('RGB')
        elif image.mode == 'P':
            image = image.convert("RGBA")
            background = Image.new('RGBA', image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert('RGB')
        elif image.mode != 'RGB':
            image = image.convert('RGB')

        if size:
            image = image.copy()
            image = image.resize(size, Image.ANTIALIAS)

        buf = BytesIO()
        image.save(buf, 'JPEG')
        return image, buf
