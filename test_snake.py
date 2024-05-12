import unittest
from snake_game import Snake, SnakeSegment, Food, NormalFood, SpecialFood, create_snake, create_food

class TestSnakeGame(unittest.TestCase):
    def test_snake_move(self):
        snake, _ = create_snake()
        initial_segments = snake.segments[:]
        snake.move()
        new_segments = snake.segments[:]
        self.assertNotEqual(initial_segments, new_segments)

    def test_snake_grow(self):
        snake, _ = create_snake()
        initial_length = len(snake.segments)
        snake.grow()
        new_length = len(snake.segments)
        self.assertEqual(new_length, initial_length + 1)

    def test_food_creation(self):
        food = create_food()
        self.assertIsInstance(food, Food)

    def test_food_effect(self):
        snake, _ = create_snake()
        initial_length = len(snake.segments)
        food = NormalFood(0, 0)
        food.effect(snake)
        new_length = len(snake.segments)
        self.assertEqual(new_length, initial_length + 1)

    def test_special_food_effect(self):
        snake, _ = create_snake()
        initial_length = len(snake.segments)
        food = SpecialFood(0, 0)
        food.effect(snake)
        new_length = len(snake.segments)
        self.assertEqual(new_length, initial_length + 2)

if __name__ == '__main__':
    unittest.main()
