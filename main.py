import os
import subprocess
import requests
import socket
import time

import ip_analysis
import username_search

#main functions



while True:



      time.sleep(2)
      print("")
      print("""
      ██╗███╗   ██╗       ██████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
      ██║████╗  ██║      ██╔════╝██╔═══██╗████╗ ████║██║████╗  ██║██╔════╝ 
      ██║██╔██╗ ██║█████╗██║     ██║   ██║██╔████╔██║██║██╔██╗ ██║██║  ███╗
      ██║██║╚██╗██║╚════╝██║     ██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
      ██║██║ ╚████║      ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
      ╚═╝╚═╝  ╚═══╝       ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ """)


      print("""
            1. username search
            2. IP analysis 
            0. exit """)
      choise_1 = input("->choise: ")



      if choise_1 == "1":
            username_search.run()

      elif choise_1 == "2":
            ip_analysis.run()

      elif choise_1 == "0":
          break

      else:
          print("chose one of the options!")


