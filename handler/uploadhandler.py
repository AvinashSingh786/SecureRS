import os
from django.conf import settings
import hashlib
from django.core.files.uploadhandler import FileUploadHandler
from django.core.exceptions import SuspiciousOperation

from django.http import HttpResponse

class HashFileUploadHandler(FileUploadHandler):
    """Hashes data as it is uploaded"""
    def __init__(self, request=None, key=None):
        self.hash = hashlib.md5()
        super().__init__(request=request)
    
    def new_file(self, *args, **kwargs):
        return super().new_file(*args,**kwargs)

    def receive_data_chunk(self, raw_data, start):
        self.hash.update(raw_data)
        return raw_data
    
    def file_complete(self, file_size):
        
        if self.request.META["HTTP_MD5SUM"]:
            if self.hash.hexdigest() == self.request.META["HTTP_MD5SUM"]:
                return

        raise SuspiciousOperation("Hash Digest does not match")
