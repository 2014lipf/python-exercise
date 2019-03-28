#!/usr/bin/python
#author:lamyoung

import subprocess
import shutil

import os
import xml.etree.ElementTree as ET

p = subprocess.Popen("svn st --xml", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
# print "output", output
excludes = ['/library/','/temp/','/local/','/build/']  
fileTempName= "last_svn_st.xml"
fileTemp = open(fileTempName,'w')
fileTemp.write(output)
fileTemp.close()
tree = ET.parse(fileTempName)
root = tree.getroot()

def svnOp(path,item):
    for ex in excludes:
        if(path.find(ex)>=0):
            print 'ignore '+path
            return
    if(item=='missing'):
        os.system("svn delete "+path)
    elif(item=='unversioned'):
        os.system("svn add "+path)


for target in root:
    for entry in target:
        # print entry.attrib
        entry_attrib = entry.attrib
        file_path = entry_attrib['path']
        for wc_status in entry:
            # print wc_status.attrib 
            wc_status_attrib = wc_status.attrib
            if(wc_status_attrib.has_key('item')):
                svnOp(file_path,wc_status_attrib['item'])


os.system("svn st")
str_sure = raw_input("show diff? (y/n)")
if(str_sure=='y' or str_sure=='Y'):
    os.system("svn diff")

str_sure = raw_input("sure commit? (y/n)")
if(str_sure=='y' or str_sure=='Y'):
    os.system("svn commit -m 'auto commit'")


