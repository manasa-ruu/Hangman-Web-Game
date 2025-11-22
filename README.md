Hangman Web Application :
   A responsive, web-based implementation of the classic Hangman word guessing game. This project demonstrates a full-stack Pythonapplication using Flask for the backend and HTML/Tailwind CSS for the frontend.
Project Overview :
   This application transforms the traditional paper-and-pencil game into an interactive web experience. Players try to guess a hiddenword one letter at a time. The backend manages the game state (score, remaining guesses, word selection) using secure server-sidesessions, ensuring a robust gaming experience that can't be easily cheated by inspecting the frontend code.
Key Features :
 1. Interactive Gameplay: Clickable virtual keyboard to guess letters.
 2. Visual Feedback: Dynamic "Hangman" stick figure updates with every incorrect guess.
 3. Score Tracking: Keeps track of wins in the current session.
 4. Responsive Design: optimized layout that works on both desktop and mobile devices.
 5. Secure Game Logic: Game state and word validation happen on the server (Python), not the browser.
 6. Session Management: Uses Flask Sessions to maintain progress across page reloads.
Technology Stack :
 1. Backend: Python 3.x, Flask
 2. Frontend: HTML5, JavaScript (Fetch API), Tailwind CSS (via CDN)
 3. Styling: Custom CSS & Tailwind utility classes
 4. Deployment Ready: Includes CORS support and Gunicorn compatibility.
How to Run :
  1. Start the Flask development server:
     python app.py
  2. Open your web browser and navigate to:
     [http://127.0.0.1:5000](http://127.0.0.1:5000)
How to Play :
1. The game selects a random word from a category (Programming, Science, etc.).
2. You will see dashes representing the letters of the hidden word.
3. Click the letters on the virtual keyboard to make a guess.
   Correct Guess: The letter is revealed in the word.
   Incorrect Guess: A part of the hangman figure is drawn.
4. You have 6 incorrect guesses before the game ends.
5. Try to guess the word before the stick figure is fully drawn!


This game is live on https://hangman-web-game.onrender.com

Developed as a Course Project.
