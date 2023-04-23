import Pyro4

@Pyro4.expose
class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 1.8 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) / 1.8
