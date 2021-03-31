try:
    import pyAesCrypt 
except ImportError:
    input("pip install pyAesCrypt")
    exit()
from os import stat, remove,path,getcwd,system
import json
from datetime import datetime
import hashlib
from lib.cripta import Delete_File
from lib.style import style
from getpass import getpass

# encryption/decryption buffer size - 64K
bufferSize = 1024 * 1024


def save_json(file):
    with open(file,"rb") as f:
        bytes = f.read() # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest();
    filename, file_extension = path.splitext(file)
    dizionario={}
    dizionario["time"]=str(datetime.now())
    dizionario["dir"]=str(getcwd())
    dizionario["size"]=str(stat(file+"aes").st_size)
    dizionario["estensione"]=file_extension
    dizionario["extension"]=file
    dizionario["hash256"]=readable_hash
    with open(file+".json", 'w') as fp:
        json.dump(dizionario, fp)





system("") #for colored console



while True:

    while True:
        try:
            scelta=int(input(style.GREEN +"1-EN,2-DE,3-EXIT,4-SCREEN CLEAN "))
            break
        except ValueError:
            print(style.RED+"error string in input")
            print(style.WHITE)


    print(style.WHITE)
   

    try:    
        if scelta==1:
            while True:
                file=input("File name ")
                if path.exists(file)==True:break
                else:
                    print(style.RED+"404 not found ")
                    print(style.WHITE)

            while True:
                password=getpass("give me the password ")
                password_conferma=getpass("retype ")
                if password_conferma == password:
                    password_conferma="jhrfhjfhhjt5rhjfgrthjrf"
                    del password_conferma
                    break
                else:
                    print(style.RED+"password not match ")
                    print(style.WHITE)



            with open(file, "rb") as fIn:
                with open(file+"aes", "wb") as fOut:
                    pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
            
            password="DGRGRGRFGRFGRGF"
            del password
            scelta=input("you want a json file with the details y/other ")
            if scelta=="y":
                save_json(file)
                
            scelta=input("do you want delete the decrypted file y/other ")
            if scelta=="y":
                Delete_File(file)
                remove(file)

            else:
                pass

        elif scelta==2:
            while True:
                file=input("File name ")
                if path.exists(file)==True:break
                else:
                    print(style.RED+"404 not found ")
                    print(style.WHITE)

            encFileSize=stat(file).st_size
            password=input("give me the password ")
            estensione=input("give me the extension of the output file [important] ")
            with open(file, "rb") as fIn:
                try:
                    with open(file+"decriptato."+estensione, "wb") as fOut:
                        pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
                except ValueError:
                    remove(file+"decriptato"+estensione)
            
            if path.exists(file+"decriptato"+estensione) is True:
                scelta=input("do you want delete the encrypted file y/other ")
                if scelta=="y":
                    remove(file)
                else:
                    pass

        elif scelta==3:
            input("press any key for exit")
            exit()

        elif scelta==4:
            system("cls")

        else:
            print(style.RED+"error")
            print(style.WHITE)
    except Exception as e:
        print(style.RED+str(e))
        print(style.WHITE)

    




