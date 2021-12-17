# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse
import urllib.error
import urllib
import os
import re

class console:
  __loop = 0
  __loopChart = ['/', '—', '\\', '|']

  @staticmethod
  def clear():
    os.system('cls')

  @staticmethod
  def log(msg):
    print(msg)

  @staticmethod
  def loading(txt, index, length):
    console.clear()
    if (console.__loop + 1 > 3):
      console.__loop = 0
    else:
      console.__loop += 1
    print('[Downloading... '+ str(index+1) +'/'+ str(length) +'] ' + console.__loopChart[console.__loop] + ' ' + txt)

class soup:
  __header = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'

  @staticmethod
  def createFolder(path):
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # '/ \ : * ? " < > |'
    rstr = r"[\:\*\?\"\<\>\|]"
    # 替换为下划线
    new_path = re.sub(rstr, "_", path)
    is_exists = os.path.exists(new_path)
    # 不存在则创建
    if not is_exists:
      os.makedirs(new_path)
    else:
      console.log(new_path + ' already exist')
  
  @staticmethod
  def downloadImage(imgurl, path, refer):
    opener = urllib.request.build_opener()
    opener.addheaders = [
      ('User-agent', soup.__header),
      ('Referer', refer)
    ]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(imgurl, path)

  @staticmethod
  def getSuffix(url):
    m = re.search(r'\.[^\.]*$', url)
    if m.group(0) and len(m.group(0)) <= 5:
      return m.group(0)
    else:
      return '.jpeg'

  @staticmethod
  def getFileName(url):
    name = url.split('/')[-1]
    return name

  @staticmethod
  def getReferrer(url, refer):
    if refer:
      return refer
    else:
      par = urllib.parse.urlparse(url)
      if par.scheme:
        return par.scheme + '://' + par.netloc
      else:
        return par.netloc