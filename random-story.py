import random

when = ['Last week', 'Yesterday', 'Last night', 'Two days ago']
who = ['Christmas Mouse', 'an elf', 'Santa Claus', 'a reindeer', 'Mary Claus']
name = ['Fred', 'George', 'Sara', 'Penelope']
residence = ['Suffolk','Richmond','the beach', 'North Carolina']
went = ['the cookie jar', 'your home', 'your school', 'your backyard', 'your living room', 'the front porch']
happened = ['ate all your cookies', 'left a treat for you', 'made a lot of friends', 'worked on their homework', 'read a book', 'studied school stuff']

""" print(random.choice(when) + ', ' +
random.choice(who) + ' visited ' +
random.choice(residence) + ', went to ' +
random.choice(went) + ' and ' +
random.choice(happened)) """

x = 0
while x < 25:
    print(str(x) + ': ' +
    random.choice(when) + ', ' +
    random.choice(who) + ' visited ' +
    random.choice(went) + ' and ' +
    #if random.choice(went) == 'the cookie jar':
        #+ happened[0]
    #else:
    random.choice(happened))
    x = x+1

character = ['Christmas Mouse', '']
where = []
what = []
advice = ['listen to your Mom', 'listen to your Dad', 'do your homework', 'read every day', 'pickup your toys']
