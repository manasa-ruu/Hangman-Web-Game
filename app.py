import random
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)

app.secret_key = 'a_very_secret_key_for_hangman' 

# List of words for the game
WORDS = ['programming', 'data', 'python', 'code', 'computer', 'engineer', 'word', 'science', 
         'machine', 'java', 'college', 'player', 'mobile', 'image', 'algorithm', 'software',
         'tuple', 'dictionary', 'loop', 'operators', 'array', 'flowchart', 'fibonacci', 'iteration','comments',
         'hangman', 'complexity', 'module', 'function', 'list' , 'set', 'strings', 'boolean']

MAX_INCORRECT_GUESSES = 6 

def initialize_game(keep_score=False):
    """Sets up a new game session. If keep_score is True (after a win), the current score is retained."""
    word = random.choice(WORDS)
    session['word'] = word.lower()
    session['guessed_letters'] = []
    session['incorrect_guesses'] = 0
    
    current_score = session.get('score', 0)
    
    # Reset score unless explicitly told to keep it (only after a win)
    if not keep_score:
        session['score'] = 0
    else:
        session['score'] = current_score

    
    session['display_word'] = ['_' for _ in word]
    
@app.route('/')
def index():
    """Renders the main game page and initializes the game session if not already running."""
    if 'word' not in session:
        
        initialize_game(keep_score=False) 
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    """Handles a letter guess from the user, updates game state, and returns the result."""
    letter = request.json.get('letter').lower()
    
    # Input Validation
    if not letter or len(letter) != 1 or not letter.isalpha():
        return jsonify(get_game_state(message="Invalid guess. Please enter a single letter."))

    # Check if the letter has already been guessed (Correct behavior)
    if letter in session['guessed_letters']:
        return jsonify(get_game_state(message="You already guessed that letter!"))

    
    session['guessed_letters'].append(letter) 
    
    word = session['word']
    game_over = False
    
    if letter in word:
       
        current_display = list(session['display_word']) 

        for i, char in enumerate(word):
            if char == letter:
              current_display[i] = letter.upper() 
    
        session['display_word'] = current_display 
        
        # Check for win
        if '_' not in session['display_word']:
            session['score'] += 1
            game_over = True
            message = "YOU WON! Click 'Play Again' to start the next round."
        else:
            message = "Correct guess!"
    else:
      session['incorrect_guesses'] += 1
        
        # Check for loss
    if session['incorrect_guesses'] >= MAX_INCORRECT_GUESSES:
            game_over = True
            message = f"YOU LOST! The word was: {word.upper()}. Click 'Play Again' to restart."
    else:
        message = "Incorrect guess!"

    return jsonify(get_game_state(message=message, game_over=game_over))

@app.route('/restart', methods=['POST'])
def restart():
    """Restarts the game, preserving score only after a successful win."""
    keep_score = False
    

    is_previous_win = (
        session.get('display_word') and 
        '_' not in session['display_word'] and 
        session.get('incorrect_guesses', 0) < MAX_INCORRECT_GUESSES
    )
    
    if is_previous_win:
        keep_score = True

    initialize_game(keep_score=keep_score)
    return jsonify(get_game_state(message="Game started. Good luck!"))

def get_game_state(message="", game_over=False):
    """Compiles the current game state into a dictionary for JSON response."""
    
    _ = session.get('word') 
    
    
    hangman_img_index = session['incorrect_guesses'] + 1 
    if hangman_img_index > 7:
        hangman_img_index = 7 
        
    return {
        # Return the displayed word as a space-separated string
        'display_word': ' '.join(session['display_word']),
        # Return the list of guessed letters
        'guessed_letters': session['guessed_letters'],
        'incorrect_count': session['incorrect_guesses'],
        'hangman_img': f'h{hangman_img_index}',
        'score': session['score'],
        'message': message,
        'game_over': game_over
    }

if __name__ == '__main__':
    app.run(debug=True)