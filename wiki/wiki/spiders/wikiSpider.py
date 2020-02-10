import scrapy
import os
import json

from wiki.items import WikiItem


class wikiSpider(scrapy.Spider):
    name = 'wikispider'
    start_urls = ['https://es.wikipedia.org/wiki/Big_data']    
    cont=0

    def start_requests(self):
        
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)
            

    def parse(self, response):
        pagina=response.url.split('/')[-1]
        carpeta="pags_html"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        nombre_archivo=carpeta+'/pag_%s.html'%pagina.replace(':',('_'))
        with open (nombre_archivo,'wb')as f:
            f.write(response.body)
            
        self.log('Archivo %s guardado' %nombre_archivo)
        page_info= WikiItem()
        page_info['url']=response.url
        page_info['ranking']=1
        page_info['palabras']=""
        page_info['enlaces']=response.css('a[href^="http"] ').xpath('@href').extract()        
        page_info['ruta']=nombre_archivo
        for url in page_info['enlaces']:
            if self.cont<30: 
                self.cont=self.cont+1
                print ('Procesando pagina numero '+str(self.cont))
                yield scrapy.Request(url=url,callback=self.parse)
                
        yield page_info
        pass
        
