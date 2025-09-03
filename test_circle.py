import unittest
from circle import *

class TestCircle(unittest.TestCase):
    def test_init_positive_radius(self):
        circle = Circle(5.0)
        self.assertEqual(circle.getRadius(), 5.0, "Radius should be set to 5.0")

    def test_init_zero_radius(self):
        circle = Circle(0.0)
        self.assertEqual(circle.getRadius(), 0.0, "Radius should be set to 0.0")

    def test_set_radius_positive(self):
        circle = Circle(1.0)
        result = circle.setRadius(10.0)
        self.assertTrue(result, "setRadius should return True for positive radius")
        self.assertEqual(circle.getRadius(), 10.0, "Radius should be updated to 10.0")

    def test_set_radius_negative(self):
        circle = Circle(1.0)
        result = circle.setRadius(-1.0)
        self.assertFalse(result, "setRadius should return False for negative radius")
        self.assertEqual(circle.getRadius(), 1.0, "Radius should remain unchanged")

    def test_get_area(self):
        circle = Circle(3.0)
        expected_area = math.pi * 3.0 * 3.0
        self.assertAlmostEqual(circle.getArea(), expected_area, places=10, msg="Area should be pi * radius^2")

    def test_get_area_zero_radius(self):
        circle = Circle(0.0)
        self.assertEqual(circle.getArea(), 0.0, "Area should be 0 for zero radius")

    def test_get_area_bug_radius_two(self):
        circle = Circle(2.0)
        self.assertEqual(circle.getArea(), 0, "Area should be 0 for radius 2 due to known bug")

    def test_get_circumference(self):
        circle = Circle(3.0)
        expected_circumference = 2.0 * math.pi * 3.0
        self.assertAlmostEqual(circle.getCircumference(), expected_circumference, places=10, msg="Circumference should be 2 * pi * radius")

    def test_get_circumference_zero_radius(self):
        circle = Circle(0.0)
        self.assertEqual(circle.getCircumference(), 0.0, "Circumference should be 0 for zero radius")

if __name__ == '__main__':
    unittest.main()