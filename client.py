# encoding: utf-8

from suds.client import Client

def hello_client():
    client = Client('http://127.0.0.1:8000/impl/wsdl')
    result = client.service.hello_test('world!')
    print result
    
if __name__ == '__main__':
    hello_client()
