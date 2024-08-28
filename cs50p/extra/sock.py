import socket


class MySocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def listen(self, host, port):
        try:
            self.sock.bind((host, port))
            self.sock.listen()
        except OSError as e:
            self.sock.close()
            self.sock = None
            raise e

    def connect(self, host, port):
        try:
            self.sock.connect((host, port))
        except OSError as e:
            self.sock.close()
            self.sock = None
            print(e)
            return

    def do_send(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def do_receive(self):
        chunks = []
        conn, self.address = self.sock.accept()
        print(self.address)
        with conn:
            print('Connected to:', self.address)
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    print("done?")
                    break
                chunks.append(chunk)
        return b''.join(chunks)
