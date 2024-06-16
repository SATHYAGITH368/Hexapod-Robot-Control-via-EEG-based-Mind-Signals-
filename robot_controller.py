#!/usr/bin/env python3

import rospy
from jethexa_controller import client
import socket
import threading


from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
class MovingNode:
   def __init__(self):
        rospy.init_node("moving_node", anonymous=True, log_level=rospy.INFO)
        self.jethexa = client.Client(self)
        self.attention_level=0 
        self.meditation_level=0

        self.attention=rospy.Publisher('mindwave/attention',Int32,queue_size=10)
        self.meditation=rospy.Publisher('mindwave/meditation',Int32,queue_size=20)
      
        rospy.Subscriber('mindwave/attention',Int32,self.attention_callback)
        rospy.Subscriber('mindwave/meditation',Int32, self.meditation_callback)

        self.socket_thread=threading.Thread(target=self.read_from_socket)
        self.socket_thread.daemon=True
        self.socket_thread.start()

        


   def attention_callback(self,data):
       
       self.attention_level=data.data
       self.control_robot()

   
   def meditation_callback(self,data):
       self.meditation_level=data.data
       self.control_robot()


   def control_robot(self):
       if 50>self.attention_level:
           self.stop()
       else:
          #if self.attention_level>self.meditation_level:
          #   self.move_forward()
          #elif self.attention_level>90:
          self.rotate()
          
   def forward(self):
        self.jethexa.traveling(
                  gait=1, 
                  stride=40.0,
                  height=15.0,
                  direction=0,
                  rotation=0.0,
                  time=1, 
                  steps=0, 
                  interrupt=True,
                  relative_height=False)
        rospy.loginfo("forward")
   def rotate(self):
        self.jethexa.traveling(
                  gait=1, 
                  stride=40.0, 
                  height=15.0, 
                  direction=0, 
                  rotation=0.5,
                  time=0.8, 
                  steps=0, 
                  interrupt=True,
                  relative_height=False)
        rospy.loginfo("rotate")
   def stop(self):
        rospy.loginfo("stop")
        self.jethexa.traveling(gait=0)
   def read_from_socket(self,host='localhost',port=10001):
      with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
         s.connect((host,port))
         print(f"connected to server at {host}:{port}")
         while not rospy.is_shutdown():
             data=s.recv(1024).decode()
             print(data)
             if data:
                for line in data.split("\n"):
                     if line.startswith("Attention"):
                           attention_value=int(line.split(':')[1].strip())
                           print(attention_value)
                           self.attention_callback(Int32(attention_value))
                     elif line.startswith("Meditation"):
                           meditation_value=int(line.split(':')[1].strip())
                           #print(line)
                           #self.meditation_callback(Int32(meditation_value))
  

  

if __name__ == "__main__":
    try:
       MovingNode()
     
       rospy.spin()
    except rospy.ROSInterruptException:
       pass

    
    





























  

