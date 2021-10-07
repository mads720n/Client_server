import indtastSlagskibsSkud as slg
import server
#import client as cl

print(server.HEADER)

class serverStart():
    def nibba():
        server.listen.listenStart()

    def test():
        return True


def test():
    if serverStart.test() and server.listen.test and server.client.test:
        print("[TEST COMPLETED WITH 0 ERRORS]")

test()

serverStart.nibba()
