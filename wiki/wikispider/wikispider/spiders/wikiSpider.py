# -*- coding: utf-8 -*-
import scrapy
import os
import json

from wikispider.items import WikispiderItem


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
        infoPagina= BuscadorwikiItem()
        infoPagina['url']=response.url
        infoPagina['ranking']=1
        infoPagina['palabras']=""
        infoPagina['enlaces']=response.css('a[href^="http"] ').xpath('@href').extract()        
        infoPagina['ruta']=nombre_archivo
        for url in infoPagina['enlaces']:
            if self.cont<30: 
                self.cont=self.cont+1
                print ('Procesando pagina numero '+str(self.cont))
                yield scrapy.Request(url=url,callback=self.parse)
                
        yield infoPagina
        pass
        
