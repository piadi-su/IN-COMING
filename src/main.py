import os

import time
import ip_analysis
import username_search
import get_ip_url
import url_state

#main functions

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    while True:

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
        choice_1 = input("->choice: ")



        if choice_1 == "1":
            username_search.run()

        elif choice_1 == "2":
            ip_analysis.run()

        elif choice_1 == "3":
            get_ip_url.run()

        elif choice_1 == "4":
            url_state.run()



        elif choice_1 == "0":
            clear()
            print("bye bye!")
            break

        else:
            print("chose one of the options!")
        
        input("click something to continue...")
        clear()

if __name__ == "__main__":
    main()
