'''
Created on 10/06/2014

@author: Fernando Martinotti
@author: Emmanuel Pericon
'''

import threading
from time import sleep

class Clock(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.observer= None

    def esperar(self):
        sleep(2)

    def run(self):
        while True:
            self.esperar()
            self.notificar()
            
    def cargarObserver(self, unCpu):
        self.observer = unCpu
        
    def notificar(self):
        self.observer.tick()
        
