import random

giving_up = 0

def wake_up():
    global giving_up
    print "When I woke up..."
    late_for_class = random.randint (0,6)
    if late_for_class == 1:
        giving_up += 5
        print "I was late for class."
    stuff_due = random.randint (0,5)
    if stuff_due == 1:
        giving_up += 5
        print "Assignments were due today."
    nightmare = random.randint (0,5)
    if nightmare == 1:
        giving_up += 5
        print "I had a nightmare."
    hours_slept = random.randint (4,12)
    if hours_slept < 6:
        giving_up += 5
        print "I slept too little."
    if hours_slept > 10:
        giving_up += 5
        print "I slept too much."
    took_medication = random.randint (0,4)
    if took_medication == 0:
        giving_up += 5
        print "I forgot to take my medication." 
    bad_weather = random.randint (0,4)
    if bad_weather == 1:
        giving_up += 3
        print "The weather was bad." 
    if late_for_class != 1 and stuff_due != 1 and nightmare != 1 and took_medication != 0 and bad_weather != 1:
        print "Everything was okay."

def what_happened():
    global giving_up
    physical_health = random.randint (1,3)
    if physical_health < 3:
        giving_up += 3
        print "I didn't feel well."
    mental_health = random.randint (1,3)
    if mental_health < 3:
        giving_up += 3
        print "I wasn't in a good mood."
    self_esteem = random.randint (-2, 2)
    if self_esteem < 0:
        giving_up += 3
        print "I didn't feel good about myself."
    nourished = random.randint (0,4)
    if nourished == 0:
        giving_up += 2
        print "I didn't eat enough food."
    bad_news = random.randint (0,6)
    if bad_news == 1:
        giving_up += 2
        print "I heard something bad happened today."

wake_up()
hour = 0
while hour < 12:
    if hour == 0:
        print "\n" + str(hour+1) + " hour after waking up..."
    else:
        print "\n" + str(hour+1) + " hours after waking up..."
    what_happened()
    g = random.randint(1,100)
    if g > (int(float(giving_up)/3)):
        if g > giving_up:
            if hour < 11:
                print "I managed to get things done."
            if hour == 11:
                print "I managed to get through the whole day!"
        else:
            print "I couldn't get anything done."
            if hour == 11:
                    print "I managed to get through the day!"            
    else:
        print "I couldn't do anything else today."
        break
        
    hour += 1