#keep checking surrounding color
#if index color is old color, flip to new color
#if all surrounding is new color, dont change

def paint_fill(image_array, r, c, color):

	old_color = image_array[r][c]

	if r < 0 or r >= len(image_array) or c < 0 or c >= len(image_array[0]):
 		return

	if image_array[r][c] == color:
		return 

	surrounding_color(image_array, r, c, color, old_color)

def surrounding_color(image_array, r, c, color, old_color):
 	

 	if r < 0 or r >= len(image_array) or c < 0 or c >= len(image_array[0]):
 		return

 	if image_array[r][c] != old_color:
 		return

 	if image_array[r][c] == old_color:
 		image_array[r][c] = color

	if r + 1 < len(image_array): 
		surrounding_color(image_array, r + 1, c, color, old_color)
 	if r - 1 >= 0: 
 		surrounding_color(image_array, r - 1, c, color, old_color)
 	if c + 1 < len(image_array[0]): 
 		surrounding_color(image_array, r, c + 1, color, old_color)
 	if c - 1 >= 0:
 		surrounding_color(image_array, r, c - 1, color, old_color)

	return True

import unittest

class Test(unittest.TestCase):
  def test_paint_fill(self):
    image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
              [30, 20, 20, 10, 10, 40, 40, 40],
              [10, 10, 20, 20, 10, 10, 10, 10],
              [10, 10, 30, 20, 20, 20, 20, 10],
              [40, 40, 10, 10, 10, 10, 10, 10]]
    image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [10, 10, 20, 20, 30, 30, 30, 30],
              [10, 10, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
    image3 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [30, 30, 20, 20, 30, 30, 30, 30],
              [30, 30, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
    paint_fill(image1, 1, 3, 30)
    self.assertEqual(image1, image2)
    paint_fill(image1, 3, 1, 10)
    paint_fill(image1, 3, 1, 30)
    self.assertEqual(image1, image3)

if __name__ == "__main__":
  unittest.main()