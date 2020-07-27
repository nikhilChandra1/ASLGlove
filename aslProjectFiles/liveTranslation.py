
import keyboard
import subprocess


running = False
while True:
    if keyboard.is_pressed('s'):
        open('test.txt', 'w').close()
    if keyboard.is_pressed('p'):
        subprocess.run(["python", "euclidianTranslationAlgorithmJustTheWord.py"])
        
              
            
        
        
