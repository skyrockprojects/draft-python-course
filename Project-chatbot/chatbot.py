from random import randint


class ChatBot:

    # Get a default greeting
    # @return a greeting
    def getGreeting(self):
        return "Hello, let's talk."

    # Gives a response to a user statement
    # @param statement
    #            the user statement
    # @return a response based on the rules given
    def getResponse(self, statement):

        response = ""
        if (len(statement) == 0):
            response = "Say something, please."

        elif (findKeyword(statement, "no", 0) >= 0):
            response = "Why so negative?"

        elif (findKeyword(statement, "mother", 0) >= 0
              or findKeyword(statement, "father", 0) >= 0
              or findKeyword(statement, "sister", 0) >= 0
              or findKeyword(statement, "brother", 0) >= 0):
            response = "Tell me more about your family."

        elif (findKeyword(statement, "dog", 0) >= 0
              or findKeyword(statement, "cat", 0) >= 0):
            response = "Tell me more about your pets."

        #Insert your new non-transformative response here:

        #Responses which require transformations
        elif (findKeyword(statement, "I want to", 0) >= 0):
            response = transformIWantToStatement(statement)

        elif (findKeyword(statement, "I want", 0) >= 0):

            response = transformIWantStatement(statement)

        #Insert your new transformative response here:

        else:
            # Look for a two word (you <something> me)
            # pattern
            psnOfYou = findKeyword(statement, "you", 0)
            psnOfI = findKeyword(statement, "I", 0)
            #Insert the variable of the position of the first word in your two-word transformative response here:

            if (psnOfYou >= 0 and findKeyword(statement, "me", psnOfYou) >= 0):
                response = transformYouMeStatement(statement)

            elif (psnOfI >= 0 and findKeyword(statement, "you", psnOfI) >= 0):
                response = transformIYouStatement(statement)

            #Insert your new two-word transformative response here:

            else:
                response = getRandomResponse()

        return response


# Take a statement with "I want to <something>." and transform it into
# "What would it mean to <something>?"
# @param statement the user statement, assumed to contain "I want to"
# @return the transformed statement
def transformIWantToStatement(statement):
    #Remove the final period, if there is one
    statement = statement.strip()
    lastChar = statement[len(statement) - 1]
    if (lastChar == '.'):
        statement = statement[0, len(statement) - 1]

    psn = findKeyword(statement, "I want to", 0)
    restOfStatement = statement[psn + 9:].strip()
    return "What would it mean to " + restOfStatement + "?"


def transformIWantStatement(statement):
    #Remove the final period, if there is one
    statement = statement.strip()
    lastChar = statement[len(statement) - 1]
    if (lastChar == '.'):
        statement = statement[0, len(statement) - 1]

    psn = findKeyword(statement, "I want", 0)
    restOfStatement = statement[psn + 6:].strip()
    return "Would you really be happy if you had " + restOfStatement + "?"


#Insert your new transformative response function here:


# Take a statement with "you <something> me" and transform it into
# "What makes you think that I <something> you?"
# @param statement the user statement, assumed to contain "you" followed by "me"
# @return the transformed statement
def transformYouMeStatement(statement):
    #Remove the final period, if there is one
    statement = statement.strip()
    lastChar = statement[len(statement) - 1]
    if (lastChar == '.'):
        statement = statement[0, len(statement) - 1]

    psnOfYou = findKeyword(statement, "you", 0)
    psnOfMe = findKeyword(statement, "me", psnOfYou + 3)

    restOfStatement = statement[psnOfYou + 3:psnOfMe].strip()
    return "What makes you think that I " + restOfStatement + " you?"


def transformIYouStatement(statement):
    #Remove the final period, if there is one
    statement = statement.strip()
    lastChar = statement[len(statement) - 1]
    if (lastChar == '.'):
        statement = statement[0, len(statement) - 1]

    psnOfYou = findKeyword(statement, "I", 0)
    psnOfMe = findKeyword(statement, "you", psnOfYou + 1)

    restOfStatement = statement[psnOfYou + 1:psnOfMe].strip()
    return "Why do you " + restOfStatement + " me?"


# Search for one word in phrase.  The search is not case sensitive.
# This method will check that the given goal is not a substring of a longer string
# (so, for example, "I know" does not contain "no").
# @param statement the string to search
# @param goal the string to search for
# @param startPos the character of the string to begin the search at
# @return the index of the first occurrence of goal in statement or -1 if it's not found
def findKeyword(statement, goal, startPos):
    phrase = statement.strip().lower()
    #The only change to incorporate the startPos is in the line below
    psn = phrase.find(goal.lower(), startPos)

    #Refinement--make sure the goal isn't part of a word
    while (psn >= 0):
        #Find the string of length 1 before and after the word
        before = " "
        after = " "
        if (psn > 0):
            before = phrase[psn - 1:psn].lower()

        if (psn + len(goal) < len(phrase)):
            after = phrase[psn + len(goal):psn + len(goal) + 1].lower()

        #If before and after aren't letters, we've found the word
        if ((not before.isalpha()) and (not after.isalpha())):
            return psn

        #The last position didn't work, so let's find the next, if there is one.
        psn = phrase.find(goal.lower(), psn + 1)

    return -1


# Pick a default response to use if nothing else fits.
# @return a non-committal string
def getRandomResponse():
    responses = [
        "Interesting, tell me more.", "Hmmm.", "Do you really think so?",
        "You don't say."
    ]
    r = randint(0, len(responses) - 1)
    return responses[r]
