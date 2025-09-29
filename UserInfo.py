# This is for storing Data of User Like user language or other

class userData():
    info = {
        # Change This According to You!
        "name" : "None", # your name
        "age" : "None", # Your Age
        "class" : "None", # Your Class
        "goal" : "None", # Your Goal
        "language" : "None" # Your language For This Model
        # Currently Hindi and English Supported For Other Go to vosk official site and download your desire Model and run that only need to change path
        # and change your current language now you are ready for it!
    }

    def giveInfo(self, arg : str = "name"):
        return self.info[arg]
        
        

if __name__ == "__main__":

    data = userData()
    print(data.info)

    print(data.giveInfo("goal"))
