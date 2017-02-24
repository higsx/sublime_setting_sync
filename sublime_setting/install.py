#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

py3k = sys.version_info.major > 2

def myprint(n):
    print(n)

if py3k:
    print('you python is 3+')
    raw_input = input


def clean(fullPath):
    if os.path.exists(fullPath):
        print('delete file {0}?'.format(fullPath))
        
        result = raw_input("type y or Y to delete,any other key to cancle\n>")
        if result.lower() == 'y':
            print('remove ' + fullPath)
            os.remove(fullPath)


#save the cmd to bat file to debug
batfile = open('mklink_cmd_for_debug.bat','w')
def mklink(link,target):
    if os.path.exists(link):
        print ('mklink ,the link {0} already exist!!'.format(link))
        return False
    else:
        cmd = 'mklink "{link}" "{target}"'.format(link=link,target=target)
        print('exec:' + cmd)
        batfile.write(cmd+"\n")
        os.system(cmd)


sub_path = "\\Sublime Text 3\\Packages\\User\\"
#the destnation direcory to contian the config
appdata_path = os.environ.get("appdata") + sub_path


def get_link_targets(rootdir,absolute_links,absolute_targets):
    for (dirpath, dirnames, filenames) in os.walk(rootdir):  
        for filename in filenames:  
            if filename != __file__:
                absolute_targets.append(os.path.join(dirpath, filename))
                absolute_links.append(os.path.join(appdata_path,filename))


def main():
    absolute_links = []
    absolute_targets = []

    rootdir = os.getcwd()  
    print('the sync source dir is :' + rootdir)  
    get_link_targets(rootdir,absolute_links,absolute_targets)

    print('>'*20)
    print('----do you want remove exists files?~-----------')
    for _file in absolute_links:
        clean(_file)
    print('<'*20)

    print('>'*20)
    print('\n\nbegin mklink ~ \n\n')
    for link in zip(absolute_links,absolute_targets):
        mklink(*link)
    print('<'*20)


if __name__ == '__main__':
    main()
