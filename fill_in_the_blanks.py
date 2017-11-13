# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

easy = '''In Python, anonymous ___1___ is a ___1___ that is defined without a name. While normal 
          ___1___s are defined using the def ___2___ , in Python anonymous ___1___s are defined 
          using the ___3___ ___2___ . Hence, anonymous ___1___s are also called ___3___ ___1___s .'''

medium = '''A python ___1___ is an unordered collection of items. While other compound data types have 
          only value as an element, a ___1___ has a key: value ___2___ . ___1___s are optimized to 
          retrieve values when the key is known. Creating a ___1___ is as simple as placing items 
          inside curly ___3___ {} separated by ___4___ . An item has a key and the corresponding value 
          expressed as a ___2___ , key: value.'''

difficult = '''Python is an ___1___ programming language. ___1___ programming (OOP) 
            focuses on creating ___2___ patterns of code, in contrast to ___3___ programming,
            which focuses on explicit sequenced instructions. When working on complex programs in 
            particular, ___1___ programming lets you reuse code and write code that is more 
            readable, which in turn makes it more ___4___'''

options = {'easy':easy,'medium':medium,'difficult':difficult}
trials_selection = {'easy':5,'medium':3,'difficult':2}

answer_list_easy = {"___1___":"function","___2___":"keyword","___3___":"lambda"}
answer_list_medium = {"___1___":"dictionary","___2___":"pair","___3___":"braces","___4___":"comma"}
answer_list_difficult = {"___1___":"object-oriented","___2___":"reusable","___3___":"procedural","___4___":"maintenable"}

answer_options = {'easy':answer_list_easy,'medium':answer_list_medium,'difficult':answer_list_difficult}

def check_answer(question,answer,answer_list):
    
    right_answer = answer_list[question]
    
    if answer == right_answer:
        
        return True
        
    return False
    
def replace_string(question,string,text):
    
    words = text.split()
    
    if question in words or question+"s" in words or question+"." in words:
        
        # if the word before the question has a . the string is capitalized
        # if it has an s the s is added to the string
        for i in range(len(words)):
            if question == words[i] or question+"s"==words[i]:
                if words[i-1][-1:] == "." and question+"s"==words[i]:
                    words[i] = string.capitalize() + "s"
                elif  words[i-1][-1:] ==".":
                    words[i] = string.capitalize()
                elif  question+"s"==words[i]:
                    words[i] = string + "s"
                else:
                    words[i] = string
        
        return " ".join(words)            
        
    return False
    
def get_user_input(question):
    
    return raw_input(question).strip()
    
def make_question(answer_list, updated_text):
    
    # convert the text in a list
    text_list = updated_text.split()
    question = ""
    questions = answer_list.keys()
    # find the first word in the text that matches a value to 
    # to question
    for word in text_list:
        if word in questions or word[:-1] in questions:
            # add the value to the question 
            if word[-1:] == ".":
                question = word[:-1]
            else:
                question =  word
            return question
            
    # if no value was found means all the question have been answered
    return False
    
def check_quiz_not_completed(answer_list,quiz):
    for value in answer_list.keys():
        if value in quiz:
            return True
            
    return False

    
def select_difficulty():
    
    not_selected = True
    options_message = "Which level do you wan to try, easy, medium or difficult? "
    
    while (not_selected):
        
        selection = get_user_input(options_message)
        
        if selection in options.keys():
            quiz = options[selection]
            total_trials = trials_selection[selection]
            answer_list = answer_options[selection]
            not_selected = False
            
            return selection, quiz, total_trials, answer_list
            
        else:
            print "Wrong option"
            

def play_game():
    
            
    selection, quiz, total_trials, answer_list = select_difficulty() 
    quiz_not_completed = True
    trials = 0
    
    print "This is the quiz. Read the text and figure out the value of each number."
    print ("As you selected the %s level you have %s trials for each fill in." % (selection, total_trials))
    print "*"*120 + "\n"
    print quiz
    print "*"*120 + "\n"
    
    
    while(quiz_not_completed):
        
        # Finds the next value to replace
        question = make_question(answer_list,quiz)
        # Build the question for the user
        question_text = "What's is the value of " + question  + "? "
        
        # gets the user answer
        answer = get_user_input(question_text)
        
        # check if the answer is right
        if check_answer(question,answer,answer_list):
            quiz = replace_string(question,answer,quiz)
            
        else:
            # if not add trial counter and ask again
            trials += 1
            if total_trials-trials == 0:
                print "The game is over. You have no trials left."
                answer = get_user_input("Do you want to start again (y/n)? ")
                if answer == 'y':
                    select_difficulty()
                else:
                    print "Thanks for playing with us. See you soon!"
                    quit()
            print ("You gave the wrong answer. You have %s trials left, Try again!"%(total_trials-trials))
            #print quiz
        print "*"*120 + "\n"    
        print quiz
        print "*"*120 + "\n"
        
        quiz_not_completed = check_quiz_not_completed(answer_list,quiz)
    
    
    print "Congratulalions! You won!"
            
        
play_game()        
    


sample_test = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___ by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

sample_1 = '''A function is created with the def keyword. You specify the inputs a function takes by
adding ___2___ separated by commas between the parentheses. function by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''    

test_1 = "___1___ ok"
test_1_a ="hola ok"
test_2 = "___1___s ok"
test_2_a ="holas ok"
test_3 = "___1___ ok ___1___s ok. ___1___ ok. ___1___s ok" 
test_3_a ="hola ok holas ok. Hola ok. Holas ok"


sample_2 = '''A function is created with the def keyword. You specify the inputs a function takes by
adding ___2___ separated by commas between the parentheses. function by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

sample_3 = """A python dictionary is an unordered collection of items. While other compound data types 
have only value as an element, a dictionary has a key: value ___2___. Dictionarys are optimized to retrieve
values when the key is known. Creating a dictionary is as simple as placing items inside curly curly {} 
separated by ___4___. An item has a key and the corresponding value expressed as a ___2___, key: value."""

answer_list = {"___1___":"function","___2___":"arguments","___3___":"None","___4___":"lists"}
answer_list2 = {"___1___":"dictionary","___2___":"pair","___3___":"curly","___4___":"comma"}
    
    
def test_check_answer():
    
    assert check_answer("___1___","function",answer_list)
    assert check_answer("___2___","argoments",answer_list) == False
    print "test_check_answer passed"
    

def test_replace_string():
    
    #print  replace_string("___1___","function",sample_test)
    #assert sample_1 == sample_2
    #assert replace_string("___1___","function",sample_test) == sample_2
    assert replace_string("___1___","hola",test_1) == test_1_a
    #print  replace_string("___1___","hola",test_2)
    assert replace_string("___1___","hola",test_2) == test_2_a
    assert replace_string("___1___","hola",test_3) == test_3_a
    
    print "test_replace_string passed"
    
def test_get_user_input():
    
    assert get_user_input("Write Voro: ") == "Voro"
    print "test_get_user_input passed"

def test_make_question():
    
    # assert make_question(answer_list,sample) == \
    # "___1___"
    # text_test = replace_string("___1___","function",sample)
    # assert make_question(answer_list,text_test) == \
    # "___2___"
    assert make_question(answer_list2,sample_3) == "___2___"
    
    print "test_make_question passed"
    
#test_check_answer()
#test_replace_string()
#test_get_user_input()
#test_make_question()

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/
