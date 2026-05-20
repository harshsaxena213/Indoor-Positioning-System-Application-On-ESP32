import network
import time
import machine


#Starting Wlan  
wlan_wifi_sta=network.WLAN(network.STA_IF)
wlan_wifi_sta.active(True)


DEFAULT_LED=machine.Pin(2,machine.Pin.OUT)
DEFAULT_LED.value(True)

RSSI=[]
counter=50


for i in range(counter):

    scan_list=wlan_wifi_sta.scan()
    SSID=scan_list[0][0].decode()
    RSSI_FOUND=scan_list[0][3]
    
    
    if SSID=="TestNetwork":
        RSSI.append(RSSI_FOUND)
        print(f"Sample:- ",i+1," RSSI:- ",RSSI_FOUND)
    
    #Small Dealy Between Scan 
    time.sleep(0.2)
    
DEFAULT_LED.value(False)
print("Done")
print(RSSI)
