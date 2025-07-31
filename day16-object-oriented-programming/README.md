# Day 16: Object-Oriented Programming (OOP) & Coffee Machine Refactor

## Overview
Today was all about diving into Object-Oriented Programming (OOP) in Python. I learned how to define and work with classes, objects, attributes, and methods—then used those concepts to rebuild the coffee machine project from Day 15 using OOP principles.

## Topics Covered
- Why OOP is important and how it structures code
- Defining custom classes and instantiating objects
- Understanding attributes vs. methods
- Using dot notation to access or modify data
- Using external Python packages via PyPi
- Refactoring procedural code into object-oriented design

## Project: OOP Coffee Machine
The procedural coffee machine logic was restructured into three classes:
- `MenuItem`: Represents drink data (name, ingredients, cost)
- `Menu`: Holds available drinks and provides interface methods
- `CoffeeMaker`: Manages resources and handles drink making
- `MoneyMachine`: Handles payments and reports profit

### Features
- Clean, modular structure using objects
- Easier to extend with new features or drinks
- Better separation of concerns and encapsulation

## Key Concepts Practiced
- `__init__()` method and object construction
- Calling and modifying object methods/attributes
- Organizing code across multiple modules
- Reusability and scalability in design

## Takeaways
OOP makes it easier to manage complex code by mimicking real-world structures. This was a major milestone that reshaped the way I approach larger projects in Python.

## Files Included
- `main.py`: The orchestrator, handling program flow
- `menu.py`, `coffee_maker.py`, `money_machine.py`: Class modules

