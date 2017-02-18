# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:21:45 2017

@author: hp
"""

import functions


toMob = ''
username = ''
password = ''

while True:
   if functions.is_connected() == False:      # no internet connection
      functions.time.sleep(60)
      continue
   elif functions.is_connected() == True:
      # sending sms
       msg= functions.get_score() 
       if msg == 'NO':
          quit()
       ls =  functions.sms(username,password)               
       if ls.send(toMob,msg) == False:
           print("sms nai gya")
           functions.time.sleep(60)
           continue
       else:
           print("sent!!!! sleeping...")
           functions.time.sleep(600)
          