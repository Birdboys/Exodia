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
    playsound('nopatheticcards.mp3')
    
    os.system('exrightleg.png')
    playsound('spawn.mp3')

    os.system('exleftleg.png')
    playsound('spawn.mp3')

    os.system('exrightarm.png')
    playsound('spawn.mp3')

    os.system('exleftarm.png')
    playsound('spawn.mp3')

    os.system('exhead.png')
    playsound('spawn.mp3')

    for proc in psutil.process_iter():
        if proc.name() == "Microsoft.Photos.exe":
            proc.kill()

    os.system('unstopable.png')
    playsound('unstopable.mp3')

    time.sleep(0.25)
                    
    os.system('obliterate.gif')
    playsound('exodia-obliterate.mp3')
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
