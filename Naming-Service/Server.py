import Pyro4

@Pyro4.expose
class Greeting:
    def greeting (self):
        return  'Hello World!'


daemon = Pyro4.Daemon()

uri = daemon.register(Greeting)
ns = Pyro4.locateNS()
ns.register('obj', uri)
print(uri)

daemon.requestLoop()