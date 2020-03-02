# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os

class ThreegstudentPipeline(object):
    def process_item(self, item, spider):
        print('1111111')
        # return item['content']
        file_name = item['title'] + '.html'
        file_name = os.path.join(os.path.abspath('.'), 'outputs', file_name)
        file_content = item['content']
        with open(file_name, 'w') as f:
            f.write(file_content)
