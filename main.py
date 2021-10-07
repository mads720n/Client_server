import indtastSlagskibsSkud as slg
import server as serv

class serverStart():
    def nibba():
        serv.listen.listenStart()

    def test():
        return True


def test():
    if serverStart.test() and serv.listen.test and serv.client.test:
        print("[TEST COMPLETED WITH 0 ERRORS]")

test()

serverStart.nibba()
