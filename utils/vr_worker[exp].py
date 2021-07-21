# REFERENCES:
# https://pymotw.com/2/asynchat/
# tuple unpacking https://stackoverflow.com/questions/1993727/expanding-tuples-into-arguments

import asyncore
import asynchat
import logging
import socket
import threading #would multiprocessing be better?

from concurrent.futures import ProcessPoolExecutor

packet_terminator = '\nEND_TRANSMISSION\n\n'
socket_obj = None
address = ('localhost', 5959)

def start():
    asyncore.loop()
    print("started loop")

def init_thread(run):
    new_thread = threading.Thread() # create a new thread object.
    new_thread.run = run
    new_thread.start()
    #process_executor = ProcessPoolExecutor(max_workers=1)
    #process_executor.submit(run)

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
        # Called when a client connects to our socket
        client_info = self.accept()
        socket_obj = EchoServerHandler(sock=client_info[0])
        # We only want to deal with one client at a time,
        # so close as soon as we set up the handler.
        # Normally you would not do this and the server
        # would run forever or until it received instructions
        # to stop.
        #self.handle_close()
        return
    
    def handle_close(self):
        self.close()


class EchoServerHandler(asynchat.async_chat):
    
    def __init__(self, sock):
        self.received_data = [] #socket buffer
        self.connected = False
        self.cmd_ops = {"TERM" : [self.close_when_done,[]]} #dict stores packet command, corresponding function call in mem, and the number of arguments needed to be passed
        asynchat.async_chat.__init__(self, sock)
        self.process_data = self._process_data #allows for switching data processing operators
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
        self.received_data = [] #empty buffer
        if self.cmd_ops.has_key(data[0]) and len(data) == 1: self.cmd_ops[data[0]][0](*self.cmd_ops[data[0]][1]) #call stored function, pass stored arguments from tuple
        elif self.cmd_ops.has_key(data[0]) and len(data) > 1: self.cmd_ops[data[0]][0](data[1], *self.cmd_ops[data[0]][1])
        else: pass

    def send_data(self, cmd, data):
        test = str.encode(cmd.upper() + " net_packet: " + data + packet_terminator)
        print(test)
        print(type(test))
        self.push(test)



class EchoClient(asynchat.async_chat):
  
    # Artificially reduce buffer sizes to illustrate
    # sending and receiving partial messages.
    #ac_in_buffer_size = 64
    #ac_out_buffer_size = 64
    
    def __init__(self, host, port):
        #self.message = message
        self.received_data = [] #socket buffer
        self.connected = False
        self.cmd_ops = {"TERM" : [self.close_when_done,[]]} #dict stores packet command, corresponding function call, and the number of arguments needed to be passed
        #self.logger = logging.getLogger('EchoClient')
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_terminator(packet_terminator)
        self.process_data = self._process_data #allows for switching data processing operators
        #self.logger.debug('connecting to %s', (host, port))
        self.connect((host, port))
        return

    def handle_connect(self):
        self.connected = True
        print("client connected!")

    def handle_close(self):
        self.connected = False
        self.close()        
    
    def collect_incoming_data(self, data):
        """Read an incoming message from the client and put it into our outgoing queue."""
        print(data)
        self.received_data.append(data)

    def found_terminator(self):
        """The end of a command or message has been seen."""
        self._process_data()
        return

    def _process_data(self):
        """We have the full ECHO command"""
        print(self.received_data)
        data = ''.join(self.received_data)
        data = data.split(' net_packet: ')
        print(data)
        self.received_data = [] #empty buffer
        if self.cmd_ops.has_key(data[0]) and len(data) == 1: self.cmd_ops[data[0]][0](*self.cmd_ops[data[0]][1]) #call stored function, pass stored arguments from tuple
        elif self.cmd_ops.has_key(data[0]) and len(data) > 1: self.cmd_ops[data[0]][0](data[1], *self.cmd_ops[data[0]][1])
        else: pass

    def send_data(self, cmd, data):
        self.push(cmd.upper() + " net_packet: " + data + packet_terminator)

if __name__ == "__main__":
    socket_obj = EchoClient(address[0], address[1])
    start()
