import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode("\n[*]Python Calculator\n[*]L : Log | S : Square Root | E : Exponential\n[*]How To Use\n[*]Ex: S 2"))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        try:
            operation, value = data.split()
            op = str(operation)
            num = float(value)

            if op[0] == 'L' or 'l':
                op = 'Log'
                answer = math.log10(num)
            elif op[0] == 'S' or 's':
                op = 'Square root'
                answer = math.sqrt(num)
            elif op[0] == 'E' or 'e':
                op = 'Exponential'
                answer = math.exp(num)
            else:
                answer = ('[*]Wrong Operation Try Again....\n\tEx: L/S/E "number"')

            message = (str(op) + '(' + str(num) + ') = ' + str(answer))
            print ('[*]Calculation done....\n')
        except:
            print ('[*]Invalid...')
            message = ('[*]Invalid... Use L/S/E operation')

        if not data:
           break

        s_sock.send(str.encode(message))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8895))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('[*]socket error')

            except Exception as e:
                print("[*]an exception occurred!")
                print(e)
                sys.exit(1)
    finally:
           s.close()

