import sys, time, random
import os
import configparser
import subprocess


class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)
usocietylogo = color_random[0] + '''
       ██╗   ██╗███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗
       ██║   ██║██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
       ██║   ██║███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ 
       ██║   ██║╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  
       ╚██████╔╝███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   
        ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝   
                                                            

'''
#Clearning Screen
def clr_src():
    os.system('clear')

#Configuration
installDir = os.path.dirname(os.path.abspath(__file__)) + '/'
configFile = installDir + "/usociety.cfg"
clr_src()
print(installDir)
config = configparser.RawConfigParser()
config.read(configFile)


class usociety:

    def completed(self):
        input("\nCompleted, press Enter to go back")
    
        self.__init__()
    
    def __init__(self):
        clr_src()
        print(usocietylogo + color.RED + '''
       !--------------- Coded By UmerFarid ---------------!
       !--------  GitHub.com/MrRobot-hub/usociety --------!
       !------------  usociety36711@gmail.com ------------!
  
       ''' + color.END + '''

       [1]-Scan Your Whole System
       [2]-Check Rootkits
       [0]-EXIT\n
     ''')
        usocietyPrompt = color.OKBLUE + "usociety:~#" + color.END
        prompt = os.system
        
        choice = input(usocietyPrompt)
        if choice == "1":
            prompt("echo " + color.RED + "[◉]" + color.END + " System scanning.. \n")
            time.sleep(2.5)
            os.system("lynis audit system")
        elif choice == "2":
            prompt("echo " + color.RED + "[◉]" + color.END + " Checking for Updates.. \n")
            time.sleep(1)
            os.system("apt install rkhunter;clear")
            prompt("echo " + color.RED + "[◉]" + color.END + " Checking Rootkits.. \n")
            time.sleep(2.5)
            os.system("rkhunter --check")

        elif choice == "0":
            with open(configFile, 'wb') as configfile:
                config.write(configfile)
            sys.exit()
        elif choice == "\r" or choice == "\n" or choice == "" or choice == " ":
            self.__init__()
        else:
            try:
                print(os.system(choice))
            except:
                pass
        self.completed()
if __name__ == "__main__":
    try:
        usociety()
    except KeyboardInterrupt:
        print("Finishing up .. \n")
        time.sleep(0.25)
