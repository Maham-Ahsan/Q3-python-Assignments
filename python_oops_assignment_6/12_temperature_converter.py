class TemperatureConverter:
    def __init__(self, temperature):
        self.temperature = temperature

    def convert_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32
    
    
print(TemperatureConverter(20).convert_to_fahrenheit())