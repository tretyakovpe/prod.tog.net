# Класс сборочной линии
import snap7
from labelFields import labelFields
from lines import lines

class line:

    client = snap7.client.Client()

    def __init__(self, name):
        self.name = name
        self.ip = lines[self.name]["ip"]
        self.addr = lines[self.name]["addr"]

    def poll(self):
        """
        Check if box is full and make a label for print
        """
        ip = lines[self.name]["ip"]
        addr = lines[self.name]["addr"]
        try:
            print("Connecting... ",ip)
            self.client.connect(ip,0,2)
        except:
            print("Station is not reachable")
        else:
            print("Station",self.name,"connected")
            raw = self.client.db_read(addr,166,1)
            boxFull = snap7.util.get_bool(raw,1,0)
            if boxFull:
                self._getData()
        self.client.disconnect()        

    def _getData(self):
        raw = self.client.db_read(self.addr,154)
