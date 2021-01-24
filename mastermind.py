# p9o0p\=-09876543e2w1q                   7654EEWOIK,MJUHNGBVFRCDVG CXGFRDESWQAaQSwdefrtyuio0p-[p0o98i7u6y54retyui\
#     ][p9io8u7yt6re4wq   OP[\
#         ][';/PLKJHGFD
#         ":,.LKMNJHBGVFC1
#         0".56+0
#         '3/]]]
# 
import random

# code = [0, 0, 0, 0]
# correct_digits_and_position = 0
# correct_digits_only = 0
# correct = False


def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""

    # global code
    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    # print(code)
    return code

def show_instructions():
    """Shows instructions to the user"""

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    # return show_instructions(code)

def show_results(correct_digits_and_position, correct_digits_only):
    """Show the results from one turn"""

    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))
    # return show_results()

def get_answer_input():
    # correct = False
    # turns = 0
    answer = input("Input 4 digit code: ")

    while len(answer) < 4 or len(answer) > 4:
            # answer = input("Input 4 digit code: ")
            if len(answer) < 4 or len(answer) > 4 or answer.isdigit():
                print("Please enter exactly 4 digits.")
                answer = input("Input 4 digit code: ")
                # print(answer)
                # continue
            # break
    return answer

def take_turn(code,turns):
    """Handle the logic of taking a turn, which includes:
       * get answer from user
       * check if answer is valid
       * check correctness of answer
    """

    # global correct_digits_and_position
    # global correct_digits_only
 
    correct_digits_and_position = 0
    correct_digits_only = 0
    answer = get_answer_input()
    for i in range(4):
        if code[i] == int(answer[i]):
            # print('sdfhjsdkjfhdsjfh')
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    show_results(correct_digits_and_position, correct_digits_only)
    return (correct_digits_and_position, correct_digits_only)
        # turns += 1
        # correct = en  d_message(correct_digits_and_position, turns)
    # show_results()

    # return take_turn()

def show_code(code):
    """Show Code that was created to user"""

    print('The code was: '+str(code))
    # return show_code()

def check_correctness(correct_digits_and_position, turns):
    """Checks correctness of answer and show output to user"""

    # global correct
    correct = False
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
    else:
        print('Turns left: ' + str(12 - turns))

    # return check_correctness()
    return(correct)

def run_game():
    """Main function for running the game"""
    # global turns
    # global correct
    correct = False

    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        correct_pos, correct_dig = take_turn(code,turns)
        turns += 1
        # check_correctness(turns)
        correct = check_correctness(correct_pos, turns)

    show_code(code)
    # return run_game()

if __name__ == "__main__":
    run_game = run_game()
