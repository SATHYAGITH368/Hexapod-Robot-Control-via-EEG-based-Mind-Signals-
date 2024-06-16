# Hexapod-Robot-Control-via-EEG-based-Mind-Signals-

This project aims to develop an innovative system for controlling a hexapod robot using brain-computer interface (BCI) technology, leveraging the NVIDIA Jetson Nano and the Robot Operating System (ROS). By utilizing EEG (electroencephalography) devices, the system captures and interprets the user's brain signals to command the hexapod robot.

1.⁠ ⁠Integration of an EEG headset with signal processing algorithms running on the Jetson Nano to decode mental commands.
2.⁠ ⁠Design and implementation of ROS-based software to map EEG signals to robot movements, utilizing ROS pub/sub for efficient communication.


The end goal is to enable hands-free operation of the hexapod robot, demonstrating the potential of mind-controlled robotics in applications ranging from assistive technologies to advanced human-robot interaction scenarios




## EEG (Electroencephalography) 

Electroencephalography (EEG) is a technique used to record electrical activity in the brain. It measures voltage fluctuations resulting from ionic current flows within the neurons of the brain. EEG is non-invasive and involves placing electrodes on the scalp, which detect and record these electrical signals.

Key Concepts:
Electrodes: Small metal discs or electrodes are placed on specific locations of the scalp. These electrodes detect electrical signals produced by the firing of neurons in the brain.

Brain Waves: EEG records brain waves, which are categorized into different frequency bands:

Delta (0.5-4 Hz): Associated with deep sleep and unconsciousness.
Theta (4-8 Hz): Related to light sleep, relaxation, and creativity.
Alpha (8-13 Hz): Present during wakeful relaxation, calmness, and meditation.
Beta (13-30 Hz): Associated with active thinking, focus, and problem-solving.
Gamma (30-100 Hz): Involved in higher cognitive processes, memory, and learning.
Applications: EEG is widely used in neuroscience research, clinical diagnosis, and brain-computer interface (BCI) systems:

Neuroscience: Studying brain function, cognition, and neurological disorders.
Clinical: Diagnosing epilepsy, sleep disorders, and brain injuries.
BCI: Enabling communication and control of devices directly through brain signals, as in this project.

## USAGE OF EEG IN THIS PROJECT:
In this project, EEG signals are used to determine the user's attention and meditation levels:

Attention: Higher levels of beta waves indicate active concentration and focus.
Meditation: Increased alpha and theta waves indicate relaxed and meditative states.
These EEG signals are processed by the server (read.py), which translates them into commands for the robot controller (robot_controller.py). This allows for a brain-controlled interaction where the robot's movements are influenced by the user's mental state, as detected through EEG signals.

## ROS

ROS (Robot Operating System) is an open-source framework designed to simplify the development of complex robotic systems. It provides a collection of tools, libraries, and conventions that facilitate tasks such as hardware abstraction, device drivers, communication between processes, and package management.

Key Concepts:
Nodes: ROS implements a distributed computing architecture where functionality is divided into nodes. Nodes are independent processes that communicate with each other using ROS topics, services, and actions.

Topics: Nodes can publish messages to topics or subscribe to topics to receive messages. Topics enable asynchronous communication between nodes, allowing them to send and receive data (e.g., sensor data, control commands).

Services: Nodes can offer services that other nodes can call to request specific tasks. Services follow a request-response pattern and are useful for synchronous communication.

Actions: Actions extend the capabilities of services by allowing nodes to execute long-running tasks in a non-blocking manner. They provide feedback on task progress and can be preempted if necessary.

Packages: ROS packages are the basic unit of software in ROS. They contain libraries, executables, scripts, configuration files, and documentation needed to perform specific tasks.


## SOCKET PROGRAMMING OVERVIEW
Socket programming is a fundamental technology for network communication, enabling applications to connect, send, and receive data over a network. It uses the concept of sockets, which are endpoints for communication between machines or processes.

Key Concepts:
Socket: A socket represents one endpoint of a two-way communication link between two programs running on the network. It includes an IP address and a port number.

Client-Server Model: Socket programming typically follows a client-server architecture:


## COMPONENTS
Server (read.py):

Acts as the brain interface, using EEG signals to determine the user's attention and meditation levels.
Utilizes socket programming to communicate with the client.
Sends commands to the robot controller based on the received EEG data.
Client (robot_controller.py):

Receives commands from the server via socket communication.
Controls the robot's movements on the Jetson Nano platform.
Commands include moving forward, rotating, and stopping the robot based on the EEG signals received.

## REQUIREMENTS
Hardware:

Jetson Nano with appropriate peripherals for robot control.
EEG device compatible with the Jetson Nano.
Software:

Libraries: socket, Jetson Nano APIs (specifics depending on robot control mechanisms).
Git - Download & Install Git. OSX and Linux machines typically have this already installed.
Python - Download & Install Python3 - Minimum requirement 3.8.x
Pybluez - Bluetooth Configuration
Mindwave Configuration with python - Mindwave configuration

## SETUP AND USAGE:
Server Setup:

Ensure the EEG device is connected and configured with the Jetson Nano.
Run python2 read.py on the Jetson Nano.
Client Setup:

Adjust robot_controller.py to interface with your specific robot hardware.
Run python3 robot_controller.py on the Jetson Nano.

Both the command should run simultaneously

## OPERATION:

The server (read.py) reads EEG signals and interprets attention and meditation levels.
Based on these levels, commands are sent via sockets to robot_controller.py.
The client (robot_controller.py) translates commands into robot movements (forward, rotate, stop).
Server: Waits for incoming connections from clients on a specified port. It handles multiple client connections simultaneously.
Client: Initiates a connection to a server's socket using the server's IP address and port number.
Communication Modes:

Stream Sockets: Provides a reliable, connection-oriented communication channel (e.g., TCP).
Datagram Sockets: Supports connectionless, unreliable communication where messages are sent in packets (e.g., UDP).


## RESOURCES:


| Topic      | Reference Link |
| ----------- | ----------- |
| Introduction to EEG and Speech based Emotion Recognition | Book from Dr Babasaheb Ambedkar Marathwada University  Aurangabad, India |
| Python library to read data from Mindwave Neurosky | https://github.com/robintibor/python-mindwave-mobile 



## NEUROSKY MINDWAVE HEADSET:
![NeuroSky-MindWave-headset](https://github.com/SATHYAGITH368/Hexapod-Robot-Control-via-EEG-based-Mind-Signals-/assets/142714885/d3f6dea7-4221-4e44-9c24-5e832237386e)



## JETHEXA
![PHOTO-2024-06-16-19-34-35](https://github.com/SATHYAGITH368/Hexapod-Robot-Control-via-EEG-based-Mind-Signals-/assets/142714885/e8ee97e0-cb4c-4307-8e5f-3a3331c39c11)


![Uploading PHOTO-2024-06-16-21-39-04.jpg…]()





