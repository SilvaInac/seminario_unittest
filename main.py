from models.Car import Car
from models.Windtunnel import Windtunnel

def main():
  model = input('Car model: ')
  year = input('Car year: ')
  color = input('Car color: ')

  car = Car(model=model, year=year, color=color)
  windtunnel = Windtunnel(car=car)

  print(car.to_string())
  print(f'Car drag coefficient: {windtunnel.get_drag_coefficient()}')

if __name__ == "__main__":
  main()
