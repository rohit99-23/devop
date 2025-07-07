import os

'''
r = sr.Recognizer()
engine = pyttsx3.init()
'''

user = input("Enter your Username: ")
ip = input("Enter your IP Address: ")

'''
def speak(text):
    print(">>", text)
    engine.say(text)
    engine.runAndWait()

def get_voice_command():
    with sr.Microphone() as source:
        speak("Aap kya karna chahte hain? Command boliye.")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="en-IN").lower()
            print(f"User said: {command}")
            return command
        except:
            speak("Command samajh nahi aayi, dobara boliye.")
            return ""

'''
print(
    """
-------------------------------------------------------------
Welcome! this is the menu for Automate Linux basic commands
-------------------------------------------------------------

press 1. To Check Current Directory.
press 2. To Move any folder or directory.
press 3. To Check files or folder on that location
Press 4. To Create files
Press 5. To create folder 
Press 6. To remove file
Press 7. To Delete file Forcefully
Press 8. To open Notepad like Shell
Press 9. To enter data in file in Command line
Press 10. To check the data of a file
press 11. To echo command
Press 12. To run Date Command
Press 13. To run Calender command
Press 14. To know ip Address
Press 15. To Know who are you 
Press 16. To create new User 
Press 17. To run Python Interpreter
Press 18. To Close python Interpreter
Press 19. To run Simple python project
Press 20. To run Streamlit Project file
Press 21. To launch new container
Press 22. To see all running Container
Press 23. To see all running and closed container
Press 24. To delete all Container
Press 25. To Restart the container
Press 26. To Launch new Container with custom OS name
Press 27. To copy file from root to docker

"""
)


while(True):
 choice=input("Enter Your Choice: ")

 if choice== "1":
     print(os.system(f" ssh {user}@{ip} pwd"))

 elif choice == "2" :
     file=input("Enter the file name or directory ")
     os.system(f" ssh {user}@{ip} cd /{file}/")

 elif choice == "3":
     os.system(f" ssh {user}@{ip} ls")

 elif choice == "4":
     file1=input("Enter the file name ")
     os.system(f" ssh {user}@{ip}  touch {file1}")

 elif choice == "5":
     file2=input("Enter the Folder name ")
     os.system(f" ssh {user}@{ip}  mkdir {file2}")

 elif choice == "6":
     file3=input("Enter the file name ")
     os.system(f" ssh {user}@{ip}  rm {file3}")

 elif choice == "7":
     file4=input("Enter the file name ")
     os.system(f" ssh {user}@{ip}  rm -rf {file4}")

 elif choice == "8":
     file5=input("Enter the file name ")
     os.system(f" ssh {user}@{ip}  gedit {file5}")

 elif choice == "9":
     file6=input("Enter the file name ")
     os.system(f" ssh {user}@{ip}  vi {file6}")

 elif choice == "10":
     file7=input("Enter the file name ")
     os.system(f" ssh {user}@{ip}  cat {file7}")

 elif choice == "11":
     file8 = input("enter file name")
     os.system(f" ssh {user}@{ip}  echo {file8}")

 elif choice == "12":
    os.system(f" ssh {user}@{ip}  date") 

 elif choice == "13":
     os.system(f" ssh {user}@{ip}  cal")

 elif choice == "14":
    os.system(f" ssh {user}@{ip}  ifconfig")

 elif choice == "15":
     os.system(f" ssh {user}@{ip}  whoami")

 elif choice == "16":
     file9 = input("enter User name")
     os.system(f" ssh {user}@{ip}  useradd {file9}")
     os.system(f" ssh {user}@{ip}  passwd {file9}")

 elif choice == "17":
     os.system(f" ssh {user}@{ip}  python3" )

 elif choice == "18":
     os.system(f" ssh {user}@{ip}  exit()" )

 elif choice == "19":
     file9 = input("enter file name")
     os.system(f" ssh {user}@{ip}  python3 {file9}")

 elif choice == "20":
     file10 = input("enter file name")
     os.system(f" ssh {user}@{ip}  streamlit run {file10}")

 elif choice == "21":
     file11 = input("enter Image name")
     os.system(f" ssh {user}@{ip}  docker run -i {file11}")

 elif choice == "22":
     os.system(f" ssh {user}@{ip}  docker ps ")

 elif choice == "23":
     os.system(f" ssh {user}@{ip}  docker ps -a")

 elif choice == "24":
     os.system(f" ssh {user}@{ip}  docker rm $(docker ps -a -q)")

 elif choice == "25":
     file12 = input("enter container name")
     os.system(f" ssh {user}@{ip}  docker attach {file12}")

 elif choice == "26":
     file13 = input("enter Container name")
     file14 = input("enter image name")
     os.system(f" ssh {user}@{ip}  docker run -it --name {file13} {file14}")
     
 elif choice == "27":
     file15 = input("enter file name")
     file16 = input("enter container name")
     file17 = input("enter folder path")
     os.system(f" ssh {user}@{ip}  docker cp {file15} {file16} {file17}")

 else:
     print("Default option! choose from Menu")

 again = input("Would you like to go for another operation??" ).lower()
 	
 if again != "yes":
     print("""Exiting... Thank you for using the tool! 
	     Come Back Again! when you have to performed operation!
	 """)
 break
