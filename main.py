import os
import subprocess
import requests
import socket
import time

import ip_analysis
import username_search
import get_ip_url
import url_state

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
            3. get the ip of a url
            4. url up? 
            0. exit """)
      choise_1 = input("->choise: ")



      if choise_1 == "1":
            username_search.run()

      elif choise_1 == "2":
            ip_analysis.run()

      elif choise_1 == "3":
           get_ip_url.run()
      
      elif choise_1 == "4":
           url_state.run()
           
           

      elif choise_1 == "0":
          break

      else:
          print("chose one of the options!")


