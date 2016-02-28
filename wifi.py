class MexiWifi:
    def wifi_power_on (self,eth_device):
        "This powers wifi ON"
        import subprocess
        subprocess.call('ifconfig ' + eth_device +  ' up', shell=True)
        return
    def wifi_power_off (self,eth_device):
        "This powers wifi OFF"
        import subprocess
        subprocess.call('ifconfig ' + eth_device +  ' down', shell=True)
        return
    def wifi_connect (self,eth_device, SSID, password):
        "This connects to a WiFi network with/without passkeys"
        from wifi import Cell, Scheme
        NotFound = True
        ap_list=Cell.all(eth_device)
        while (NotFound):
            for item in ap_list:
                if(item.ssid.find(SSID) == 0):
                    print item
                    NotFound=False
                    scheme.delete()
                    scheme = Scheme.for_cell(eth_device,SSID,item,passkey=password)
                    scheme.save()
            scheme.activate()
        return

