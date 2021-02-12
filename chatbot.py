# Ian White - Chatbot, COG376
# Personality: Nicholas Angel (Simon Pegg) from Hot Fuzz (2007) 

import re
import os
from random import *
 
print("Sergeant Angel here.")

while(True):
    original = input("> ")

    if ("Angle" in original or "angle" in original):
        print("Very funny.\n<click>")
        os._exit(1)
    elif (original == "Bye" or original == "bye"):
        print("<click>")
        os._exit(1)
    
    newstr = original
    
    # Fact answers
    newstr = re.sub("[Ww]hat.*action movies\?",
                    "There's no way that you could perpetrate that amount of carnage " +
                    "and mayhem and not incur a considerable amount of paperwork.",
                    newstr, 0)
    newstr = re.sub("[Ww]ho are you\?",
                    "Sergeant Nicholas Angel, Sanford Police Force.",
                    newstr, 0)
    newstr = re.sub(".*about yourself[\.\?]",
                    "Sergeant Nicholas Angel, formerly Constable. Born and schooled in London. " +
                    "Graduated Canterbury University in 1993 with a double first in politics and sociology.",
                    newstr, 0)
    newstr = re.sub(".*injured.*\?",
                    "I've sustained three injuries in the line of duty. Most recently in December, when wounded " +
                    " by a man dressed as father Christmas.",
                    newstr, 0)
    newstr = re.sub(".*arrest record.*\?",
                    "Highest for any officer in the Met.",
                    newstr, 0)
    newstr = re.sub(".*[Hh]ow are you.*\?",
                    "I'd be a lot better if I didn't feel like I was going crazy in this town.",
                    newstr, 0)
    newstr = re.sub("[Tt]ell me a.*\.",
                    "There was the time I distracted Lurch with the cuddly monkey then I said \"play time's over\"" +
                    "and I hit him in the head with the peace lily.",
                    newstr, 0)
    newstr = re.sub("([Hh]ow's|[Ww]hat's) the weather( like|)\?",
                    "It's quite alright. Drive safe.",
                    newstr, 0)
    newstr = re.sub(".*ice cream.*[\.\?]",
                    "I love a cornetto.",
                    newstr, 0)
    newstr = re.sub("[Ii]s it true that there is a place.*that if you shoot it it will.*\?",
                    "...",
                    newstr, 0)
    newstr = re.sub("[Hh]ow about.*\?",
                    "I don't think that gives off the right signals.",
                    newstr, 0)
    
    # Pattern replacement
    newstr = re.sub("[Aa]re you.*at (.*)\?", "I'm exceptional at \\1.", newstr, 0)
    newstr = re.sub("[Ww]hen is (.*)\?", "I don't have time for \\1, Danny! There's are murderer on the loose!", newstr, 0)
    newstr = re.sub("[Dd]o you like (.*)\?", "\\1 is fine. But could I have a glass of the cranberry juice, please?", newstr, 0)
    newstr = re.sub("[Ww]hat happened to (.*)\?","\\1 was murdered!", newstr, 0)
    newstr = re.sub("[Ii]s (.*) (.*)ing\?","I don't know where \\1 is, but he certainly shouldn't be \\2ing.", newstr, 0)
    newstr = re.sub("(?:[Hh]ow's|[Ww]hat's it like) being a (.*)\?","Being a \\1 is what I do - but it's certainly not about proper action.", newstr, 0)
    
    
    
    
    if (newstr == original):
        i = randint(1,4)
        if (i == 1):
            newstr = "Not you too, Danny!"
        if (i == 2):
            newstr = "What the hell is going on around here?"
        if (i == 3):
            newstr = "...narp?"
        if (i == 4):
            newstr = "I... don't really know what to say."
        if (i == 5):
            newstr = "Am I going completely mad?"
    
    print(newstr)