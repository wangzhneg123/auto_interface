# coding:utf-8

from  common.configs import  *
from  common.Util import *


import pytest

# def  fun_getValue():
#     return [
#         # 正确用户名，错误密码
#         ("wang999","youyou","密码错误！"),
#         ("wang999","","密码错误！"),
#         ("wang999","    ","密码错误！"),
#          # 错误的用户名，正确的密码
#         ("", "wang999", "账户不能为空！"),
#         ("     wang999", "wang999", "用户不存在！"),
#         # ("   ", "wang999", "账户不能为空！"),  #情况特殊  用户不存在！
#         # 错误的用户名 错误的密码
#         ("ajsdhfoa hwso ihiokajgvo pajsvnb", "asdfasknfasdoifaos", "用户不存在！")
#
#     ]

def fun_getValue():
    return read_excel("dataExcel.xlsx","login")





class  Test_login():

    def loginTest(self,Url , name,pwd,s):
        mbody = {
            "mobile":name,
            "password":pwd,
            "type":"1"
        }
        mhearders ={
            "X-Requested-With":"XMLHttpRequest",
            "User-Agent":UserAgent
        }
        mdata=s.post(url=Url,data=mbody,headers=mhearders)
        return mdata


    def test_01_ok(self,topGetSession):
        """
        正向： 正确的用户名 和正确的密码
        :param topGetSession:  session对象 主要是用来保存cookie使用
        :return:
        """
        topGetSession.get(url=URL_login)
        value=self.loginTest(URL_login,"wang999","wang999",topGetSession)
        msg = value.json().get("msg")
        assert msg =="登录成功"


    @pytest.mark.parametrize(("name","pwd","Msg"),fun_getValue())
    def test_02_no(self,topGetSession,name,pwd,Msg):
        """
        反向：【错误用户名，正确密码】【正确用户名，错误密码】【错误用户名，错误密码】  通过参数化实现
        :param topGetSession:  session对象 主要是用来保存cookie使用
        :return:
        """
        topGetSession.get(url=URL_login)
        value = self.loginTest(URL_login, name, pwd, topGetSession)
        msg = value.json().get("msg")
        assert msg == Msg


