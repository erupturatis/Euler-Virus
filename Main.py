from pyclbr import Function
from re import A
from typing import List
import requests
import os

'''
Payload : When running download math documentation and euler photos and puts them on desktop
Multiply Sistem : Via Discord
'''



class VirusCore():
    def __init__(self,message: str):
        self.message = message

    def multiply_in_dms(self):
        print("multiply_in_dms")


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
    
    ht = "http://httpbin.org/get"
    a = "https://www.101books.ru/carte/descarca-adolf-hitler-mein-kampf-lupta-mea-pdf"
    cluj = "https://admitereonline.utcluj.ro/docs/2021/matematica/Siruri_NReal_Baias_Popa.pdf"


    r = requests.get(cluj)
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    path = os.path.join(desktop,'culegeretestare232.pdf')
    with open(path , 'wb') as f:
        f.write(r.content)


    #req = list()
    #req = ["http://www.upt.ro//img/files/2021-2022/Admitere/Licenta/Culegere_admitere_UPT_2022.pdf"]

    #algebra_downloader = AlgebraDownloader("downloaded")





if __name__ == '__main__':
    main()
    