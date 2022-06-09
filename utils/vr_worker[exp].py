# The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
# The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
# Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
# All such material is used with the permission of the owner.
# All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
# All Rights Reserved.

import asyncore
import asynchat
import logging
import socket
import threading

from concurrent.futures import ProcessPoolExecutor

packet_terminator = '\nEND_TRANSMISSION\n\n'
socket_obj = None
address = ('localhost', 5959)

def start():
    asyncore.loop()
    print("started loop")

def init_thread(run):
    new_thread = threading.Thread() 
    new_thread.run = run
    new_thread.start()

class EchoServer(asyncore.dispatcher):
    
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.address = self.socket.getsockname()
        self.listen(1)
        print ("server listening!")
        return

    def handle_accept(self):
        client_info = self.accept()
        socket_obj = EchoServerHandler(sock=client_info[0])
        return
    
    def handle_close(self):
        self.close()


class EchoServerHandler(asynchat.async_chat):
    
    def __init__(self, sock):
        self.received_data = [] 
        self.connected = False
        self.cmd_ops = {"TERM" : [self.close_when_done,[]]} 
        asynchat.async_chat.__init__(self, sock)
        self.process_data = self._process_data 
        self.set_terminator(packet_terminator)
        return

    def handle_connect(self):
        self.connected = True

    def handle_close(self):
        self.connected = False
        self.close()

    def collect_incoming_data(self, data):
        
        print(data)
        self.received_data.append(data)

    def found_terminator(self):
        
        self.process_data()
        return
    
    def _process_data(self):
        """We have the full ECHO command"""
        data = ''.join(self.received_data)
        data = data.split(' net_packet: ')
        self.received_data = [] 
        if self.cmd_ops.has_key(data[0]) and len(data) == 1: self.cmd_ops[data[0]][0](*self.cmd_ops[data[0]][1]) 
        elif self.cmd_ops.has_key(data[0]) and len(data) > 1: self.cmd_ops[data[0]][0](data[1], *self.cmd_ops[data[0]][1])
        else: pass

    def send_data(self, cmd, data):
        test = str.encode(cmd.upper() + " net_packet: " + data + packet_terminator)
        print(test)
        print(type(test))
        self.push(test)



class EchoClient(asynchat.async_chat):
    
    def __init__(self, host, port):

        self.received_data = [] 
        self.connected = False
        self.cmd_ops = {"TERM" : [self.close_when_done,[]]} 
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_terminator(packet_terminator)
        self.process_data = self._process_data
        self.connect((host, port))
        return

    def handle_connect(self):
        self.connected = True
        print("client connected!")

    def handle_close(self):
        self.connected = False
        self.close()        
    
    def collect_incoming_data(self, data):
        print(data)
        self.received_data.append(data)

    def found_terminator(self):
        self._process_data()
        return

    def _process_data(self):
        print(self.received_data)
        data = ''.join(self.received_data)
        data = data.split(' net_packet: ')
        print(data)
        self.received_data = [] 
        if self.cmd_ops.has_key(data[0]) and len(data) == 1: self.cmd_ops[data[0]][0](*self.cmd_ops[data[0]][1]) 
        elif self.cmd_ops.has_key(data[0]) and len(data) > 1: self.cmd_ops[data[0]][0](data[1], *self.cmd_ops[data[0]][1])
        else: pass

    def send_data(self, cmd, data):
        self.push(cmd.upper() + " net_packet: " + data + packet_terminator)

if __name__ == "__main__":
    socket_obj = EchoClient(address[0], address[1])
    start()
