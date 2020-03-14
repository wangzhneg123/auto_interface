# coding:utf-8
import requests
import pytest



@pytest.fixture(scope="package")
def topGetSession():
   return  requests.session()