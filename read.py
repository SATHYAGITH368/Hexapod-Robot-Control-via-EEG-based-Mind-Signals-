import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint,AttentionDataPoint,MeditationDataPoint,DataPoint,UnknownDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap
import socket
  

def start_mindwave_server(host='localhost',port=10001):
           mindwaveDataPointReader = MindwaveDataPointReader()
           print('starting')
           mindwaveDataPointReader.start()
   	   if(mindwaveDataPointReader.isConnected()):
           	s=socket.socket()
           	s.bind((host,port))
           	s.listen(1)
                print('Ready')
                while True:
		   	conn,addr=s.accept()
		       	print('connected by',addr)
		        while True:
		        	
					#print(1)
		     			dataPoint=mindwaveDataPointReader.readNextDataPoint()
					#print(2)
		                        if(not dataPoint.__class__ is RawDataPoint):
                                             if isinstance (dataPoint,AttentionDataPoint):
                                                   print(dataPoint)
                                                   
                                                   data=dataPoint.__str__()
   					           #print('Attention')
                                                   conn.sendall(data.encode())
                                             #elif isinstance (dataPoint,MeditationDataPoint):
                                                   #print(dataPoint)
                                                   #data=dataPoint.__str__()
						   #print(dataPoint)
                                                   #print('Meditation')
                                                   #conn.sendall(data.encode())
                                             #data='attention:'+str(dataPoint)
					     #print(data)
					     #conn.sendall(data.encode())

           else:
                print("could not connect to mindwavemobiledevice")
 
        
            


         




if __name__ == '__main__':
       start_mindwave_server()
    
