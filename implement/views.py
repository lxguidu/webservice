# encoding: utf-8

from .service import ApplicationService
from soaplib.core.service import DefinitionBase
import json
from soaplib.core.model.primitive import String
from soaplib.core import Application
import soaplib
from soaplib.core.service import soap

# Create your views here.
class HelloTest(DefinitionBase):
    __tns__ = ''
    
    @soap(String, _returns=String)
    def hello_test(self, name=None):
        return 'Hello, %s' % name
    
service = ApplicationService([HelloTest,], 'tns')