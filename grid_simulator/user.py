import simpy

class ElectricityUser(object):
    def __init__(self, env, name, consumption):
        self.env = env
        self.name = name
        self.consumption = consumption
        
    def print_name(self):
        print(self.name)
        
    def consume(self,area):
        if self.consumption > 0:
            yield area.demand.put(self.consumption)