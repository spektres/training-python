from time import sleep

import pyautogui as pag

start = pag.position() 

while start.x > 600:
    print(start.x, start.y)
    start = pag.position() 
    sleep(0.05)
    signal = pag.position()
    if start.y > signal.y + 100: break


while start.x > 100:
    pag.moveRel(-5, -3, 2)
    sleep(1)




    
