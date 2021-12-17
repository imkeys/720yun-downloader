from utils.core import soup
from utils.core import console
from time import sleep, ctime, time
import datetime
import random
 
class Downloader:
  __datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '/'
  __referrer = 'https://www.720yun.com'
  __dir = 'download/'
  __sleep = .1

  def __init__(self):
    return
  
  def start(self):
    soup.createFolder(self.__dir + self.__datetime)
    self.creatImgList()
  
  def download(self, imgurl):
    rand = random.randint(10, 99)
    sleep(self.__sleep + rand * 0.001)
    fileName = soup.getFileName(imgurl)
    path = self.__dir + self.__datetime + str(fileName)
    refer = soup.getReferrer(imgurl, self.__referrer)
    try:
      soup.downloadImage(imgurl, path, refer)
    except BaseException as msg:
      console.log(msg)

  def creatImgList(self):
    imgList = self.initImg()
    startTime = time()
    for index, item in enumerate(imgList):
      console.loading(item, index, len(imgList))
      self.download(item)
    console.clear()
    console.log(str(len(imgList)) + ' pictures downloaded.')
    console.log('Download time: ' + str(round((time() - startTime), 2)) + 's')
  
  def initImg(self):
    basePath = 'https://ssl-panoimg131.720static.com/resource/prod/35a379das02/986jOrkvtv9/41811474/1622995819/imgs/'
    noodles = ['b', 'd', 'f', 'l', 'r', 'u']
    mode = 'l3'
    length = 6
    suffix = '.jpg'
    imgs = []
    for k in noodles:
      for i in range(1, (length + 1)):
        for j in range(1, (length + 1)):
          file = mode + '_' + k + '_' + str(i) + '_' + str(j) + suffix
          folder = k + '/'+ mode +'/' + str(i) + '/'
          imgs.append(basePath + folder + file)
    return imgs

if __name__ == '__main__':
  downloader = Downloader()
  downloader.start()


'''
https://ssl-panoimg131.720static.com/resource/prod/35a379das02/986jOrkvtv9/41811474/1622995819/imgs/b/l3/2/l3_b_2_2.jpg
https://ssl-panoimg131.720static.com/resource/prod/35a379das02/986jOrkvtv9/41811474/1622995819/imgs/d/l1/1/l1_d_1_1.jpg
https://ssl-panoimg131.720static.com/resource/prod/35a379das02/986jOrkvtv9/41811474/1622995819/imgs/d/l1/2/l1_d_2_2.jpg
https://ssl-panoimg131.720static.com/resource/prod/35a379das02/986jOrkvtv9/41811474/1622995819/imgs/d/l1/2/l1_d_2_1.jpg
https://ssl-panoimg131.720static.com/resource/prod/35a379das02/986jOrkvtv9/41811474/1622995819/imgs/l/l1/1/l1_l_1_2.jpg
https://ssl-panoimg131.720static.com/resource/prod/b51if9b2281/91b27wfOybf/46844269/imgs/r/l3/05/l3_r_05_05.jpg
https://ssl-panoimg131.720static.com/resource/prod/b51if9b2281/91b27wfOybf/46844269/imgs/r/l3/05/l3_r_05_03.jpg
'''
