from mongoDB import MongoDB
from utils import Utils
from bson.json_util import dumps
import json

class SearchService(MongoDB,Utils):
    def __init__(self):
        self._mongo = MongoDB()
        self._utils = Utils()

    def getProductsByCode(self, iCode):
        try:
            lProducts = self._mongo.getProducts()
            return self.search_by_code(lProducts, iCode)
        except Exception as error:
             raise error
    
    def getProductsByDescr(self, sDescr):
        try:
            lProducts = self._mongo.getProducts()
            return self.search_by_description(lProducts, sDescr)
        except Exception as error:
             raise error
    """
    Method search by description or brand
    Apply discount to all products if description or brand are palindromes
    in: bson lProducts, str description
    out: bson, Collection
    """
    def search_by_description(self, lProducts, sDescription):
        qSearch = ".*{}.*".format(sDescription)
        productos =  lProducts.find({"$or":[ 
                                            {"brand":{"$regex" : qSearch}}, 
                                            {"description":{"$regex" : qSearch}}
                                        ]})
        lista = []
        if productos is not None:
            for row in productos:
                self.initialize_row(row)
                if self._utils.isPalindrom(sDescription) is True:
                    row = self.apply_discount(self.decode_bson(row), 0.5)
                del row['_id']
                lista.append(row)
        
        return lista
    
    def initialize_row(self, row):
        try:
            row['newprice'] = row['price']
            row['discount'] = 0
            row['image'] = self._utils.setUrlImage(row['image'])
        except Exception as error:
            raise Exception("problem initialize row, {}" , error)

    """
    Method search by code 
    Apply discount to all products if code is palindrome
    in: bson lProducts, int Code
    out: bson, row modified
    """
    def search_by_code(self, lProducts, iCode):
        lista = []
        row = lProducts.find_one({"id": iCode})
        if row is not None:
            self.initialize_row(row)
            if self._utils.isPalindrom(str(iCode)) is True:
                row = self.apply_discount(self.decode_bson(row), 0.5)
            del row['_id']
            lista.append(row)
        return lista

    """
    Method decode bson to json
    in: bson product
    out: json product
    """    
    def decode_bson(self, row):
        str_json = dumps(row)
        decoded = json.loads(str_json)
        return decoded
    
    """
    Method apply discount
    in: json product , float: discount
    out: product modified
    """
    def apply_discount(self, product, discount):
        product['newprice'] = product['newprice']*discount
        product['discount'] = discount*100
        return product
