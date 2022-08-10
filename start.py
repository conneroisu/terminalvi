import os
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

def get_marked_status(video_list, video, video_list_file = "video_list.txt"):
    with open(video_list_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line == video + "\n":
            return True
    return False

#function that takes a bool and prints marked if true and unmarked if false
def bool_to_string(bool):
    if bool:
        return "marked"
    else:
        return "unmarked"
    
#function to get the length of a line in the current terminal
def get_line_length():
    return int(subprocess.check_output(['tput', 'cols']))

    
#function that takes a string and returns an appropriate length string terminating in ... for the display of two lines of text
def terminate_long_string(string):
    if len(string) > 9:
        return string[:9] + "..."
    else:
        return string
    
    

#show the video before the video index, the video in the video index, and the video after the video index and their marked status in the video list file
def input_prompt(video_list_file, video_list, video_index):
    with open(video_list_file, 'r') as f:
        lines = f.readlines()
    print("\n")
    print("Video before: " + video_list[video_index - 1] + " " + terminate_long_string(bool_to_string(get_marked_status(video_list, str(video_list[video_index - 1])))+"\n"))
    print("Video in: " + video_list[video_index] + " " + terminate_long_string(bool_to_string(get_marked_status(video_list, str(video_list[video_index]))))+ "<--"+"\n")
    print("Video after: " + video_list[video_index + 1] + " " + terminate_long_string(bool_to_string(get_marked_status(video_list, str(video_list[video_index + 1])))+"\n"))
    return
    
def clear_screen():
    os.system('clear')
    return

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
    vidpane.send_keys('./tvp '+ str(video))
    vidpane.send_keys('\n')
    pane.set_height(4)
    pane.select_pane()
    pane.display_message(str(get_vid_length(video)))
    return vidpane

def run_video(vidpanes, video):
    
    vidpanes.send_keys('./tvp '+ video)
    return vidpanes

#gets a list of all the mp4 files in the subfolder of data 
def init_video_list(data_subfolder):
    data_subfolder = "data/" + data_subfolder
    video_list = []
    for root, dirs, files in os.walk(data_subfolder):
        print("root: " + root)
        for file in files:
            print(file)
            if file.endswith('.mp4'):
                video_list.append(os.path.join(root, file))
        
    return video_list

#Append a string into the video list file
def append_video_to_list(video_list, video):
    with open(video_list, 'a') as f:
        f.write(video + "\n")
    return video_list
  
#Create a text file with the video names in it that are marked for deletion if there is not already a text file
def create_video_list_file(video_list):
    video_list_file = "video_list.txt"
    if not os.path.isfile(video_list_file):
        with open(video_list_file, 'w') as f:
            for video in video_list:
                f.write(video + "\n")
                print('sucess')
    return video_list_file


#Delete a video from the video list file
def delete_video_from_list(video_list, video):
    with open(video_list, 'r') as f:
        lines = f.readlines()
    with open(video_list, 'w') as f:
        for line in lines:
            if line != video + "\n":
                f.write(line)
    return video_list

#function that adds the first video of the video list to the end of the video list 
def add_first_video_to_list(video_list):
    video_list.append(video_list[0])
    
    

   
    

if __name__ == "__main__":
    
    data_subfolder = "MineRLBasaltFindCave-v0"
    video_index = 0
    video_list = []
    video_list = init_video_list(data_subfolder)
    vid_list_file = create_video_list_file(video_list[video_index])
    #video = 'cheeky-cornflower-setter-00c9a1c015d6-20220715-100525.mp4'
    cur_vid = 'cheeky-cornflower-setter-00c9a1c015d6-20220715-100525.mp4'
    session = open_tmux()
    vidpane = start_run_video(session, cur_vid)
    hey = "n"
    max_video_index = len(video_list)
    add_first_video_to_list(video_list)
    while hey !=  'q':
        #while video_index is within range
        clear_screen()
        input_prompt(vid_list_file, video_list, video_index)
        hey = input(str(video_index) + "/" + str(max_video_index))
        
        if hey == "j" and (video_index + 1) < max_video_index:
            vidpane.send_keys('C-c', enter=False,suppress_history=False)
            video_index += 1
            cur_vid = video_list[video_index]
            vidpane = run_video(vidpane, cur_vid)
        if (hey =="k") and  (video_index>0):
            vidpane.send_keys('C-c', enter=False,suppress_history=False)
            video_index -= 1
            cur_vid = video_list[video_index]
            vidpane = run_video(vidpane, cur_vid)
        if hey == "dd":
            #mark video for deletion 
            vid_list_file = create_video_list_file(video_list[video_index])
            vid_list_file = append_video_to_list(vid_list_file, str(video_list[video_index]))
        if hey == "ud": 
            #unmark video for deleton 
            delete_video_from_list(vid_list_file, str(video_list[video_index]))
        else:
            print("unrecognized command")
            
            
#(str(get_vid_length(video)), enter=False)

    
    
