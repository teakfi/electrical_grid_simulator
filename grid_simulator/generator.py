import simpy

MIN_PRIORITY = 0
MAX_PRIORITY = 100

class PowerPlant(object):
    def __init__(self, env, name, priority, min_production, max_production, initial_production):
        self.env = env
        self.name = name
        self.max_production = max_production
        self.min_production = min_production
        self.previous_production = initial_production
        self.next_min = min_production
        self.next_max = max_production
        if priority < MIN_PRIORITY:
            priority=MIN_PRIORITY
        elif priority > MAX_PRIORITY:
            priority=MAX_PRIORITY
        self.priority = priority

            
    def print_name(self):
        print(self.name)
        
    def produce(self, area, production):
        self.previous_production = production
        print('Power plant ' + self.name + ' produced ' + str(production) + ' of energy')  
        if production > 0:
            yield area.demand.get(production)
        
    def give_next_min_production(self):
        return self.next_min
    
    def give_next_max_production(self):
        return self.next_max