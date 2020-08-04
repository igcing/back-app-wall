class Utils:
    PREFIX_URL = "http://"
    def isPalindrom(self, word):
        try:
            word = word.replace(" ","").lower()
            bResult = False
            size = len(word)-1
            if size <= 1:
                bResult = True
            else:
                for index in range(0,size-1):
                    if word[index] == word[size-index]:
                        bResult = True
                    else:
                        bResult = False 
                        break
            return bResult
        except:
            print("Error no se pudo determinar si la palabra es palindromo")
    
    def setUrlImage(self, url):
        try:
            if( url.find(self.PREFIX_URL,0,len(url)) == -1):
                return "{}{}".format(self.PREFIX_URL,url)
            else:
                return url
        except Exception as error:
            raise Exception("Problem setting url" , error)
