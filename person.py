#coding : utf-8
#!/usr/bin/python
# Filename: person.py


import cPickle as p 
import sys 
import os
import time

def dumpfile(li):
    f = file('friendbook.data','w')
    p.dump(li,f)
    f.close()

if os.path.isfile('friendbook.data'):
    friendbook = 'friendbook.data'
else:
    li = {'dhg':{'name':'dhg','age':'20','email':'lala'}}
    dumpfile(li)
    friendbook = 'friendbook.data'
    
f = file(friendbook)
friendlist = p.load(f)

def addFriend(name,age,email):
    if name=='':
        print 'failed to add a new friend'
    else:
        friendlist[name] = {'name':name,'age':age,'email':email}
        dumpfile(friendlist)
        print 'succeed to add a new friend.'

def showAll():
    print 'Your friendlist:'
    print 
    for k,v in friendlist.items():
        print 'Name: %s Age: %s Email: %s'%(v['name'],v['age'],v['email'])

def update():
    name = raw_input('enter your friend\'s name that you want to update--> ')
    if name in friendlist:
        name = raw_input('enter your friend\'s name--> ')
        age = raw_input('enter your friend\'s age--> ')
        email = raw_input('enter your friend\' email--> ')
        if name=='':
            print 'failed to update'
        else:
            friendlist[name] = {'name':name,'age':age,'email':email}
            dumpfile(friendlist)
            print 'succeeded to update'
    else:
        print'NOT FOUND'

print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
1:Search your friend's email from friendsbook
2:add your friend to friendsbook
3:del your friend from friendbook
4:show all of your friends
5:update your friend 
6:press num 6 to exit
'''

num = raw_input('enter the number 1~6-->')

if(num=='1'):
    name = raw_input('Enter your friend\'s name--> ')
    if name in friendlist:
        print friendlist[name]
    else:
        print 'No found'
elif (num=='2'):
    name = raw_input('enter your friend\'s name--> ')
    age = raw_input('enter your friend\'s age--> ')
    email = raw_input('enter you friend\'s email--> ')
    addFriend(name,age,email)
elif (num=='3'):
    name = raw_input('enter your friend\'s name--> ')
    if name in friendlist:
        friendlist.pop(name)
        dumpfile(friendlist)
        print friendlist
    else:
        print 'Not found'
elif (num == '4'):
    showAll()
elif (num == '5'):
    update()
elif (num == '6'):
    print 'Good-bye'
else:
    print 'Please enter the right number'
