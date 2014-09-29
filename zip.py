# -*- coding: utf-8 -*-
import zipfile , os, os.path

# fo = open('/data/package/aiqiyishipin_90.apk')

# for line in fo:
# 	print line
# 	if line.find("qiyi.export.key") >= 0 :
# 		print line

# zf = zipfile.ZipFile('/data/package/aiqiyishipin_90.apk', "w", zipfile.zlib.DEFLATED)


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
def unzip_file(zipfilename, unziptodir, channel):
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
	            print ext_filename
            if not os.path.exists(ext_dir) : 
            	os.makedirs(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()

def download_apk(url, dest_dir) :
	pass

def spider_apk_url(channel) :
	pass

if __name__ == '__main__' :
	channel_list = [
		{   
			'name' : 'baidu',
			'url':'http://www.baidu.com',
			'apk_url' : '',
			'key':'12333333'
		}
	]
	# unzip_file(r'/data/package/aiqiyishipin_90.apk', r'/data/package/aiqiyi')
	
	for channel in channel_list:
		print channel['name'] 
























