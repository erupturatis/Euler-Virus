from pyclbr import Function
from typing import List
import requests

'''
Payload : When running download math documentation and euler photos and puts them on desktop
Multiply Sistem : Via Discord
'''



class VirusCore():
    def __init__(self,message: str):
        self.message = message
    
    def custom_message(f):
        def wrapper(self,*args,**kwargs):
            print(*args)        # auxiliary message
            f(self)
            print(self.message) # virus message
        return wrapper

    @custom_message
    def multiply_in_dms(self):
        print("multiply_in_dms")

    @custom_message
    def multiply_in_severs(self):
        pass
    
        

    
class AlgebraDownloader(VirusCore):
    def __init__(self,message: str,request_list: List[str]):
        super().__init__(message)
        self.requests = request_list

    def download(self):
        pass

class ChromeTabOpener(VirusCore):
    def __init__(self,message: str,links_list: List[str]):
        super().__init__(message)
        self.links = links_list


def main():
    pass
    //virus = VirusCore("testing virus")
    //virus.multiply_in_dms("mul1","mul2")




if __name__ == '__main__':
    main()
    