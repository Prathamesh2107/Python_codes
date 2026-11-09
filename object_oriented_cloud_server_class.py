class CloudServer:

    def __init__(self, name, cpu, memory):

        self.name = name
        self.cpu = cpu
        self.memory = memory

    def show_details(self):

        print("\nServer:", self.name)
        print("CPU:", self.cpu, "%")
        print("Memory:", self.memory, "%")

    def check_health(self):

        if self.cpu >= 90 or self.memory >= 90:
            print("Server Health: CRITICAL")

        else:
            print("Server Health: HEALTHY")


server1 = CloudServer("Web-Server", 95, 90)
server2 = CloudServer("Database", 15, 42)

server1.show_details()
server1.check_health()

server2.show_details()
server2.check_health()