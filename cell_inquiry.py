"""
CELL INQUIRY PROJECT 

Ben & Kayaan
"""
import time


brain = [False, "Lungs"]
blood = [True, "Oxygen"]
lungs = [True, "Blood"]
heart = [True, ""]

while True:
    if brain[0]:
        lungs[0] = True
    else:
        lungs[0] = False
    print(brain)
    print(lungs)
    time.sleep(1)
