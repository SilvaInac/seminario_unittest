import unittest
from unittest.mock import MagicMock

from src.models.Windtunnel import Windtunnel
from src.models.Car import Car

class WindtunnelTest(unittest.TestCase):
  def test_windtunnel_mock(self):
    car_mock = Car(model=None, year=None, color=None)
    
    car_mock.get_model = MagicMock(return_value='Jeep Renegade')
    car_mock.get_color = MagicMock(return_value='Red')
    car_mock.get_year = MagicMock(return_value='2019')

    windtunnel = Windtunnel(car=car_mock)

    mock_drag_coef = windtunnel.get_drag_coefficient()
    expected_drag_coef = 0.4194976850845352

    self.assertEquals(mock_drag_coef, expected_drag_coef)
