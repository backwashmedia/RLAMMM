"""
----------------------------------------------------
RANDOM LYRIC ABSTRACT MAGIC MYSTERY MACHINE!!!!!!!!
----------------------------------------------------
FILE: rlg.py
----------------------------------------------------
My final project is a random lyric generator. I have been a musician for 25 years, and have never once had confidence in
writing lyrics. It never came naturally, and I was always too embarrassed of even thinking of singing my own words aloud.
So I thought, why not try and build a random lyric generator? As I learn python, I want to continue to develop and evolve 
this program to be more functional. At this time, the songs are very abstract. I did not focus on trying to rhyme words at 
this time, although it is a goal of this project in the long run to make that a feature. I would also like to add the ability 
of choosing a genre, or subject, to create lyrics for. For example: love, the blues, political, motivational, etc.) There are 
many different types of song structures. I tried to stray away from a full mad-libs, so the sentences would be totally random. 
However, in order to make the program work as is, I decided to add some constants in some of the sentences.
The user will be prompted the type of song structure they would like, and the program will generate random verses from
many predefined sentence structures, and print the lyrics accordingly. I love to make improvisational music, and very
weird strange lyrics appeal to me. Something like a completely random lyric machine would be useful, to me it would
anyways. I have learned to love effects, and to me personally, the music is what I tend to focus on. If I can add SOME
kind of lyric, albeit very strange random non-sensical lyrics, then a song can be finished. I enjoy the abstractness of
it. I hope you enjoy!
"""

import random
from reportlab.pdfgen import canvas  # used reportlab module to draw python's output onto a new pdf.
from reportlab.lib.pagesizes import letter  # used reportlab module to set the newly created pdf to a standard letter size, 8.5" x 11".


def main():
    intro()  # prints out the welcome message and intro.
    can = canvas.Canvas('lyrics.pdf', pagesize=letter)  # creates a standard letter-sized, blank pdf called 'lyrics.pdf'
    choice = get_choice()  # gets user input and determines if the input is valid for our program (any whole # > 0).
    get_credentials(can)  # gets the artist's name, generates a random song title, and outputs to pdf.
    get_lyrics(choice, can)  # retrieves lyrics and sends the output to our new pdf.
    can.save()  # saves our newly created song as pdf.

# --------------------------------------------------------------------------------------------------------------------
############################################ main functions #########################################################
# --------------------------------------------------------------------------------------------------------------------

def intro():
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    print("Welcome to the Random Lyric Abstract Magic Mystery Machine!!!")
    print("Here, you will be prompted to enter how many blocks of lyrics you would like generated.")
    print("You will then decide your artist name, and be provided with a randomly generated song title for the lyrics.")
    print("The RLAMMM will generate however many blocks of 4 verses that the user desires.")
    print("As a bonus, the RLAMMM will output your new lyrics to a fresh pdf so you can send it to your friends!")
    print("Don't worry about generating too much. No amount of lyrics is too much for the RLAMMM!")
    print("RLAMMM will output multiple pages of lyrics if you want a huge song.")
    print("Be warned! This is very abstract, meaning it is nonsensical most of the time!")
    print("It is meant to be! Art - especially the abstract - is very much in the eye of the beholder.")
    print("Have fun and I hope many laughs are had! Enjoy!!!")

def get_choice():
    while True:
        print()
        print("----------------------------------------------------------------------------------------")
        print()
        choice = input("How many bars would you like to create? ")
        try:
            choice = int(choice)
            if choice > 0:
                return choice
            else:
                print("Invalid whole number. Please enter a whole number greater than 0.")
        except ValueError:
            print("No strings or floats. Please enter a whole number greater than 0.")

# gets input from user to establish the artist name, and randomly chooses a song title from a set of song titles.
# outputs the generated credentials to our newly created pdf.

def get_credentials(can):
    print()
    print("----------------------------------------------------------------------------------------")
    print()
    artist = input("What's the artist's name whom I have the pleasure of interacting with? ")
    print("Assigning writing credentials........")
    print()
    song_title = get_song_title()
    print("----------------------------------------------------------------------------------------")
    art = str("Artist:" + " " + artist)
    song = str("Song Title: " '"' + song_title + '"')
    print(art)
    print(song)
    print("----------------------------------------------------------------------------------------")
    print()
    can.setFont("Courier", 10)  # sets the font and size.
    can.drawString(15, 770, "--------------------------------------------------------------------------------------------------")
    can.drawString(15, 750, art)
    can.drawString(15, 730, song)
    can.drawString(15, 710, "--------------------------------------------------------------------------------------------------")

