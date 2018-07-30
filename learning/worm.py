import json
from common.Log import MyLog as Log
import requests
import os

pro_dir = os.path.split (os.path.realpath (__file__))[0]
img_dir = os.path.join (pro_dir, 'images')
if not os.path.exists (img_dir):
    os.mkdir (img_dir)

class GetImg ():
    def __init__(self):
        global log,logger
        log = Log.get_log()
        logger=log.get_logger()

    def get_page_url(self):
        request_url = 'https://bbs.youxiake.com/api/album/detail'
        params = {'albumId':'3142038'}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
        img_list = []
        response = requests.get (request_url,headers=headers,params=params)
        img_url = response.text
        json_img = json.loads (img_url)
        for v in json_img['data']['pics']:
            img_list.append (v['url'])
        return img_list

    def down_img(self):
        url_list = self.get_page_url()
        logger.info("test start")
        for url in url_list:
            for u in url.split('/'):
                if u.find('?') != -1:
                    image_name = u.split('?')[0]
                    path = os.path.join(img_dir,image_name)
            try:
                if not os.path.exists(path):
                    r = requests.get(url)
                    r.raise_for_status()
                    with open(path,'wb') as fb:
                        fb.write(r.content)
                    print("download successfully")
                else:
                    print("file exists")
            except Exception as ex:
                print(str(ex))
            finally:
                logger.info ("test end")


if __name__ == "__main__":
    getImg = GetImg()
    getImg.down_img()
