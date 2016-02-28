import simplejson as json
import math
import os

import camera
import config
import wifi

from client import MexidronHttpClient as mhc
    #def pushFiles(self):
    #def save_work(self,response):

class Controller:
    def __init__(self):
        self.index = 0

    def set_batea_id(self,id):
        self.batea_id = id

    def set_cord_id(self,id_cord):
        self.cord_id = id_cord

    def set_cord_lenght(self,altitude):
        self.cord_lenght = altitude

    def set_cord_destination(self,point):
        self.cord_destination = point

    def set_period(self,period):
        self.period = period

    def make_job(self,path):

        job_total_duration = 10 #math.ceil(float(self.cord_lenght)/config.DRONE_SPEED)
        job_current_duration = 0

        while (job_current_duration <= job_total_duration ):
            base_path = path + "/" + str(self.batea_id) + "_" + str(self.cord_id) + "_" + str(job_current_duration)
            camera.take_pic( base_path + ".jpeg")
            job_current_duration += self.period

            #guardamos datos de la foto en json
            current_altitude = job_current_duration*config.DRONE_SPEED
            json_response = { 'id_batea' : self.batea_id,
                          'id_cuerda' : 2,
                          'destino' : self.cord_destination,
                          'z' : current_altitude,
                          'image' :  str(self.batea_id) + "_" + str(self.cord_id) + "_" + str(job_current_duration) + ".jpeg"
                          }
            data = json.dumps(json_response)
            with open(base_path + '.json', 'w') as outfile:
                json.dump(data, outfile)

            import time
            time.sleep(self.period)


    def upload_job(self,path):
        import glob
        files = glob.glob(path + "/*.json")
        for eachfile in files:
            base = os.path.basename(eachfile)
            files = [os.path.splitext(base)[0]+ ".jpeg",base]
            response = client.doUpload(config.API_UPLOAD_JOBS,files)
            print response.json()


if __name__ == '__main__':
    #cargamos objetos a manejar
    client = mhc(config.SERVER_NAME)
    controller = Controller()
    wifi_controller = wifi.MexiWifi()


    #Creacion de directorios
    try:
        os.stat(config.PATH_DATA_CAPTURE)
    except:
        os.mkdir(config.PATH_DATA_CAPTURE)

    try:
        os.stat(config.PATH_DATA_HISTORY)
    except:
        os.mkdir(config.PATH_DATA_HISTORY)


    #TODO activar la wifi
    print "Levantamos interfaz wifi..."
    print ""
    wifi_controller.wifi_power_on(config.WIFI_ETH)


    while True:
        print "Pulse 0 para conectar al AP del batea"
        print "Pulse 1 para iniciar simulacion"
        print "Pulse 2 para iniciar captura de imagenes"
        print "Pulse 3 para enviar imagenes al servidor"
        print "Pulse 4 para salir"
        value = int(raw_input())

        if value == 0:
            print "Conectando a la wifi mexidron..."
            wifi_controller.wifi_connect(config.WIFI_ETH,config.WIFI_SSID,config.WIFI_PASSWORD)
        elif value == 1:
            print "Pediendo trabajo a batea..."
            response = client.doGet(config.API_CALL_JOBS)
            try:
                request_job = response.json()
            except:
                print "Error comunicando con servidor..."
                continue

            controller.set_batea_id(request_job["idBatea"])
            controller.set_cord_id(request_job["idCuerda"])
            controller.set_cord_destination(request_job["puntoFinal"])
            controller.set_cord_lenght(request_job["altura"])
            controller.set_period(request_job["intervaloFoto"])

            print "Descargando trabajo pendiente de batea: " + \
                    str(controller.batea_id) + " Cuerda: " + str(controller.cord_id) \
                    + " Altura de cuerda: " + str(controller.cord_lenght)
            print "+-+-+-+-+"

        elif value == 2:
            print "Capturando imagenes..."
            controller.make_job(config.PATH_DATA_CAPTURE)

        elif value == 3:
            print "Enviando imagenes..."
            controller.upload_job(config.PATH_DATA_CAPTURE)
            print "Apagando interfaz wifi..."
            #wifi_controller.wifi_power_off()

        else:
            break
