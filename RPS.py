# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 1:
        last_guess = opponent_history[-1]
        if last_guess == 'R':
            guess = 'R'  # They think you'll play 'P', so play 'R'
        elif last_guess == 'P':
            guess = 'P'
        elif last_guess == 'S':
            guess = 'S'


    return guess
