from MexidronHttpClient.client import MexidronHttpClient as mhc
import simplejson as json
import ConfigParser, os


class MexidronLoadImages:
    def __init__(self):
        print mhc
        self.mhc = mhc("http://192.168.3.101:8000")
        self.json_example = '{"IMG1" : "foto.png","IdBatea":' \
                            ' "b0001","IdCuerda": "b0001c01",' \
                            '"Timestamp": "2016-02-27T16:40:13+00:00",' \
                            '"Altura": "230",' \
                            '"Temperatura": "15",' \
                            '"Presion": "1,5"
        }"

    def loadFiles(self,):
        parsed_json = json.loads(self.json_example)
        print(parsed_json['IMG'])

if __name__ == '__main__':
    mli = MexidronLoadImages()
    mli.loadFiles()
