# Course work Snake game

### What is my application?

The application developed is a classic Snake game implemented using the Pygame library in Python. The Snake game is a simple yet addictive game where the player controls a snake that moves around the screen, eating food to grow longer while avoiding collisions with itself and the walls. The objective of the game is to achieve the highest score possible by controlling the snake's movements strategically.

### How to run the game?

To run the Snake game program, follow these steps:

1. Ensure you have Python installed on your system. If not, you can download and install it from the official Python website (https://www.python.org/).
2. Install the Pygame library by running the following command in your terminal or command prompt:
- `pip install pygame`
3. Download the Snake game source code.
4. Navigate to the directory containing the Snake game source code using the terminal or command prompt.
5. Run the Python script named snake_game.py using the following command:
- `python snake_game.py`

### How the program implements functional requirements?
**4 OOP pillars:**
  - **Encapsulation:** I've encapsulated related functionality into classes like `Snake`, `SnakeSegment`, `Food`, `NormalFood`, and `SpecialFood`. Each class encapsulates its specific behavior and properties.
  - **Abstraction:** Class Interfaces: Each class provides a clear interface for interacting with its objects. For example, the Snake class exposes methods like `move()` and `grow()` for controlling the snake's movement and growth, respectively. Users of the `Snake` class do not need to know the internal details of how these methods are implemented; they only need to know how to use them.
  - **Polymorphism:** Method Overriding - Polymorphism is achieved through method overriding, where subclasses provide their own implementation of methods defined in the superclass. For example, both `NormalFood` and `SpecialFood` classes override the `draw()` and `effect()` methods inherited from the `Food` class.
  - **Inheritance:** In `GameObject` class it serves as the base class for game objects like snake segments and food items. Other classes inherit from this base class to inherit common attributes and methods.

**2 design patterns:**
  - **Builder:** Function`create_snake()` initializes and returns a Snake object along with its initial direction. Although it's not explicitly named as a builder method, it serves the purpose of constructing a Snake object with its initial state. Function `create_food()` creates and returns a Food object, either a NormalFood or SpecialFood object, based on the specified type. It acts as a factory method for creating different types of food objects. These functions encapsulate the logic for creating complex objects (Snake and Food) and hide the details of their construction from the caller. While they may not adhere strictly to the traditional builder pattern, they fulfill a similar role in the context of your game code by providing abstraction and encapsulation of object creation logic.
  - **Composite:** `GameObject` and its Subclasses: Although `GameObject` is used as a base class for `SnakeSegment` and `Food` (and its subclasses), they don't form a composite structure in the traditional sense. `GameObject` provides a common interface for all game objects, but there isn't a hierarchy or tree structure where objects contain other objects of the same type, which is a hallmark of the Composite pattern.
The program counts users score and writes it in file. With this principle people can always see high score and their score after game.

### Challenges faced during the implementation

- One of the biggest challenge was writing desing patterns in the code. In the end those patterns are not ideal and not perfect.
- Another challenge was making the two diffrent foods and making them interract with snake (tail length)

### Conclusion
It was my first game ever developed and for the first time I can see what code does - in my case how it creates game. The program created is a fully functional Snake game that provides an interactive and engaging user experience. Players can start the game, control the snake, consume food items, and attempt to beat the high score.
The implementation of various OOP concepts within the game's design ensures the code is modular, easier to manage, and scalable for future enhancements. 

### Future Prospects of the Program

- New Features: Adding more complex game features such as different levels, obstacles, or power-ups can make the game more engaging.
- Improved Graphics: Integrating more advanced graphical elements and animations could enhance the visual appeal and gameplay experience.
- Sound Effects and Music: Adding audio feedback for various game actions can make the game more immersive and enjoyable
- Performance Optimization: Refining the code to improve efficiency and performance, particularly as new features are added.
- Refactoring: Continuous refactoring can simplify existing implementations and accommodate new game features more easily.


