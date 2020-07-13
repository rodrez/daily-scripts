import os 

os.system("git pull")

os.system("git add .")

commit_message = input("Enter your commit message. \n")
os.system('git commit -m"{commit_message}"')