import unittest
import math
from shapes import Circle, Triangle, Rectangle, calculate_area

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)
    
    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
    
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)
    
    def test_triangle_inequality(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)
    
    def test_right_angled_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())
        
        triangle2 = Triangle(3, 4, 4)
        self.assertFalse(triangle2.is_right_angled())
    
    def test_rectangle_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)
    
    def test_calculate_area_function(self):
        shapes = [Circle(2), Triangle(3, 4, 5), Rectangle(4, 5)]
        areas = [calculate_area(shape) for shape in shapes]
        self.assertAlmostEqual(areas[0], math.pi * 4)
        self.assertAlmostEqual(areas[1], 6.0)
        self.assertEqual(areas[2], 20)

if __name__ == '__main__':
    unittest.main()
