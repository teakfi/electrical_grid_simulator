import simpy
import itertools
from .area import Area
from .user import ElectricityUser
from .generator import PowerPlant

def produce_in_area(env, area):
    area.sort_electricity_providers()
    minimum_production = 0
    for provider in area.providers:
        minimum_production += provider.give_next_min_production()
    difference = area.demand.level - minimum_production
    if difference <= 0:
        for provider in area.providers:
            yield env.process(user.produce(area,provider.give_next_min_production()))
    else:
        for provider in area.providers:
            next_max = provider.give_next_max_production()
            next_min = provider.give_next_min_production()
            delta = next_max-next_min
            if delta <= difference:
                yield env.process(provider.produce(area, next_max))
                difference -= delta
            else:
                yield env.process(provider.produce(area, next_min+difference))
                difference = 0




def time_step(env, area):
    print(area.name)
    for i in itertools.count():
        yield env.timeout(1)
        for user in area.users:
            user.print_name()
            yield env.process(user.consume(area))
        area.show_demand()
        yield env.process(produce_in_area(env,area))
                