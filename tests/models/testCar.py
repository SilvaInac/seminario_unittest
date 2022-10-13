import unittest
from src.models.Car import Car

class CarTest(unittest.TestCase):
  def test_valid_car(self):
    model = 'Ford Focus'
    year = '2012/2013'
    color = 'Silver'

    car = car = Car(model=model, year=year, color=color)

    self.assertEqual(car.get_model(), model)
    self.assertEqual(car.get_year(), year)
    self.assertEqual(car.get_color(), color)
    
    self.assertTrue(car.get_is_clean())
    self.assertFalse(car.get_is_engine_running())