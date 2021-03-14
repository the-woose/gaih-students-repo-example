#-------------------------Final Project-------------------------#
# This is a 10 question Computer knowledge competition program
# It gets its questions wrom the web, so it requires an internet connection
# Question Source:  https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple
#---------------------------------------------------------------#

#-------------------------get questions-------------------------#
import urllib.request
with urllib.request.urlopen('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple') as response:
   url_bytes = response.read()     #----read url----#
url_string = url_bytes.decode("utf-8")     #----decode bytes to string----#
url_string_fixed = url_string.replace("&quot;","'")     #----convert html quotes to string apostrophe----#
url_string_fixed = url_string_fixed.replace("&#039;","")     #----remove html apostrophe----#
url_dict=eval(url_string_fixed)     #----convert url to dictionary----#
# print(url_dict["results"])     #----print dictionary for testing purposes----#

#-------------------------trivia-------------------------#
right_answer_counter = 0
print("\n\n--Computer knowledge competition--\n")     #----Program Title----#
for i in range(10):
    print("\nQuestion",i+1,"\b:")
    print(url_dict["results"][i]["question"])
    answer = input("Answer: ")
    if answer.lower() == url_dict["results"][i]["correct_answer"].lower():     #----case sensitivity----#
        right_answer_counter += 1

#-------------------------results-------------------------#
print("\nYou answered", right_answer_counter, "questions correctly. Your Score is", right_answer_counter*10)     #----score feedback----#
if right_answer_counter <= 5: print("You failed the competition. Please try again")
else: print("Congratulatons. You Won!")
