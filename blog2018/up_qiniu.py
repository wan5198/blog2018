# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag
def qiniu_up(url_img,url_name):
    #需要填写你的 Access Key 和 Secret Key
    access_key = 'jScNMMq55B0O2SXah4Qw9c10jM58tzlog3OEHNAh'
    secret_key = 'bGeE3Z0nTo_LLl31YYUbOT9vVTsPCos4lwk6OVpN'
    #构建鉴权对象
    q = Auth(access_key, secret_key)
    #要上传的空间
    bucket_name = 'blog2018'
    #上传到七牛后保存的文件名
    key = url_name
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    #要上传文件的本地路径
    localfile = url_img
    ret, info = put_file(token, key, localfile)
    print(dir(ret))
    print(ret['key'])
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)