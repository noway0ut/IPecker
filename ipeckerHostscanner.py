import socket
import pyfiglet
from colorama import init, Fore, Back, Style
import os


while True:  
    try:
    


        init(autoreset=True)

        bold_start = "\033[1m"
        bold_end   = "\033[0m"

        banner = """                                                                                                     
                          ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  
                         ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                          ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  
                                 ██╗██████╗ ███████╗ ██████╗██╗  ██╗███████╗██████╗ 
                                 ██║██╔══██╗██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
                                 ██║██████╔╝█████╗  ██║     █████╔╝ █████╗  ██████╔╝
                                 ██║██╔═══╝ ██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
                                 ██║██║     ███████╗╚██████╗██║  ██╗███████╗██║  ██║
                                 ╚═╝╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                          ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  
                         ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
                          ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  
        """
        inf = """                                               
                                               --Hostscanner Tool--
                                                  Author : Emre Ü. 
                                                       V1.0
        """

        print(Fore.BLUE  + banner)

        print(Fore.LIGHTBLUE_EX + inf)

        q1 = input("Do you want to write to text (Y/N): ")

        if q1 == "y":

            filename = input("Filename : ")
            ipst1 = input("IP Start : ")
            ipst2 = ipst1.split(".")    
            dot = '.'
            ipaddrst = ipst2[0],ipst2[1],ipst2[2],ipst2[3]

            ipend1 = input("IP End : ")
            ipend2 = ipend1.split(".")

            ipaddrend = ipend2[0],ipend2[1],ipend2[2],ipend2[3]

            for cnvrt in range(int(ipaddrst[3]), int(ipaddrend[3])):

                firstthree = ipst2[0],ipst2[1], ipst2[2]
                proc1 = '.'.join(firstthree)
                proc2 = str(proc1)+"."+str(cnvrt)
                transform = str(proc2)
                file = open("./"+filename+".txt","a+")
                hostname = socket.getfqdn(transform)

                file.write("\nIP address : "+transform)
                file.write("   |--Hostname : "+hostname+"\n")

        elif q1 == "n":

            ipst1 = input("IP Start : ")
            ipst2 = ipst1.split(".")    
            dot = '.'
            ipaddrst = ipst2[0],ipst2[1],ipst2[2],ipst2[3]

            ipend1 = input("IP End : ")
            ipend2 = ipend1.split(".")

            ipaddrend = ipend2[0],ipend2[1],ipend2[2],ipend2[3]

            for cnvrt in range(int(ipaddrst[3]), int(ipaddrend[3])):

                firstthree = ipst2[0],ipst2[1], ipst2[2]
                proc1 = '.'.join(firstthree)
                proc2 = str(proc1)+"."+str(cnvrt)
                transform = str(proc2)
                hostname = socket.getfqdn(transform)

                print("\nIP address : " + Fore.GREEN +transform)
                print("   |--Hostname : " + Fore.RED +hostname+"\n")
    
    except:
        KeyboardInterrupt("Returning...")
        os.system("cls")  
