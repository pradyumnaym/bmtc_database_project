import os
folder="FINALLY"
for i in os.listdir():
    if(str(i).__contains__(".") and not str(i).__contains__(".py") ):
        os.rename(i,"4F13"+i)