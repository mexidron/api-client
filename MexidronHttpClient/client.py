#!/usr/bin/env python


__version__ = "0.1"
__all__ = ["MexidronHttpClient"]
__author__ = "pnietoiglesias"
__home_page__ = "http://github.com/mexidron/api-client"

import requests

class MexidronHttpClient:
    def __init__(self, server="localhost"):
        self.server=server
        self.session=requests.Session()
        self.session.headers.update({'referer': self.server})

    def doUpload(self, filenames):
        import magic
        mime = magic.Magic(mime=True)


        for filename in filenames:
            multiple_files = [(filename, (filename, open(filename, 'rb'), mime.from_file("testdata/test.pdf")))]
        url=self.server
        return(self.session.post(url, files=multiple_files))

    def doGet(self,url):
        return (sel.session.get(url))


if __name__ == '__main__':
    mu=MexidronHttpClient("http://192.168.3.101:8000")
    mu.test()
