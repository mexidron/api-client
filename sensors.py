#!/usr/bin/env python

__version__ = "0.1"
__all__ = ["MexidromBarometer"]
__author__ = "NachoSeijo"
__home_page__ = "http://github.com/mexidrom/api-client"


class barometer:

    def __init__(self):
        #variables related to temperature
        self.TEMP_RAW = '/sys/class/i2c-dev/i2c-1/device/1-0060/iio\:device0/in_temp_raw'
        self.TEMP_SCALE = '/sys/class/i2c-dev/i2c-1/device/1-0060/iio\:device0/in_temp_scale'

        #variables related to pressure
        self.PRES_RAW = '/sys/class/i2c-dev/i2c-1/device/1-0060/iio\:device0/in_pressure_raw'
        self.PRES_SCALE = '/sys/class/i2c-dev/i2c-1/device/1-0060/iio\:device0/in_pressure_scale'

    #returns temperature
    def getTemperature(self):
        with open (self.TEMP_RAW, 'rb') as tr:
            temp = tr.read()
        with open (sef.TEMP_SCALE, 'rb') as ts:
            scale = ts.read()
        return float(temp) * float(scale)

    #returns pressure
    def getPressure(self):
        with open (self.PRES_RAW, 'rb') as pr:
            pres = pr.read()
        with open (self.PRES_SCALE, 'rb') as ps:
            scale = ps.read()
        return float(pres) * float(scale)

    #returns altitude
    def getAltitude(self):
        P0 = 1013.25
        P = self.getPressure()
        T = self.getTemperature()
        return ((( pow( ( P0 / P ), (1/5.257)) ) - 1 ) * (T + 273.15)) / 0.0065
