import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1' #obs:enquanto estava apenas '' n funcionou, apenas depois que
                                                    #especificou o host 127...
porta = 8291

s.connect((host, porta))
dados = s.recv(1024)
print(dados.decode('ascii'))
