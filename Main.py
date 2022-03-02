from pyclbr import Function
from re import A
from typing import List
import requests
import os
import webbrowser

'''
Payload : When running download math documentation and euler photos and puts them on desktop
'''



class VirusCore():
    def multiply_in_dms(self):
        print("multiplying")
        pass

    def copy_in_startup(self):
        pass

    
class AlgebraDownloader(VirusCore):
    def __init__(self,clone_number: int,message: str,request_list: List[str]):
        self.requests = request_list
        self.clone_number = clone_number
        
    def download(self):
        for req in self.requests:
            r = requests.get(req)
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            for i in range(self.clone_number):
                path = os.path.join(desktop,f'culegeretest{i}.pdf')
                with open(path , 'wb') as f:
                    f.write(r.content)
        return self




def main():
    algebra_downloader = AlgebraDownloader(5,"",["http://www.upt.ro//img/files/2021-2022/Admitere/Licenta/Culegere_admitere_UPT_2022.pdf"])
    algebra_downloader.download()





if __name__ == '__main__':
    main()
    