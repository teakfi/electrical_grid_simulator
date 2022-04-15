import random
import simpy
from .user import ElectricityUser
from .generator import PowerPlant

class Area(object):
    def __init__(self, env, name):
        self.env = env
        self.name = name
        self.users = []
        self.demand = simpy.Container(env)
        self.providers = []
    
        
    def add_electricity_user(self, name,cap):
        factory = ElectricityUser(self.env,name,cap)
        self.users.append(factory)
        
    def list_electricity_users(self):
        for user in self.users:
            print(user.name)

    def add_electricity_provider(self, name,  priority, min_production, max_production, initial_production):
        power_station = PowerPlant(self.env,name,  priority, min_production, max_production, initial_production)
        self.providers.append(power_station)
        
    def list_electricity_providers(self):
        for provider in self.providers:
            print(provider.name)
            
    def sort_electricity_providers(self):
        random.shuffle(self.providers)
        self.providers = sorted(self.providers, key=lambda provider: provider.priority)
            
    def show_demand(self):
        print(self.demand.level)