# passes in how many bars the user wants, and generates that number of bars. one bar of verses == a block of 4 verses.
# each bar will get written to the pdf. if the program reaches the end of a page, a new page is created and the
# process continues.

def get_lyrics(num_bars, can):
    y = 700
    if num_bars <= 6:
        for i in range(num_bars):
            y -= 20
            for i in range(4):
                y -= 20
                get_random_verse(can,y)
            print()
    else:
        for i in range(num_bars):
            y -= 20
            for i in range(4):
                y -= 20
                get_random_verse(can,y)
                if y < 50:
                    can.showPage()
                    can.setFont("Courier", 10)
                    y = 770
            print()

# retrieves one random verse. uses the previous y location to determine where to print(in this case, the next line down)

def get_random_verse(can,y):
    objects = get_objects()
    sen1 = objects['adj3'] + " " + objects['noun'] + ", " + objects['adverb'] + " " + objects[
        's_verb'] + "," + " the " + objects['adj'] + " " + objects['noun2'] + " " + objects['adverb2'] + " " + objects[
               's_verb2'] + "."
    sen2 = objects['art'] + " " + objects['noun'] + " " + objects['s_verb3'] + ", " + objects['art'] + " " + objects[
        'noun2'] + " " + objects['s_verb2'] + "."
    sen3 = "I never " + objects['past_verb'] + " the " + objects['noun'] + "," + " but I did " + objects[
        'verb'] + " a " + objects['noun2'] + "."
    sen4 = "you want me to " + objects['verb'] + "? " + "I will never " + objects['verb'] + "!"
    sen5 = "are you the " + objects['noun'] + " i'm looking for?" + " i " + objects['past_verb'] + " " + objects[
        'adverb'] + ", " + "and you were " + objects['adj3'] + " for once."
    sen6 = objects['verb'] + "! " + objects['verb'] + "!" + " " + objects['verb2'] + " the " + objects['noun'] + "!"
    sen7 = "the " + objects['noun2'] + " " + objects['adverb'] + " " + objects['s_verb'] + " the " + objects[
        'noun3'] + "!"
    sen8 = objects['adj'] + " " + objects['noun'] + ", " + objects['adj'] + " " + objects['noun2'] + "."
    sen9 = objects['adverb2'] + " " + objects['s_verb'] + " the " + objects['adj2'] + " " + objects['noun3'] + "."
    sen10 = "a " + objects['noun'] + " " + objects['s_verb'] + " " + objects['adverb'] + "," + " the " + objects[
        'adj'] + " " + objects['noun2'] + " " + objects['adverb2'] + " " + objects['s_verb2'] + "."
    sen11 = objects['verb'] + ", " + objects['verb'] + ", my " + objects['adj'] + " " + objects['noun'] + "."
    sen12 = "don't " + objects['verb'] + ", " + objects['art'] + " " + objects['adj'] + " " + objects[
        'animal'] + " will " + objects['verb2'] + "."
    sen13 = objects['adj'] + " ---"
    sen14 = "to " + objects['country'] + ", to " + objects['country2'] + "------"
    sen15 = objects['art'] + " " + objects['adj'] + " " + objects['adj2'] + " " + objects[
        'noun'] + " of " + objects['country'] + ", " + objects['s_verb'] + " " + objects['art2'] + " " + objects[
        'noun2'] + "."
    sen16 = objects['adj'] + " " + objects['adj2'] + " " + objects['noun'] + "."
    sen17 = "the " + objects['noun'] + " of " + objects['country'] + " is " + objects['adj'] + "."
    List = [sen1, sen2, sen3, sen4, sen5, sen6, sen7, sen8, sen9, sen10, sen11, sen12, sen13, sen14, sen15, sen16,
            sen17
            ]
    choice = random.choice(List)
    can.drawString(15, y, choice)
    print(choice)

# retrieves song title using randomly generated objects.

