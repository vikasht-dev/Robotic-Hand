# Robotic-Hand
These codes can be used for running the servo motor of robotic hand as per the human hand movement. The webcam detects the human hand and different points in hand, thus the detects data goes to ardunio controller than ardunio transfer the data to servo motor

The Hand Detect file of python contains the code for hand detection, it detect the hand and give output in form of list as 0 and 1 
means for open fingure it will be 1 and for closed it will be 0

supoose just index fingure is open and other are closed so the output will be in [0,1,0,0,0] where 1 shows the opened index fingure and other fingures are closed.
