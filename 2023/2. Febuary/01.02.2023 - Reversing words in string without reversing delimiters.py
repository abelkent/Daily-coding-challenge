"""
Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. 
For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

def word_reverse(string, delimiters):

    #Initialises empty word and delimiter lists
    word_list = list()
    delimiter_list = list()

    #Initialises empty current word and delimiter strings
    current_word = str()
    current_delimter = str()

    #Iterates over characters in input string
    for character in string:
        
        #Finds delimiter
        if character in delimiters:
            #Was previously on a word
            if current_word != str():
                word_list.append(current_word)
                current_word = str()
            
            current_delimter += character

        #Finds non-delimiter
        else:
            #Was previously on a delimiter
            if current_delimter != str():
                delimiter_list.append(current_delimter)
                current_delimter = str()
            
            current_word += character
    
    #If current word and delimiter are not empty at end of character iteration, updates lists
    if current_word != str():
        word_list.append(current_word)
    if current_delimter != str():
        delimiter_list.append(current_delimter)
    
    #Reverses words
    word_list.reverse()
    
    #Initialiss blank output string
    output_string = str()

    #Composes output string and prints it
    for word in word_list:
        output_string += word
        if len(delimiter_list) != 0:
            output_string += delimiter_list.pop(0)

    print(output_string)
word_reverse("hello/world:here/", ["/",":"])
word_reverse("hello//world:here", ["/",":"])