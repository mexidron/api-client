import simplejson as json

import camera
import config

from client import MexidronHttpClient as mhc


class MexidronLoaderImages:
    def __init__(self,server):
        print mhc
        self.client = mhc(server)
        self.json_example = '{"IMG1" : "foto.png","IdBatea",\
                            "b0001","IdCuerda": "b0001c01",\
                            "Timestamp": "2016-02-27T16:40:13+00:00",\
                            "Altura": "230",\
                            "Temperatura": "15",\
                            "Presion": "1,5"}'

    def pushFiles(self):
        parsed_json = json.loads(self.json_example)
        print(parsed_json['IMG'])

    def save_work(self,response):
        parsed_response = json.loads(reponse)

class CameraController:
    def __init__(self):
        self.index = 0

    def setIdBatea(self,id):
        self.id_batea = id

    def setCord(self,id_cord):
        print id_cord

    def setPeriod(self,period):
        self.period = period
        print period

    def takePhotos(self,path,period):
        camera.take_pic(path + "/"+self.index + "_test1.jpeg")
        sleep(period)
        camera.take_pic(path + "/"+self.index + "_test2.jpeg")

        #TODO
        json_mock = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
        data = json.dumps(json_mock)

        with open(path,self + self.index + '_data.json', 'w') as outfile:
            json.dump(data, outfile)

if __name__ == '__main__':
    #cargamos clases a manejar
    controller = MexidronLoaderImages(config.SERVER_NAME)

    while True:
        controller.pending = False

        print "Pulse 1 para iniciar simulacion"
        print "Pulse 2 para iniciar captura de imagenes"
        print "Pulse 3 para enviar imagenes al servidor"
        print "Pulse 4 para salir"
        value = int(raw_input())
        if value == 1:
            print "Llamando a trabajo..."
            response = controller.client.doGet(config.SERVER_NAME + config.API_WORKING)
            #c=.launch_work(response)
            print ""
        elif value == 2:
            print "Capturando imagenes..."
            print ""
        elif value == 3:
            print "Enviando imagenes..."
            print ""
        else:
            break
    #mli = MexidronLoadImages()
    #mli.loadFiles()
