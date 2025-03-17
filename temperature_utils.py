from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    pass  # remove pass statement and implement me
    celsius = (5/9) * (fahrenheit_temp-32)
    celsius = round(celsius, 2)
    return float(celsius)

def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    pass  # remove pass statement and implement me
    fahrenheit = (celsius_temp * (9/5)) + 32
    fahrenheit = round(fahrenheit, 2)
    return int(fahrenheit)

def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    pass  # remove pass statement and implement me
    #takes in 'temperatures' then dependant of input_unit_of_measurement converts to c/f/k
    #returns a tuple of tuples 'original temp' and 'converted temp'
    tuple = ()
    if input_unit_of_measurement == "f":
        # for i in temperatures:
        #     fchange = (temperatures, convert_to_fahrenheit(temperatures))
        #     tuple = list(tuple).append(fchange,)
        pass
    elif input_unit_of_measurement == "c":
        pass
    elif input_unit_of_measurement == "a":
        pass

def convert_to_kelvin(fahrenheit_temp: float) -> float:
    kelvin = (fahrenheit_temp-32)/1.8 + 273.15
    kelvin = round(kelvin, 2)
    return float(kelvin)