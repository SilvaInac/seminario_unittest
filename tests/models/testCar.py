import unittest

from src.models.Car import Car

class CarTest(unittest.TestCase):

  # cada metodo de teste tem que ter o prefixo 'test_'

  def setUp(self):
    self.model = 'Ford Focus'
    self.year = '2012/2013'
    self.color = 'Silver'

  def test_valid_car(self):
    car = car = Car(model=self.model, year=self.year, color=self.color)

    self.assertEqual(car.get_model(), self.model)
    self.assertEqual(car.get_year(), self.year)
    self.assertEqual(car.get_color(), self.color)
    
    self.assertTrue(car.get_is_clean())
    self.assertFalse(car.get_is_engine_running())

  @unittest.expectedFailure
  def test_invalid_car(self):
    Car(model=self.model, year=self.year)