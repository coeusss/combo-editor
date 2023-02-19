
class Colors:
    RED = "\033[0;31m"
    BLUE = "\033[1;34m"
    GREEN = "\033[1;32m"
    RESET = "\033[0m"

class Editor:
    def __init__(self, combos):
        self.options = {"1": self.replaceBadEncoding, "2": self.replaceDomain, "3": self.newSeparator, "4": self.toDifferentFormat}
        self.combos = combos
        self.newCombos = []

    def writeFile(self):
        if len(self.newCombos) == 0:
            return

        #<!-- Erase the old file and write the new one --!>#
        erase = open("combos.txt", "w").close()
        writeFile = open("combos.txt", "a+")

        for combo in self.newCombos:
            writeFile.write(f"{combo}\n")
        
        writeFile.close()

        print(Colors.GREEN + f"[!] Wrote {len(self.newCombos)} {'combo' if len(self.newCombos) == 1 else 'combos'} to combos.txt." + Colors.RESET)

    def replaceBadEncoding(self, args):
        #<!-- If a line is not valid utf-8 encoded, try to replace it --!>#
        for combo in self.combos:
            #get rid of the separator dot & @
            newCombo = combo.replace(args[1], "")
            newCombo = newCombo.replace("@", "")
            newCombo = newCombo.replace(".", "")

            if newCombo.isalnum():
                self.newCombos.append(combo)

    def replaceDomain(self, args):
        #<!-- strip a line if the domain isn't in the whitelist --!>#
        for combo in self.combos:
            pass

    def newSeparator(self, args):
        #<!-- change the sep. to a new one --!>#
        old = args[1]
        new = args[2]

        for combo in self.combos:
            separated = combo.split(old)
            try:
                self.newCombos.append(f"{separated[0]}{new}{separated[1]}")
            except:
                print(Colors.RED + "[!] Separator given does not exist.")

    def toDifferentFormat(self, args):
        #<!-- if emailPass is set to True, replace user pass with email pass, otherwise, email to user/pass--!>#
        if "userPass->" in args[2]:
            print("Enter the Email Domain you want to use ", end = "")
            domain = input("> ")

            for combo in self.combos:
                combo = combo.split(args[1])
                self.newCombos.append(f"{combo[0]}{domain}{args[1]}{combo[1]}")

        elif "emailPass->" in args[2]:
            for combo in self.combos:
                combo = combo.split(args[1])
                username = combo[0].split("@")[0]
                self.newCombos.append(f"{username}{args[1]}{combo[1]}")




def main():
    print(Colors.BLUE + """
    
     _   _                  _ _____    _ _ _             
    / \ | |_ ___  _ __ ___ (_) ____|__| (_) |_ ___  _ __ 
   / _ \| __/ _ \| '_ ` _ \| |  _| / _` | | __/ _ \| '__|
  / ___ \ || (_) | | | | | | | |__| (_| | | || (_) | |   
 /_/   \_\__\___/|_| |_| |_|_|_____\__,_|_|\__\___/|_|   
                                                         
    <Enter the number that corresponds to your choice>

    1. strip non UTF-8 characters <currentSeparator>
    2. replace the domain if it is not entered as a whitelist <@gmail.com @yahoo.com>
    3. use a new separator <oldSeparator> <NewSeparator>
    4. format the combos differently <separator> <userPass->emailPass emailPass->userPass> 

    """ + Colors.RESET)

    print("> ", end = "")
    choice = input("")

    edit = Editor([combo.strip("\n") for combo in open("combos.txt")])
    edit.options[choice.split(" ")[0]](choice.split(" "))
    edit.writeFile()

if __name__ == "__main__":
    main()
