# import socket
#
# sock = socket.socket()
#
# HOST=""
# PORT = 9090
#
#
# sock.bind((HOST, PORT))
# sock.listen(1)
# conn, addr = sock.accept()
# print(f'{addr} connected address')
#
# while True:
#     data= conn.recv(1024)
#     if not data:
#         break
#     conn.send(data.upper())
#
# conn.close()
from subprocess import Popen, CREATE_NEW_CONSOLE
import os
process_list = [] #coR 6Ay
while True:
    user = input("3anycTuTb 10 KnMeNTOB (start) / 3akpuTb KnMENTOB (close) / BuRTH (quit) ")
    if user =="quit": #ecnn nonb3oBaTenb BBen quit, MKn:
        break
    elif user =='start': #ecnn nonb30Barenb BBen start, TO sanyckaem mpouecco B KOHCOnI
        for _ in range (10):
            process_list.append(Popen('python client.py', creationflags=CREATE_NEW_CONSOLE)) #CREATE_NEW_CONSOLE - s OBO
            print(' 3anyueo 10 KMEHTOB')
    elif user == 'close': #ecnu nonb3oBatenb BBen close, TO Aponaem npouecco
        for process in process_list:
            process.kill()
            process_list.clear()