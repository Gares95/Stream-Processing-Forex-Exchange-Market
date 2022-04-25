import socket

from dataclasses import dataclass
import json
    
@dataclass
class Price:
    
    def __init__(
            self,
            unique_id: str,
            inst: str,
            bid: str,
            ask: str,
            current_time: str
            ):  
        
        self.unique_id = unique_id
        self.inst = inst
        self.bid = self.calculate_new_price("bid", bid)
        self.ask = self.calculate_new_price("ask", ask)
        self.current_time = current_time
        
    def calculate_new_price(self, operation, price):
        commission = float(price) * (0.1/100)
        if(operation == "bid"):
            commission = commission*(-1)
        
        new_price = float(price) + commission
        
        return new_price
    
    def serialize(self):
        return json.dumps(
            {
                "unique_id": self.unique_id,
                "inst": self.inst,
                "bid": self.bid,
                "ask": self.ask,
                "current_time": self.current_time,
            }
        )



if __name__ == '__main__':
    print("Starting Server...")

    serversocket = socket.socket()
    host = socket.gethostname()
    port = 9000

    serversocket.bind((host,port)) 
    serversocket.listen(1)
    clientsocket,addr = serversocket.accept()
    with clientsocket:
        print(f"Connected by {addr}")
        while True:
            data = clientsocket.recv(1024)
            message = data.decode('utf8')
            # if not data:
            #     break
            print("Message recieved: {}".format(message))

            new_price = Price(*message.split(',')).serialize()

            print("Processed price: {}".format(new_price))
            