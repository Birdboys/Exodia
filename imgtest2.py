import os
import time
from playsound import playsound
import psutil
import glob
#playsound('exodia-obliterate.mp3')

def deletion(path):
    p = os.listdir(path)
    for file in p:

        os.remove(path+'\\'+file)
def exodia():
    playsound('Images\\nopatheticcards.mp3')
    
    os.system('Images\\exrightleg.png')
    playsound('Images\\spawn.mp3')

    os.system('Images\\exleftleg.png')
    playsound('Images\\spawn.mp3')

    os.system('Images\\exrightarm.png')
    playsound('Images\\spawn.mp3')

    os.system('Images\\exleftarm.png')
    playsound('Images\\spawn.mp3')

    os.system('Images\\exhead.png')
    playsound('Images\\spawn.mp3')

    for proc in psutil.process_iter():
        if proc.name() == "Microsoft.Photos.exe":
            proc.kill()

    os.system('Images\\unstopable.png')
    playsound('Images\\unstopable.mp3')

    time.sleep(0.25)
                    
    os.system('Images\\obliterate.gif')
    playsound('Images\\exodia-obliterate.mp3')
    deletion(path)

    for proc in psutil.process_iter():
        if proc.name() == "Microsoft.Photos.exe":
            proc.kill()
path = str(input())    
exodia()

'''
stuff = ''
for file in os.listdir():
    if file != 'imgtest.py':
        stuff += "--add-data \"" + file + ";.\" "
print(stuff)

'''
