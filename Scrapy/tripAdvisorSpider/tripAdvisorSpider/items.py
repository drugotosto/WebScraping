# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class Attraction(Item):
    titolo=Field()
    luogo=Field()
    indirizzo=Field()
    numReview=Field()
    urlPagina=Field()
    tipoAttr=Field()
    sottoTipoAttr=Field()
    #booleano
    certificatoEcc=Field()
    #booleano
    certificatoPop=Field
    #definita come dizionario
    rating=Field()
    #definita come lista
    listaAttrVicine=Field()

