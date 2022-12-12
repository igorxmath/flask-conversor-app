def tempconverter(measure, mconverted, datain):
    def Celsius_to_Kelvin_function(temp):
        return temp + 273.15

    def Celsius_to_Fahrenheit_function(temp):
        return (temp * 9/5) + 32

    def Fahrenheit_to_Celsius_function(temp):
        return (temp - 32) * 5/9

    def Fahrenheit_to_Kelvin_func(temp):
        return (temp - 32) * 5/9 + 273.15

    def Kelvin_to_Celsius(temp):
        return temp - 273.15

    def Kelvin_to_Fahrenheit(temp):
        return (temp - 273.15) * 9/5 + 32

    dict_of_func = {1: {3: Celsius_to_Kelvin_function, 2: Celsius_to_Fahrenheit_function}, 2: {1: Fahrenheit_to_Celsius_function, 3: Fahrenheit_to_Kelvin_func}, 3: {1: Kelvin_to_Celsius, 2: Kelvin_to_Fahrenheit}}

    return round((dict_of_func.get(measure)[mconverted](datain)), 2)