import socket
s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
print("Processes : \n 1) quit \n 2) read \n 3) Receive \n 4) Transfer \n 5) append")
while True:
    command = input("Enter command : ")
    if command == "quit":
        break
    elif command == "read":
        filename = input("Enter the name of file being read : ")
        doc = open(filename,'r')
        print(doc.read())
    elif command == "Receive":
        filename = input("Enter the name of file to recieve data: ")
        doc = open(filename,'ab')
        doc_data = s.recv(1024)
        doc.write(doc_data)
        print("File has been received succesfully...")
    elif command == "Transfer":
        filename = input("Input the name of the file to transfer data: ")
        doc = open(filename,'rb')
        doc_data = doc.read(1024)
        s.send(doc_data)
        print("Data has been sent....")
    elif command == "append":
        filename = input("Input the name of the file: ")
        doc = open(filename,'w')
        L=input("Enter data: ")
        doc.writelines(L)

s.close()
