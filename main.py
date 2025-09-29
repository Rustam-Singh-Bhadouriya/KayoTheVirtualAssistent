"""

    This is for public use and study purpose with MIT LICENSE. 
    NOTE = There is no guarantie with model for any curroption after modifing it, but without modify it gives
    warrenty also

Main page For you our model with rich user request data

"""
from UserInfo import userData
from voices import  tell, listen
import gemini
from web import get_article
# import deepseek
Info = userData()
# print(infor.info)

def SetupAuto():
    print("Checking User Info.....")
    for items,  value in Info.info.items():
        if(value == None):
            print(f"{items} is Empty, Go to UserInfo.py and change info dict")
            return

    print("Process Done!")
    print(f"Welcome {Info.info["name"]}")

    while True:
        UserInput : str= listen(Info.info["language"])
        print("Say `wiki and any article name` for asking wikipedia: ")
        if UserInput.lower() == "exit":
            break
        if "wiki" in UserInput.lower():
            article = get_article(UserInput[4:])
            tell(article)

        else:
            response =  gemini.generate(UserInput, Info.info["language"])
            tell(response)

    print("Byee, See You Again <3")



def manualSetup(lang : str = "en"):
    print("Initializing Kayo AI Bot.....")
    while True:
        UserInput : str= listen(language=lang)
        if UserInput.lower() == "exit":
            break
        if "wiki" in UserInput.lower():
            article = get_article(UserInput[4:])
            tell(article)

        else:
            response =  gemini.generate(UserInput, lang)
            tell(response)

    print("Byee, See You Again <3")





def setup():
    tell("Initializing kayo")
    info_ask = input("Do you Wanna Share Your Information (y/n): ")
    match info_ask.lower():
        case "y":
            print("Welcome To AI World")
            SetupAuto()

        case "n":
            print("en => english\n hi => hindi\n en-in => indian english")
            language = input("Enter Language by seeing up: ")
            manualSetup(language)

        case _ :
            print("Enter y/n")
            setup()



if __name__ == "__main__":
    setup()