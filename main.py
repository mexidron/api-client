from MexidronHttpClient.client import MexidronHttpClient as mhc
import simplejson as json
#import camera
import wifi.MexiWifi as wifi
import ConfigParser, os


class MexidronLoadImages:
    def __init__(self):
        print mhc
        self.client = mhc("http://192.168.3.101:8000")
        self.json_example = '{"IMG1" : "foto.png","IdBatea",\
                            "b0001","IdCuerda": "b0001c01",\
                            "Timestamp": "2016-02-27T16:40:13+00:00",\
                            "Altura": "230",\
                            "Temperatura": "15",\
                            "Presion": "1,5"}'

    def pushFiles(self,):
        parsed_json = json.loads(self.json_example)
        print(parsed_json['IMG'])

    def save_work(self,response):
        parsed_response = json.loads(reponse)


if __name__ == '__main__':
    #cargamos clases a manejar
    controller = MexidronLoadImages(SERVER_NAME)

    while True:
        controller.pending = False

        print "Pulse 1 para iniciar simulacion"
        print "Pulse 2 para iniciar captura de imagenes"
        print "Pulse 3 para enviar imagenes al servidor"
        print "Pulse 4 para salir"
        value = int(raw_input())
        if value == 1:
            print "Llamando a trabajo..."
            response = controller.client.doGet(SERVER_NAME + API_WORKING)
            controller.launch_work(response)
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
