def to_ordinal_numbers(n):
    if n <= 0 or n > 12:
        ordinal_n = ''
    elif n == 1:
        ordinal_n = 'First'
    elif n == 2:
        ordinal_n = 'Second'
    elif n == 3:
        ordinal_n = 'Third'
    elif n == 4:
        ordinal_n = 'Fourth'
    elif n == 5:
        ordinal_n = 'Fifth'
    elif n == 6:
        ordinal_n ='Sixth'
    elif n == 7:
        ordinal_n = 'Seventh'
    elif n == 8:
        ordinal_n = 'Eighth'
    elif n == 9:
        ordinal_n = 'Ninth'
    elif n == 10:
        ordinal_n = 'Tenth'
    elif n == 11:
        ordinal_n = 'Eleventh'
    elif n == 12:
        ordinal_n = 'Twelfth'



def verses(n):
    if n == 1:
        verse = 'A partridge in a pear tree'
        return verse
    else:
        if n == 2:
            verse = '\nTwo turtledoves'
        if n == 3:
            verse = '\nThree French hens'
        elif n == 4:
            verse = '\nFour calling birds'
        elif n == 5:
            verse = '\nFive gold rings'
        elif n == 6:
            verse = '\nSix geese a-laying'
        elif n == 7:
            verse = '\nSeven swans a-swimming'
        elif n == 8:
            verse = '\nEight maids a-milking'
        elif n == 9:
            verse = '\nNine ladies dancing'
        elif n == 10:
            verse = '\nTen lords a-leaping'
        elif n == 11:
            verse = '\nI sent eleven pipers piping'
        elif n == 12:
            verse = '\nTwelve drummers drumming'
    return verse

def poesia():
    total_verses = ''
    last_verse = 'And a partridge in a pear tree'
    for i in range(1,13):
        if i == 1:
            print(f'On the {to_ordinal_numbers(i)} day of Christmas, my true love sent to')
            print(verses(i))
        else:
            print(f'On the {to_ordinal_numbers(i)} day of Christmas, my true love sent to')
            if not total_verses:
                print(verses(i) + last_verse)
            else:
                print(total_verses + verses(i) + last_verse)
            total_verses += verses(i)

poesia()
        





