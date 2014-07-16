import user

# Representacion de un Shell
class Shell():
    def __init__(self, password,intrHandler):
        self.users = []
        self.programs ={"loggin" : self.loggin,
                        "whoIam" : self.whoIam,
                        "addUser" : self.addUser,
                        "changePassword" : self.changePassword,
                        "setAsAdmin" : self.setAsAdmin,
                        "ps" : self.ps,
                        "thatProcessIsRunning" : self.thatProcessIsRunning,
                        "FIFOImplement" : self.FIFOImplement,
                        "RRImplement" : self.RRImplement,
                        "PriorityImplement" : self.PriorityImplement,
                        "exit" : self.exit
                        }
        self.interruptionHandler = intrHandler
        self.interruptionHandler.setShell(self)
        self.users.append(user.AdministratorUser("Root",password))
        self.currentUser = None
        self.isRun = False

    def startUp(self):
        self.isRun = True
        self.FIFOImplement()
        presentation = open("./presentacion",'r')
        print(presentation.read())
        presentation.close()
        statePrompt = " >> "
        self.loggin()
        while self.isRun:
            entrada = raw_input(self.currentUser.getName() + statePrompt)
            try:
                p = self.programs[entrada]
                p()
            except:
                self.runCommand(entrada)