# -*- coding: utf-8 -*-
import zipfile , os, os.path
import urllib
from xml.etree import ElementTree

# zip 压缩
def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
         
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()
 
# zip 解压
def unzip_file(zipfilename, unziptodir, channel = ''):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')
        
        if name.endswith('/'):
            os.makedirs(os.path.join(unziptodir, name))
        else:            
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if ext_filename.find('qiyi.properties') >= 0:
                print getKey(ext_filename)
            if ext_filename.find('AndroidManifest.xml') >= 0:
                print ext_filename
                getPackage(ext_filename)
            if not os.path.exists(ext_dir) : 
                os.makedirs(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()

# 下载文件
def download_apk(url, dest_file) :
    urllib.urlretrieve(url, dest_file)


# def spider_apk_url(channel) :
#     pass
# 解析包中的key
def getKey(path) :
    fobj = open(path)
    try:
        for line in fobj:
            if line.find('qiyi.export.key') >= 0:
                return line.split('=')[1].strip()
        return ''
    finally:
        fobj.close()

def getPackage(path) :
    root = ElementTree.parse(path)
    node = root.getiterator('manifest')
    print node



if __name__ == '__main__' :
    channel_list = [
        {   
            'name' : 'baidu',
            'url':'http://www.baidu.com',
            'apk_url' : '',
            'key':'12333333'
        },
        {
            'name': '360',
            'url':'http://www.360.com',
            'apk_url' : '',
            'key' : '122221111'
        }
    ]
    unzip_file(r'/data/package/aiqiyishipin_90.apk', r'/data/package/aiqiyi')
    # url = r'http://5.su.bdimg.com/icon/77588.jpg'
    # download_apk(url, '/data/package/1.jpg')
    
    # for channel in channel_list:
    #     print channel['name'] 
























