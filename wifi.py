WifiName='sanjurjo'
WifiPassword='None'
WirelessETH='wlan0'
NotFound=True
from wifi import Cell, Scheme
import subprocess
subprocess.call('ifconfig ' + WirelessETH +  ' up'], shell=True)
os.system(ifconfig )
while (NotFound):
    ap_list=Cell.all(WirelessETH)
    for item in ap_list:
        if(item.ssid.find(WifiName) == 0):
            print item
            NotFound=False
            scheme.delete()
            scheme = Scheme.for_cell(WirelessETH,WifiName,item,passkey=WifiPassword)
            scheme.save()
    scheme.activate()

#We call the Upload service

subprocess.call('ifconfig ' + WirelessETH +  ' down', shell=True)