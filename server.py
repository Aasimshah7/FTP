import socket
s = socket.socket()
print ("Socket successfully created")
port = 12345
s.bind(('127.0.0.1', port))
s.listen(5)
print ("socket is listening")
c, addr = s.accept()
print('Got connection from', addr)
print("Processes : \n 1) quit \n 2) read \n 3) Transfer \n 4) Receive \n 5) append")
while True:
    command = input("Enter command : ")
    if command == "quit":
        break
    elif command == "read":
        filename = input("Enter the name of file being read : ")
        doc = open(filename,'r')
        print(doc.read())
    elif command == "Transfer":
        filename = input("Enter the name of file to transfer data: ")
        doc = open(filename,'rb')
        doc_data = doc.read(1024)
        c.send(doc_data)
        print("Data has been sent....")
    elif command == "Receive":
        filename = input("Enter the name of file to receive data : ")
        doc = open(filename,'ab')
        doc_data = c.recv(1024)
        doc.write(doc_data)
        print("File has been received succesfully...")
    elif command == "append":
        filename = input("Input the name of the file: ")
        doc = open(filename,'w')
        L=input("Enter data: ")
        doc.writelines(L)
s.close()
