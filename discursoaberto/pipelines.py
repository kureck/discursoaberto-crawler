# -*- coding: utf-8 -*-

import datetime
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DiscursoPipeline(object):
    def process_item(self, item, spider):
        item['inserted_at'] = datetime.datetime.utcnow()
        item['created_at'] = datetime.datetime.strptime(
            item['created_at'], "%d/%m/%Y %H:%M")
        return item


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        item['inserted_at'] = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M")
        item['created_at'] = item['created_at'].strftime("%d/%m/%Y %H:%M")
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
