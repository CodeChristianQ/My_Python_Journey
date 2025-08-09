# The Turtle Cross Project

This project was inspired by the classic arcade game *Frogger*, but instead of a frog, we used a turtle!  
It was built entirely with Python's **turtle graphics** module, applying many of the same tools and programming concepts learned in earlier projects such as **Snake** and **Pong**.

## Project Overview
The goal of the game is to guide the turtle safely from the bottom of the screen to the top, avoiding moving cars along the way. Each time the turtle successfully reaches the top, the difficulty increases, making the game progressively more challenging.

## Key Features
- **Player Movement:** Controlled using the keyboard, allowing the turtle to move upward towards the goal.
- **Car Generation & Movement:** Cars are randomly generated in different lanes and move horizontally across the screen.
- **Collision Detection:** The game detects when the turtle collides with a car (*game over* scenario).
- **Level Progression:** Speed and difficulty increase each time the turtle reaches the other side.
- **Scoreboard:** Tracks and displays the player's progress and final score.

## Concepts Reinforced
- **Object-Oriented Programming (OOP):**  
  - Created multiple classes for modular code (`Player`, `CarManager`, `Scoreboard`).
  - Used inheritance and method overriding for better structure and reusability.
- **Event Listening:** Captured keypress events to control the player’s movements.
- **Collision Detection:** Implemented bounding-box logic to detect car-player overlaps.
- **Game Loop:** Managed real-time updates, object creation, and difficulty scaling.

## Skills Gained
- Improved understanding of game design patterns in Python.
- Strengthened OOP skills through class creation and inter-class communication.
- Learned how to progressively increase game difficulty for better player engagement.
- Refined logic for collision detection and scoring.

**Status:** ✅ Completed
