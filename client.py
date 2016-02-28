#!/usr/bin/env python


__version__ = "0.1"
__all__ = ["MexidronHttpClient"]
__author__ = "pnietoiglesias"
__home_page__ = "http://github.com/mexidron/api-client"

import requests
import config

class MexidronHttpClient:
    def __init__(self, server="localhost"):
        self.server=server
        self.session=requests.Session()
        self.session.headers.update({'referer': self.server})

    def doUpload(self, url, filenames):

        for filename in filenames:
            #print "Subiendo fichero... " + filename
            multiple_files = [(filename, (filename, open(config.PATH_DATA_CAPTURE + "/"+filename, 'rb')))]
        url_post=self.server + url
        return(self.session.post(url_post, files=multiple_files))

    def doGet(self,url):
        return (self.session.get(self.server + url))


if __name__ == '__main__':
    mu=MexidronHttpClient("http://google.com")
    mu.doGet()