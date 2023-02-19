
class Colors:
    RED = ""
    BLUE = ""
    GREEN = ""
    RESET = ""

class Editor:
    def __init__(self, combos):
        self.combos = combos

    def replaceBadEncoding(self):
        #<!-- If a line is not utf-8 encoded, try to replace it --!>#
        pass

    def replaceDomain(self, whitelistDomains):
        #<!-- strip a line if the domain isn't in the whitelist --!>#
        pass

    def newSeparator(self, separator):
        #<!-- change the sep. to a new one --!>#
        pass

    def toDifferentFormat(self, emailPass = False):
        #<!-- if emailPass is set to True, replace user pass with email pass, otherwise, email to user/pass--!>#
        pass


def main():
    print(Colors.BLUE + """
    
     _   _                  _ _____    _ _ _             
    / \ | |_ ___  _ __ ___ (_) ____|__| (_) |_ ___  _ __ 
   / _ \| __/ _ \| '_ ` _ \| |  _| / _` | | __/ _ \| '__|
  / ___ \ || (_) | | | | | | | |__| (_| | | || (_) | |   
 /_/   \_\__\___/|_| |_| |_|_|_____\__,_|_|\__\___/|_|   
                                                         
    <Enter the number that corresponds to your choice>

    1. strip non UTF-8 characters
    2. replace the domain if it is not entered as a whitelist
    3. use a new separator
    4. format the combos differently (userPass->emailPass) etc

    """ + Colors.RESET)

    print("> ", end = "")
    choice = input("")

    edit = Editor([combo.strip("\n") for combo in open("combos.txt")])
    

if __name__ == "__main__":
    main()