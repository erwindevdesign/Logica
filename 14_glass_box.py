import unittest


def is_mayor(edad):
    if edad >= 18:
        return True
    else:
        return False
    
class GlassBoxTesting(unittest.TestCase):
    
    def test_is_mayor(self):
        edad = 20

        result = is_mayor(edad)

        self.assertEqual(result, True)

    def test_is_minor(self):
        edad = 15

        result = is_mayor(edad)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main() 