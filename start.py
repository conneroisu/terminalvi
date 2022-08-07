from os import system 
import libtmux
import time
import subprocess 
from subprocess import call 
import json
import cv2



def get_vid_length(file_name):
    video = cv2.VideoCapture(file_name)
    duration = video.get(cv2.CAP_PROP_POS_MSEC)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    return frame_count


def open_tmux():
#    task = system('tmux new -s terminalvi')
#    call(task)
    server = libtmux.Server()
    session = server.find_where({"session_name": "terminalvi"})
    return session

def start_run_video(session, video):
    get_vid_length(video)
    window = session.attached_window
    pane = window.attached_pane
    vidpane = window.split_window(attach=False)
    vidpane.send_keys('./tvp '+ video)
    vidpane.send_keys('\n')
    pane.set_height(3)
    pane.select_pane()
    pane.display_message(str(get_vid_length(video)))
    pane.send_keys(str(get_vid_length(video)), enter=False)
    return vidpane

def run_video(vidpanes, video):
    vidpanes.send_keys('./tvp '+ video)
    vidpanes.send_keys('\n')
    return vidpanes

#gets a list of all the mp4 files in the subfolder of data called MineRLBasaltFindCave-v0
def init_video_list():
    




if __name__ == "__main__":
    
    video = 'cheeky-cornflower-setter-00c9a1c015d6-20220715-100525.mp4'
    session = open_tmux()
    vidpane = start_run_video(session, video)
    hey = "n"
    while hey !=  'q':
        hey = input("dd to mark for deletion ud to unmark")
        if hey == "j":
            vidpane.send_keys('C-c', enter=False,suppress_history=False)
            vidpane = run_video(vidpane, video)
        if 

    
    