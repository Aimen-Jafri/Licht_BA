# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:05:54 2023

@author: Aimen Jafri
"""


import time #module for time related functions
import board

# for I2C use:
from adafruit_as726x import AS726x_I2C
import adafruit_as726x
import smbus
import struct
from adafruit_bus_device.i2c_device import I2CDevice

class Sensor:
    def __init__(self):
        i2c = board.I2C()
        self.sensor = AS726x_I2C(i2c)
        self._integration_time = 2.8
        self.conversion_mode = self.sensor.MODE_2
        self.gain = 64
          
        time.sleep(1)
        self.int_times = [adafruit_as726x.integration_time(self,2.8),adafruit_as726x.integration_time(self,140),adafruit_as726x.integration_time(self,280),
                adafruit_as726x.integration_time(self,420),adafruit_as726x.integration_time(self,560),adafruit_as726x.integration_time(self,700)]
        
        self.sensor.integration_time = self.int_times[0]
        
            
    def measure(self):
        # Read the V, B, G, Y, O, R color (raw?) data.
        v = self.sensor.raw_violet()
        b = self.sensor.raw_blue()
        y = self.sensor.raw_yellow()
        g = self.sensor.raw_green()
        o = self.sensor.raw_orange()
        r = self.sensor.raw_red()
        #device_temp = self.sensor.temperature()
        return ["V", v],["B", b],["G", g],["Y", y],["O", o],["R", r]
           


        

       