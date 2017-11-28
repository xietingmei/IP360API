#-*- coding: utf-8 -*-
'''
    created by xietingmei 2017-11-16
'''
__version__='0.1'

import string
import urllib2
import urllib
import cookielib
import json
import sys
from basiclib import *
import pysical_devices as device
import api_url as api
import time
import datetime
import random
reload(sys) 
sys.setdefaultencoding('utf8')

class IP360Login(object):

    #----------------------------------------------------------------------------------------IP360WebApi
    def ip360webapi_login(self,**confdict):
        '''
            IP360webapi登录。

            参数:
          
            举例:
            | ip360webapi login |
        '''
        # 配置login信息
        json_content = ''
        url_string = api.ADMIN_API['ip360login'].replace("account1",'''%7b%22account%22%3a%22'''+confdict["account"]+'''%22%2c%22password%22%3a%22''').replace("password1",confdict["password"]+'''%22%2c%22vcode%22%3a%22''').replace("vcode1",confdict['vcode']+'''%22%2c%22type%22%3a%22781234%22%7d''')
        
        # 发送request到IP360WEBAPI
        my_request = IP360Request(url_string,json_content)
        my_response = my_request.request_get()
        res = my_response.text
        print "response",res
        tokenlist = []
        tokenlist = res.split(',')
        strname = "\"token\":"
        templist = []
        accesstoken=''
        for i in range(0,len(tokenlist)):
               if strname in tokenlist[i]:
                   templist=tokenlist[i].split(':')
                   accesstoken1 = templist[1]
                   accesstoken = accesstoken1.strip('\"}')
                   break
        print 'Get the accesstoken',accesstoken
        idlist = []
        idlist = res.split(',')
        strname = "\"id\":"
        templist = []
        ids=''
        for i in range(0,len(idlist)):
               if strname in idlist[i]:
                   templist=idlist[i].split(':')
                   ids1 = templist[1]
                   ids = ids1.strip('\"}')
                   break
        print 'Get the id',ids
        # 解析response返回信息

        if 'token' in str(my_response.text):
            print 'Passed:ip360login successed';
            flag_ret = 1
            return accesstoken,ids,flag_ret
        elif '用户名或密码错误' in str(my_response.text):
            print 'Passed:ip360login password error check successed';
            flag_ret = 1
            return flag_ret
        elif '验证码不正确' in str(my_response.text):
            print 'Passed:ip360login vcode error check successed';
            flag_ret = 1
            return flag_ret
        elif '密码错误次数过多' in str(my_response.text):
            print 'Passed:ip360login password error 3 times check successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:ip360login failed';
            flag_ret = 0
            return flag_ret



    #----------------------------------------------------------------------------------------IP360WebApi
    def ip360webapi_snapshotquzheng(self,token,uid,**confdict):
        '''
            IP360webapi快照取证。

            参数:
          
            举例:
            | ip360webapi snapshotquzheng |
        '''
        # 配置login信息
        json_content = ''
        url_string = api.ADMIN_API['ip360snapshotquzheng'].replace("quzheng",'''%7b%22uid%22%3a'''+uid+'''%2c%22name%22%3a%22''').replace("name1",confdict['name']+'''%22%2c%22url%22%3a%22''').replace("url1",confdict['url']+'''%22%7d&token=''').replace("test",token)
        # 发送request到IP360WEBAPI
        my_request = IP360Request(url_string,json_content)
        my_response = my_request.request_post()
        print my_response

        if '操作成功' in my_response:
            print 'Passed:ip360snapshotquzheng successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:ip360snapshotquzheng failed';
            flag_ret = 0
            return flag_ret


    #----------------------------------------------------------------------------------------IP360WebApi
    def ip360webapi_recordquzheng(self,token,uid,**confdict):
        '''
            IP360webapi录屏取证。

            参数:
          
            举例:
            | ip360webapi recordquzheng |
        '''
        # 配置login信息
        json_content = ''
        url_string = api.ADMIN_API['ip360recordquzheng'].replace("quzheng",'''%7b%22uid%22%3a''').replace("uid1",uid+'''%2c%22name%22%3a%22''').replace("name1",confdict['name']+time.strftime('%H:%M:%S')+'''%22%2c%22websiteType%22%3a''').replace("website1",confdict['website']+'''%2c%22liveTime%22%3a%22''').replace("livetime1",confdict['livetime']+'''%22%2c%22url%22%3a%22''').replace("url1",confdict['url']+'''%22%7d&token=''').replace("test",token) 
        # 发送request到IP360WEBAPI
        my_request = IP360Request(url_string,json_content)
        my_response = my_request.request_post()
        print my_response

        if '操作成功' in my_response:
            print 'Passed:ip360snapshotquzheng successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:ip360snapshotquzheng failed';
            flag_ret = 0
            return flag_ret

    #----------------------------------------------------------------------------------------IP360WebApi getevidencelist
    def ip360webapi_getevidencelist(self,token,uid,**confdict):
        '''
            IP360webapi获取证据列表。

            参数:
          
            举例:
            | ip360webapi getevidencelist |
        '''
        # 配置login信息
        json_content = ''
        url_string = api.ADMIN_API['ip360getevidencelist'].replace("evidence1",'''%7b%22uid%22%3a''').replace("uid1",uid+'''%2c%22type%22%3a''').replace("type1",confdict['type']+'''%7d&token=''').replace("test",token)
                   
        # 发送request到IP360WEBAPI
        my_request = IP360Request(url_string,json_content)
        my_response = my_request.request_get()
        res = my_response.text
        print "response",res
        evidencelist = []
        evidencelist = res.split(',')
        strname = "\"id\":"
        templist = []
        ids=''
        for i in range(0,len(evidencelist)):
               if strname in evidencelist[i]:
                   templist=evidencelist[i].split(':')
                   ids1 = templist[1]
                   ids = ids1.strip('\"}')
                   break
        print 'Get the id',ids
        # 解析response返回信息

        if 'id' in str(my_response.text):
            print 'Passed:get evidence id';
            flag_ret = 1
            return ids
        else:
            print 'Failed:get evidence id failed';
            flag_ret = 0
            return flag_ret


    #----------------------------------------------------------------------------------------IP360WebApi
    def ip360webapi_addtoinvetory(self,ids,token,uid,**confdict):
        '''
            IP360webapi加入证据库。

            参数:
          
            举例:
            | ip360webapi addtoinvetory |
        '''
        # 配置login信息
        json_content = ''
        url_string = api.ADMIN_API['ip360addtoinvetory'].replace("evidence1",'''%7b%22uid%22%3a''').replace("uid1",uid+'''%2c%22ids%22%3a%22''').replace("ids1",ids+'''%22%2c%22rightOrSnaport%22%3a%22''').replace("rightOrSnapshot1",confdict['rightOrSnaport']+'''%22%2c%22fromSecondaryPage%22%3a%22''').replace("page1",confdict['fromSecondaryPage']+'''%22%7d&token=''').replace("test",token)
        # 发送request到IP360WEBAPI
        my_request = IP360Request(url_string,json_content)
        my_response = my_request.request_post()
        print my_response

        if '"添加操作进行中' in my_response:
            print 'Passed:ip360 evidences add to invetory successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:ip360 evidences add to invetory failed';
            flag_ret = 0
            return flag_ret


    #----------------------------------------------------------------------------------------IP360WebApi
    def ip360webapi_newright(self,token,uid,**confdict):
        '''
            IP360webapi新建确权。

            参数:
          
            举例:
            | ip360webapi newright |
        '''
        # 配置login信息
        boundary = '----------%s' % hex(12345 * 1000)
        json_content = ''
        json_data = ['--%s' % boundary]
        json_data.append('Content-Disposition: form-data; name="%s"\r\n' % 'uid')
        json_data.append(uid)
        json_data.append('--%s' % boundary)

        json_data.append('Content-Disposition: form-data; name="%s"\r\n' % 'type')
        json_data.append(confdict['type'])
        json_data.append('--%s' % boundary)

        json_data.append('Content-Disposition: form-data; name="%s"\r\n' % 'token')
        json_data.append(token)
        json_data.append('--%s' % boundary)
        
        fr=open(r'id_rsa.txt','rb')
        json_data.append('Content-Disposition: form-data; name="%s"; filename="id_rsa.txt"' % 'file')
        json_data.append('Content-Type: %s\r\n' % 'text/plain')
        json_data.append(fr.read())
        fr.close()
        json_data.append('--%s--\r\n' % boundary)

        json_content += '\r\n'.join(json_data)

        url_string = api.ADMIN_API['ip360newright']
        # 发送request到IP360WEBAPI
        my_request = IP360Request(url_string,json_content)
        my_response =my_request.request_post()
        print my_response

        if '上传成功' in my_response:
            print 'Passed:ip360 new right successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:ip360 new right failed';
            flag_ret = 0
            return flag_ret

if __name__ == "__main__" :
    my_obj = IP360Login()

