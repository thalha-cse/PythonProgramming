'''Our task is to generate a random story every time the user runs the program. 
I will first store the parts of the stories in different lists, 
then the Random module can be used to select the random parts of the story stored in different lists'''

import random
when = ["A few years ago", "Yesterday", "Last night", "A long time ago", "On 20th Jan"]
who = ["a rabbit", "an elephant", "a mouse", "a turtle", " a cat"]
name = ["Ali", "Miriam", "daniel", "Tomy", "Stephen"]
residence = ["Barcelona", "India", "Germany", "Venice", "England"]
went = ["Cinema", "university", "Seminar", "School", "laundry"]
happened = ["made a lot of friends", " Eats a burger", "found a secret", "solved a mistery", "wrote a book"]
print(random.choice(when) + ", " + random.choice(name) + " that lived in " + random.choice(residence) + " went to the " +
      random.choice(went) + " and " + random.choice(happened))
