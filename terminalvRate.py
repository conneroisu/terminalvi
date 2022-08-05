import os 
import subprocess 
import threading
import keyboard
from multiprocessing import Process
import time
import logging 




    
if __name__ == '__main__':

    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

    path = r'/home/connero/basalt_2022_competition_submission_template/data/MineRLBasaltFindCave-v0'
    vids = []
    for peth in os.listdir(path):
        if "mp4" not in os.path.basename(peth):
            continue
        vids.append(peth)



    for vid in vids:
             
        name = path + "/" + vid
        subprocess.run(["./tvp",name])
        while not keyboard.is_pressed('p') :
            continue
        subprocess.run(["killall", "tvp"])
