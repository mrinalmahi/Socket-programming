# 
# Import socket library and Hash(MD5) library
#
from socket import *
import hashlib
import os.path
#
# Generate md5 hash function
#
def generate_md5_hash (file_data):
    md5_hash = hashlib.md5(file_data)
    f_id = md5_hash.hexdigest()
    return str(f_id)


    
# 
# Define Server URL and PORT
#
serverPort = 9999
serverURL = "localhost"
serverpath= "serverdata"

# 
# Create TCP socket for future connections
#
serverSocket = socket(AF_INET, SOCK_STREAM)
# 
# Bind URL and Port to the created socket
#
serverSocket.bind((serverURL, serverPort))
# 
# Start listening for incoming connection (1 client at a time)
#
serverSocket.listen(2)
print("Server is listening on port: " + str(serverPort))

while True:
    # 
    # Accept incoming client connection
    #
    connectSocket, addr = serverSocket.accept()
    print("Client connected: " + str(addr))
    cmd=connectSocket.recv(1024).decode("ascii")
    if(cmd=="SHOW_FILES"):
        files=os.listdir('serverdata')
        if len(files)==0:
            msg="no files"
            connectSocket.send(msg.encode("ascii"))
            connectSocket.send('Done'.encode("ascii"))

        else:
             for f in files:
                connectSocket.send(f.encode("ascii"))
             connectSocket.send("Done".encode("ascii"))
             print("done")
                

        
    elif( cmd=="UPLOAD"):
        msg="Give filename and filesize"
        connectSocket.send(msg.encode("ascii"))
        file=connectSocket.recv(1024).decode("ascii")
        filesize=int(file.split(";")[1])
        msg="ready to receive file"
        connectSocket.send(msg.encode())
        filepath=os.path.join("serverdata", file+".gif") 
        with open(filepath,"wb") as f:
            while True:
                data=connectSocket.recv(1024)
                
                if (data ==("EOF".encode("ascii"))):
                    break
                else:
                    f.write(data)
                    md5=generate_md5_hash(data)
            
                    
            
            f.close()
        
        
        savefile=os.path.join("serverdata",md5+";"+file+".gif")
        if not os.path.isfile(savefile):
                    os.rename(filepath, savefile)
       
        connectSocket.send(md5.encode("ascii"))
    elif(cmd=="DOWNLOAD"):
        connectSocket.send("please send a file ID".encode("ascii"))
        data=connectSocket.recv(1024).decode("ascii")
        file=os.listdir("serverdata")
        for f in file:
            if data in f:
                download=f
        with open(os.path.join("serverdata",download),"rb") as d:
            while True:

                data=d.read(1024)
                if not data:
                    break
                connectSocket.sendall(data)
            connectSocket.send("EOF".encode())



        

       
        

       
        
        

        

    

        
        
        

        


    
    
            
      
    
    
    

 






    #close TCP connection
    connectSocket.close()