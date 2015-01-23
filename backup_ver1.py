#coding:utf-8
#!/usr/bin/python
#Filename: backup_ver2.py
#
#import os
#import time
#
#source = ['/home/sq/git/learn.py', '/home/sq/git/testpy.py']
#
#target_dir = '/home/sq/下载/test/'
#
#today = target_dir + time.strftime('%Y%m%d')
#
#now = time.strftime('%H%M%S')
#
#if not os.path.exists(today):
#    os.mkdir(today)
#    print 'Sucessfully created dictionary',today
#
#target = today + os.sep + now +'.zip'
#
#zip_command = "zip -qr '%s' %s"% (target,' '.join(source))
#
#if os.system(zip_command)==0:
#    print 'Successfully backup to',target
#else:
#    print 'failed'


import os 
import time

source = ['/home/sq/git/learn.py', '/home/sq/git/testpy.py']

target_dir = '/home/sq/下载/test/'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment-->')

if len(comment) == 0:
    target = today +os.sep +now +'.zip'
else:
    target = today +os.sep +now + '_' +comment.replace(' ','_')+'.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully create dirctory'

zip_command = "zip -qr '%s' %s"% (target,' '.join(source))

if os.system(zip_command)==0:
    print 'Successfully backup to',target
else:
    print 'failed'
