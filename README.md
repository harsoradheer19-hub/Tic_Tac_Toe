This Tic Tac Toe application is a modern, Python-based desktop game featuring a sleek graphical user interface and multiple levels of artificial intelligence. Built with a focus on clean code and algorithmic implementation, it offers both a casual experience for friends and a challenging environment for solo players.

Core Features
Three-Tier AI Opponents:

Easy: Makes random moves for a relaxed game.

Medium: Employs basic strategy to prioritize winning moves and block the player from winning.

Hard: Utilizes the Minimax Algorithm, a recursive decision-making tool that ensures the AI plays optimally and is virtually unbeatable.

Dual Game Modes: Supports "Play Solo" against the computer or "Play With Friend" for local 1v1 multiplayer.

Modern UI/UX: Features a dark-themed interface built with Tkinter, complete with a persistent scoreboard, dynamic turn indicators, and responsive button animations.

Robust Game Logic: Includes a centralized win-checking engine that identifies horizontal, vertical, and diagonal victories or draws.

Technical Highlights
Language: Python

Library: Tkinter (GUI)

Algorithms: Minimax (Recursion), Randomization, and Heuristic Search

Architecture: Modular design with separate files for AI logic, game rules, and UI management to ensure scalability and readability.

Project Structure
ui.py: Manages the visual interface, animations, and user interactions.

ai.py: Houses the decision-making logic for all difficulty levels.

game.py: Contains the core rules and win-condition checks.

main.py: The entry point for launching the application.

Would you like me to help you draft the specific README.md file for your GitHub repository?
