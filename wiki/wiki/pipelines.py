# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class BuscadorwikiPipeline(object):
    
    def process_item(self, item, spider):
        a={'ranking':'1','enlaces':item['enlaces'],'ruta':item['ruta'],'palabras':item['palabras']}
        self.conjPages[item['url']]=a
        
           
        
    def open_spider(self, spider):
      # Proceso a ejecutar
      self.file = open('crawlOut.json', 'w')
      self.conjPages={}

    def close_spider(self, spider):
      # Proceso a ejecutar      
      line = json.dumps(self.conjPages)
      self.file.write(line)
      self.file.close()
      
