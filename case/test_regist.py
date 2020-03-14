# coding:utf-8

from common.configs import *
from common.Util import *
import  requests
import pytest


def fun_getValue():
    return read_excel("dataExcel.xlsx", "regist")





class Test_regist():

    def registTest(self,s, Url, pName, pEmail, pPassword, pRepassword):
        mbody = {
            "username": pName,
            "email": pEmail,
            "password": pPassword,
            "repassword": pRepassword,
        }
        mhearders = {
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": UserAgent
        }
        mdata = s.post(url=Url, data=mbody, headers=mhearders)
        return mdata



    def  test_01_no(self):
        """
        正向：合法的用户名，合法的邮箱，合法的密码，密码相同的确认密码   ---》注册成功
        :return:
        """
        mjson=self.registTest(requests,URL_regist,"wang9999", "wang9999@qq.com", "wang9999", "wang9999")
        assert mjson.get("msg")


    @pytest.mark.parametrize(("pName", "pEmail", "pPassword", "pRepassword","Msg"),fun_getValue())
    def  test_01_no(self,pName, pEmail, pPassword, pRepassword,Msg):
        """
        反向的
        :param pName:用户名
        :param pEmail: 邮箱
        :param pPassword: 密码
        :param pRepassword:确认密码
        :param Msg:返回的 内容【断言使用】
        """
        mjson=self.registTest(requests,URL_regist,pName, pEmail, pPassword, pRepassword)
        assert mjson.json().get("msg") ==Msg