def get_song_title():
    x = get_objects()
    title1 = x['adj'] + " " + x['noun']
    title2 = x['art'] + " " + x['adverb'] + " " + x['past_verb'] + " " + x['noun']
    title3 = x['art'] + " " + x['animal'] + " and " + x['art2'] + " " + x['adj'] + " " + x['animal2']
    title4 = x['verb'] + "! " + x['verb'] + "! " + x['verb'] + "!"
    title5 = x['verb'] + ", " + x['verb2'] + ", " + x['verb3']
    title6 = x['art'] + " " + x['animal'] + " " + x['past_verb'] + " my " + x['noun']
    title7 = x['art'] + " " + x['adj'] + " " + x['animal'] + " from " + x['country']
    title8 = "a " + x['animal'] + " named " + x['firstname']
    title9 = x['firstname'] + " is a " + x['adj'] + " " + x['noun']
    title10 = x['adj'] + " " + x['country']
    title11 = x['country'] + " is " + x['past_verb']
    title12 = x['firstname'] + " looks like " + x['art'] + " " + x['animal']
    title13 = x['firstname'] + " changed their name to " + x['firstname2'] + ", " + "and now it's " + x['adj']
    List = [title1, title2, title3, title4, title5, title6, title7, title8, title9, title10, title11, title12, title13]
    choice = random.choice(List)
    return choice

# ---------------------------------------------------------------------------------------------------------------------
############################################ very important helper functions!!! ######################################
# ---------------------------------------------------------------------------------------------------------------------

# creates a dictionary of all of our sentence objects we will use to create individual verses.

def get_objects():
    dict = {'adj': get_adjective(), 'adj2': get_adjective(), 'adj3': get_adjective(),
            'noun': get_noun(), 'noun2': get_noun(), 'noun3': get_noun(),
            'verb': get_verb(), 'verb2': get_verb(), 'verb3': get_verb(),
            's_verb': get_s_verb(),'s_verb2': get_s_verb(), 's_verb3': get_s_verb(),
            'past_verb': get_past_verb(), 'past_verb2': get_past_verb(), 'past_verb3': get_past_verb(),
            'adverb': get_adverb(), 'adverb2': get_adverb(), 'adverb3': get_adverb(),
            'art': get_art(), 'art2': get_art(), 'art3': get_art(),
            'animal': get_animal(), 'animal2': get_animal(), 'animal3': get_animal(),
            'country': get_country(), 'country2': get_country(), 'country3': get_country(),
            'firstname': get_first_name(), 'firstname2': get_first_name(), 'firstname3': get_first_name(),
            'pronoun': get_pronoun(),
            }
    return dict

# retrieves random pronoun from pron.txt file.

def get_pronoun():
    List = open('pron.txt').readlines()
    pronoun = random.choice(List)
    pronoun = pronoun.strip()
    return pronoun

# retrieves random noun from noun.txt file.

def get_noun():
    List = open('nouns.txt').readlines()
    noun = random.choice(List)
    noun = noun.strip()
    return noun

# retrieves random verb from verb.txt file.

def get_verb():
    List = open('verb.txt').readlines()
    verb = random.choice(List)
    verb = verb.strip()
    return verb

#retrieves random adverb from adverb.txt file.

def get_adverb():
    List = open('adverb.txt').readlines()
    adverb = random.choice(List)
    adverb = adverb.strip()
    return adverb

# retrieves random adjective from adj.txt file.

def get_adjective():
    List = open('adj.txt').readlines()
    adjective = random.choice(List)
    adjective = adjective.strip()
    return adjective

# retrieves random article from art.txt file.

def get_art():
    List = open('art.txt').readlines()
    art = random.choice(List)
    art = art.strip()
    return art

# retrieves random plural, present tense verb from verb_plural.txt file.

def get_s_verb():
    List = open('verb_plural.txt').readlines()
    s_verb = random.choice(List)
    s_verb = s_verb.strip()
    return s_verb

# retrieves random past tense verb from verb_past.txt file.

def get_past_verb():
    List = open('verb_past.txt').readlines()
    past_verb = random.choice(List)
    past_verb = past_verb.strip()
    return past_verb

# retrieves random animal from animal.txt file.

def get_animal():
    List = open('animal.txt').readlines()
    animal = random.choice(List)
    animal = animal.strip()
    return animal

# retrieves a random country from countries.txt file.

def get_country():
    List = open('countries.txt').readlines()
    country = random.choice(List)
    country = country.strip()
    return country

# retrieves a random first name from firstnames.txt file.

def get_first_name():
    List = open('firstnames.txt').readlines()
    firstname = random.choice(List)
    firstname = firstname.strip()
    return firstname


if __name__ == '__main__':
    main()
