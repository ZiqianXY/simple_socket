# coding=utf-8
import threading
from SocketServer import ThreadingMixIn, TCPServer
from SocketServer import StreamRequestHandler
from common_utils.util_log import log


# define multiThread class
class Server(ThreadingMixIn, TCPServer):
    pass


class StreamHandler(StreamRequestHandler):

    def handle(self):

        addr = self.request.getpeername()
        print 'Got connection from ', addr

        try:
            while True:
                data = self.rfile.readline().strip()
                cur_thread = threading.current_thread()
                output = "{}, {}: {}".format(cur_thread.name, self.client_address, data)
                print(output)
                if data == 'exit' or not data:
                    print('---*<client exit>*---!')
                    log.info(addr + 'self-closed.\n')
                    self.finish()
                    break

                elif data == '<end>':
                    print('<end>')
                    pass
                else:
                    self.wfile.write(data.upper())

        except Exception, err:
            log.error('connection of client {0} stopped! Error: {1}\n'.format(addr, err.args))

        finally:
            self.finish()


def start(host, port):
    server = None

    try:
        print('---**---Welcome!')
        log.info('---**---listening on {0}:{1}'.format(host, port))
        # bing to Host:port, using TCP
        server = Server((HOST, PORT), StreamHandler)
        server.serve_forever()

        # # Start a thread with the _server -- that thread will then start one
        # # more thread for each request
        # server_thread = threading.Thread(target=server.serve_forever)
        # # Exit the server thread when the main thread terminates
        # server_thread.daemon = True
        # server_thread.start()
        # print "Server loop running in thread:", server_thread.name
        # threading._sleep(100)

    except Exception, e:
        print(e.args)
        log.error('service failed to start! Error: {0}\n'.format(e.args))

    finally:
        print('---**---Bye!')
        if server:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    HOST, PORT = '10.0.2.15', 5555
    start(HOST, PORT)
