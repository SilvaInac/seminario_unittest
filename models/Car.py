class Car():
  __model = None
  __year = None
  __color = None

  __is_engine_running = False
  __is_clean = True

  def __init__(self, model, year, color):
    self.__model = model
    self.__year = year
    self.__color = color

  def get_model(self):
    return self.__model

  def get_year(self):
    return self.__year

  def get_color(self):
    return self.__color

  def get_is_engine_running(self):
    return self.__is_engine_running

  def get_is_clean(self):
    return self.__is_clean

  def start_engine(self):
    self.__is_engine_running = True

  def stop_engine(self):
    self.__is_engine_running = False
  
  def set_clean(self, isClean):
    self.__is_clean = isClean

  def to_string(self):
    is_clean_str = 'Yes' if self.__is_clean else 'No'
    is_engine_running_str = 'Yes' if self.__is_engine_running else 'No'

    return (
      f'=> Car:\n\t' +
        f'- Model: {self.__model}\n\t' +
        f'- Year: {self.__year}\n\t' +
        f'- Color: {self.__color}\n\t' + 
        f'- Is clean? {is_clean_str}\n\t' +
        f'- Is engine running? {is_engine_running_str}'
    )
