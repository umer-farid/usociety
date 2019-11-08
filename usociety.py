import sys,os, configparser, datetime, platform


class color:
    RED = '\033[91m'
    END = '\033[0m'
    OKBLUE = '\033[94m'


installDir = os.path.dirname(os.path.abspath(__file__)) + '/'

configFile = installDir + "/usociety.cfg"
print(os.system('clear'))
print(installDir)

config = configparser.RawConfigParser()
config.read(configFile)
class usociety:

    def completed(self):
        input("Completed, click return to go back")
    
        self.__init__()
    

    def __init__(self):
#        print(os.system("clear"))
        print(color.RED + '''
       !--------------- Coded By UmerFarid ---------------!
       !--------  GitHub.com/MrRobot-hub/usociety --------!
       !------------  usociety36711@gmail.com ------------!
  
       ''' + color.END + '''
       1-Current Date & Time
       2-System Info
       0-EXIT\n
     ''')
        usocietyPrompt = color.OKBLUE + "usociety:~#" + color.END

        choice = input(usocietyPrompt)
        
        if choice == "1":
            print(datetime.datetime.now())
        elif choice == "2":
            print("Machine: " + platform.machine())
            print("Architecture: " + platform.architecture()[0])
            print("Node: " + platform.node())
            print("System: " + platform.system())


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
