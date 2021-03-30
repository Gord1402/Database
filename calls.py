import requests, random, datetime 
class Calls(object):
    
    all = 0
    author = "база от Gord1402 "
    
    def __init__(self):
        pass

    def send(self, serv, phone):
        if serv == 1:requests.Post("callerbot.ru/test_call.php", data={"tel":phone})
 
