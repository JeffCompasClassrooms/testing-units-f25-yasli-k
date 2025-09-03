import unittest
from tempconverter import *

class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TemperatureConverter()

    # Celsius to Fahrenheit Tests (16 test cases)
    def test_celsius_to_fahrenheit_freezing(self):
        result = self.converter.celsius_to_fahrenheit(0)
        self.assertAlmostEqual(result, 32.0, places=10, msg="0°C should equal 32°F")

    def test_celsius_to_fahrenheit_boiling(self):
        result = self.converter.celsius_to_fahrenheit(100)
        self.assertAlmostEqual(result, 212.0, places=10, msg="100°C should equal 212°F")

    def test_celsius_to_fahrenheit_room_temp(self):
        result = self.converter.celsius_to_fahrenheit(20)
        self.assertAlmostEqual(result, 68.0, places=10, msg="20°C should equal 68°F")

    def test_celsius_to_fahrenheit_negative(self):
        result = self.converter.celsius_to_fahrenheit(-40)
        self.assertAlmostEqual(result, -40.0, places=10, msg="-40°C should equal -40°F")

    def test_celsius_to_fahrenheit_positive(self):
        result = self.converter.celsius_to_fahrenheit(37)
        self.assertAlmostEqual(result, 98.6, places=10, msg="37°C should equal 98.6°F")

    def test_celsius_to_fahrenheit_zero(self):
        result = self.converter.celsius_to_fahrenheit(0)
        self.assertAlmostEqual(result, 32.0, places=10, msg="0°C should equal 32°F")

    def test_celsius_to_fahrenheit_float_positive(self):
        result = self.converter.celsius_to_fahrenheit(25.5)
        self.assertAlmostEqual(result, 77.9, places=10, msg="25.5°C should equal 77.9°F")

    def test_celsius_to_fahrenheit_float_negative(self):
        result = self.converter.celsius_to_fahrenheit(-10.5)
        self.assertAlmostEqual(result, 13.1, places=10, msg="-10.5°C should equal 13.1°F")

    def test_celsius_to_fahrenheit_large_positive(self):
        result = self.converter.celsius_to_fahrenheit(200)
        self.assertAlmostEqual(result, 392.0, places=10, msg="200°C should equal 392°F")

    def test_celsius_to_fahrenheit_large_negative(self):
        result = self.converter.celsius_to_fahrenheit(-100)
        self.assertAlmostEqual(result, -148.0, places=10, msg="-100°C should equal -148°F")

    def test_celsius_to_fahrenheit_small_positive(self):
        result = self.converter.celsius_to_fahrenheit(0.5)
        self.assertAlmostEqual(result, 32.9, places=10, msg="0.5°C should equal 32.9°F")

    def test_celsius_to_fahrenheit_small_negative(self):
        result = self.converter.celsius_to_fahrenheit(-0.5)
        self.assertAlmostEqual(result, 31.1, places=10, msg="-0.5°C should equal 31.1°F")

    def test_celsius_to_fahrenheit_positive_integer(self):
        result = self.converter.celsius_to_fahrenheit(10)
        self.assertAlmostEqual(result, 50.0, places=10, msg="10°C should equal 50°F")

    def test_celsius_to_fahrenheit_negative_integer(self):
        result = self.converter.celsius_to_fahrenheit(-20)
        self.assertAlmostEqual(result, -4.0, places=10, msg="-20°C should equal -4°F")

    def test_celsius_to_fahrenheit_body_temp(self):
        result = self.converter.celsius_to_fahrenheit(36.6)
        self.assertAlmostEqual(result, 97.88, places=10, msg="36.6°C should equal 97.88°F")

    def test_celsius_to_fahrenheit_extreme_negative(self):
        result = self.converter.celsius_to_fahrenheit(-273.15)
        self.assertAlmostEqual(result, -459.67, places=10, msg="-273.15°C should equal -459.67°F")

    # Fahrenheit to Celsius Tests (16 test cases)
    def test_fahrenheit_to_celsius_freezing(self):
        result = self.converter.fahrenheit_to_celsius(32)
        self.assertAlmostEqual(result, 0.0, places=10, msg="32°F should equal 0°C")

    def test_fahrenheit_to_celsius_boiling(self):
        result = self.converter.fahrenheit_to_celsius(212)
        self.assertAlmostEqual(result, 100.0, places=10, msg="212°F should equal 100°C")

    def test_fahrenheit_to_celsius_room_temp(self):
        result = self.converter.fahrenheit_to_celsius(68)
        self.assertAlmostEqual(result, 20.0, places=10, msg="68°F should equal 20°C")

    def test_fahrenheit_to_celsius_negative(self):
        result = self.converter.fahrenheit_to_celsius(-40)
        self.assertAlmostEqual(result, -40.0, places=10, msg="-40°F should equal -40°C")

    def test_fahrenheit_to_celsius_positive(self):
        result = self.converter.fahrenheit_to_celsius(98.6)
        self.assertAlmostEqual(result, 37.0, places=10, msg="98.6°F should equal 37°C")

    def test_fahrenheit_to_celsius_zero(self):
        result = self.converter.fahrenheit_to_celsius(32)
        self.assertAlmostEqual(result, 0.0, places=10, msg="32°F should equal 0°C")

    def test_fahrenheit_to_celsius_float_positive(self):
        result = self.converter.fahrenheit_to_celsius(77.9)
        self.assertAlmostEqual(result, 25.5, places=10, msg="77.9°F should equal 25.5°C")

    def test_fahrenheit_to_celsius_float_negative(self):
        result = self.converter.fahrenheit_to_celsius(13.1)
        self.assertAlmostEqual(result, -10.5, places=10, msg="13.1°F should equal -10.5°C")

    def test_fahrenheit_to_celsius_large_positive(self):
        result = self.converter.fahrenheit_to_celsius(392)
        self.assertAlmostEqual(result, 200.0, places=10, msg="392°F should equal 200°C")

    def test_fahrenheit_to_celsius_large_negative(self):
        result = self.converter.fahrenheit_to_celsius(-148)
        self.assertAlmostEqual(result, -100.0, places=10, msg="-148°F should equal -100°C")

    def test_fahrenheit_to_celsius_small_positive(self):
        result = self.converter.fahrenheit_to_celsius(32.9)
        self.assertAlmostEqual(result, 0.5, places=10, msg="32.9°F should equal 0.5°C")

    def test_fahrenheit_to_celsius_small_negative(self):
        result = self.converter.fahrenheit_to_celsius(31.1)
        self.assertAlmostEqual(result, -0.5, places=10, msg="31.1°F should equal -0.5°C")

    def test_fahrenheit_to_celsius_positive_integer(self):
        result = self.converter.fahrenheit_to_celsius(50)
        self.assertAlmostEqual(result, 10.0, places=10, msg="50°F should equal 10°C")

    def test_fahrenheit_to_celsius_negative_integer(self):
        result = self.converter.fahrenheit_to_celsius(-4)
        self.assertAlmostEqual(result, -20.0, places=10, msg="-4°F should equal -20°C")

    def test_fahrenheit_to_celsius_body_temp(self):
        result = self.converter.fahrenheit_to_celsius(97.88)
        self.assertAlmostEqual(result, 36.6, places=10, msg="97.88°F should equal 36.6°C")

    def test_fahrenheit_to_celsius_extreme_negative(self):
        result = self.converter.fahrenheit_to_celsius(-459.67)
        self.assertAlmostEqual(result, -273.15, places=10, msg="-459.67°F should equal -273.15°C")

if __name__ == '__main__':
    unittest.main()