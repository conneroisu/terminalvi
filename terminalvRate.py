import os 
import subprocess 
import time
import logging 
improt libtmux

PROJECT_PATH = ''
def tmux(command):
    system('tmux %s' % command)


def tmux_shell(command):
    tmux('send-keys "%s" "C-m"' % command)
    
if __name__ == '__main__':
    # vim in project
    tmux('select-window -t 0')
    tmux_shell('cd %s' % PROJECT_PATH)
    tmux_shell('vim')
    

#    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

    path = r'/home/connero/basalt_2022_competition_submission_template/data/MineRLBasaltFindCave-v0'
    vids = []
    for peth in os.listdir(path):
        if "mp4" not in os.path.basename(peth):
            continue
        vids.append(peth)



    for vid in vids:
             
        name = path + "/" + vid
        #shell('./tvp ' + name , input_='')
#        subprocess.run(["./tvp",name])
#        while not keyboard.is_pressed('p') :
#            continue
#        subprocess.run(["killall", "tvp"])
