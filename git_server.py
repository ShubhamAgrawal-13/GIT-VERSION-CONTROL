#!/usr/bin/python3
import socket      
import os
import time             

port = 6005                   
s = socket.socket()            
host = socket.gethostname()     
s.bind((host, port))            
s.listen(5)                     

print ('Server listening....')

path=os.getcwd()+"/server"

if(not os.path.exists(path)):
	os.mkdir(path)

while (True):
    conn, addr = s.accept()    
    print('Got connection from', addr)
    data = conn.recv(1024).decode('utf-8')
    print('Server received', repr(data))
    conn.send(b'3')
    v_no=str(conn.recv(1024).decode('utf-8'))
    conn.send(b'3')
    filename=str(conn.recv(1024).decode('utf-8'))
    conn.send(b'3')
    size=conn.recv(1024).decode('utf-8')
    # conn.send(b'3')
    time.sleep(1)
    v_no_path=path+"/"+str(v_no)
    if(not os.path.exists(v_no_path)):
    	os.mkdir(v_no_path)
    filename=v_no_path+"/"+filename
    print(filename)
    f=open(filename, 'wb')
    size=int(size)
    print(size)
    print ('file opened'+filename)
    while (size>0):
    	print('receiving data...')
    	data = conn.recv(1024)
    	if(not data):
    		break
    	f.write(data)
    	size-=len(data)
    	print(len(data))
    f.close()
    conn.send(b'done')
