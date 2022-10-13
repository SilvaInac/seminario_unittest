from random import seed
from random import random

class Windtunnel():
  __car = None

  def __init__(self, car):
    self.__car = car
    car.start_engine()

  def get_drag_coefficient(self):
    model_number = [ord(c) for c in self.__car.get_model()]
    year_number = [ord(c) for c in self.__car.get_year()]
    color_number = [ord(c) for c in self.__car.get_color()]

    rand_seed = sum(model_number) + sum(year_number) + sum(color_number)

    seed(rand_seed)
    return random()