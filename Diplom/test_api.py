import requests
import pytest 
import allure
from constant import url, url2, url3, url4, url5, token, data1 


# @pytest.mark.test_api.py
# @pytest.fixture()
@allure.id('Chitay-Gorod1')
def test_search_book_Gogol():
   headers = {"authorization":f"Bearer {token}"}
   book = requests.get(url, headers=headers)
   print(book.status_code)
   print(book.text)
   assert book.status_code == 200

@allure.id('Chitay-Gorod2')
def test_search_book_Tolstoy():
   headers = {"authorization":f"Bearer {token}"}
   book = requests.get(url5, headers=headers)
   print(book.status_code)
   print(book.text)
   assert book.status_code == 200

@allure.id('Chitay-Gorod3')
def test_add_book():
   headers = {"authorization":f"Bearer {token}"}
   book = requests.post(url2,headers=headers, json=data1)
   print(book.status_code)
   print(book.text)
   assert book.status_code == 200


def test_checking_cart():
   headers = {"authorization":f"Bearer {token}"}
   book = requests.get(url3, headers=headers)
   print(book.status_code)
   print(book.text)
   assert book.status_code == 200
   

def test_delete_book():
   headers = {"authorization":f"Bearer {token}"}
   book = requests.delete(url4, headers=headers)
   print(book.text)
   print(book.status_code)
   assert book.status_code == 204


test_search_book_Gogol()
test_search_book_Tolstoy()
test_add_book()
test_checking_cart()
test_delete_book()