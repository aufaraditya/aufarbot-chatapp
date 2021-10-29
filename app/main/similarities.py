import re
import random
import json

def unknown(): #If Bot got no Idea what you talking about
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message

    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    with open('app/main/intents.json') as file:
        data = json.load(file) #Open dictionary from json file
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        response = random.choice(bot_response) #Pick random response for given intents-patterns
        highest_prob_list[response] = message_probability(message, list_of_words, single_response, required_words)


    # Responses -------------------------------------------------------------------------------------------------------
    for intent in data['intents']:
        if bool(intent['required_words']):
            response(intent['botresponse'], intent['patterns'], single_response=True)
        else:
            response(intent['botresponse'], intent['patterns'], required_words = intent['required_words'])
   
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower()) #Normalizing
    response = check_all_messages(split_message)
    return response
