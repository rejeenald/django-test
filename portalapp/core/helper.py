import random

class StaticUIHelper:

    @staticmethod
    def line_split_notes (str):
        count = 1
        wpl = 40
        str = str.strip()
        words = str.split(" ")
        text = ""
        for w in words:
           count += len(w)
           if count >= wpl:
                text += "<br/>"  
                count = 1   
           text += w + " "
           
        return text
    
    @staticmethod   
    def html_img(alt, str_url):
        s = "<img src='" + alt + "' src='" + str_url + "' />"
        return s

    @staticmethod
    def mask_email(s):
        #finding the location of @
        ln = len(s)
        op = s[0] + "*******" + s[ln-1]
        lo = s.find('@')
        la = s.find ('.', lo)
        if la < 0:
            return op
        if lo > 0:
            k = s[0] + "******" + s[lo-1:lo+2] + "****" + s[la-1:]
            return k
        else:
            return op


    @staticmethod
    def your_randint():
        return random.randint(1, 5)
