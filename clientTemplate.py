# 
# Import socket library and Hash(MD5) library
#
from socket import *
import hashlib
import time
import os
#
# Generate md5 hash function
#
def generate_md5_hash (file_data):
    md5_hash = hashlib.md5(file_data)
    f_id = md5_hash.hexdigest()
    return str(f_id)
def check(data):
    received=clientSocket.recv(1024).decode("ascii")
    if(data==received):
        print("success")
    else:
        print("fail")
def findfile():
    clientSocket.send("SHOW_FILES".encode("ascii"))
    msg=None
    available=[]
        
    while msg!="Done":
         msg=clientSocket.recv(1024).decode("ascii")
         available.append(msg)
    return available[:-1]
    

    
    
    
        
        

# 
# Define Server URL and PORT
#
serverPort = 9999
serverURL = "localhost"
# 
# Create TCP socket for future connections
#
clientSocket = socket(AF_INET, SOCK_STREAM)
# 
# Connect the client to the specified server
#
clientSocket.connect((serverURL, serverPort))
print("Client connected to server: " + serverURL + ":" + str(serverPort))
while True:
    data=input("enter input 1)SHOW_FILES 2)UPLOAD 3)DOWNLOAD")
    if(data=="SHOW_FILES"):
        file=findfile()
        print(file)
        break
        


            
            
    elif(data=="UPLOAD"):
        clientSocket.send(data.encode("ascii"))
        print(clientSocket.recv(1024).decode("ascii"))
        file=input()
        clientSocket.send(file.encode())
        print(clientSocket.recv(1024).decode("ascii"))
        filename=file.split(";")[0]
        with open(filename,"rb") as f:
            while True:
                data=f.read(1024)
                if not data:
                    break
                clientSocket.send(data)
                md5=generate_md5_hash(data)
            clientSocket.send("EOF".encode("ascii"))
        check(md5)
        break
    elif(data=="DOWNLOAD"):
        clientSocket.send("DOWNLOAD".encode("ascii"))
        print(clientSocket.recv(1024).decode("ascii"))
        clientSocket.send("8f5cc27b60b2336b0a0f6ccad36e9d27".encode("ascii"))
        filepath=os.path.join("clientdata", "downloadedfile"+".gif") 
        with open(filepath,"wb") as f:
            while True:
                data=clientSocket.recv(1024)
                
                if (data ==("EOF".encode("ascii"))):
                    break
                else:
                    f.write(data)
                    md5=generate_md5_hash(data)
        if(md5=="8f5cc27b60b2336b0a0f6ccad36e9d27"):
            print("success")
        else:
            print("fail")
            
                    
            
            f.close()
        break
        
    
       

        
        

