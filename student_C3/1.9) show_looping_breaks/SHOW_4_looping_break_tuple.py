all_my_stuff = ['book', 'dog', 3, ('cat', 'dog'), 12.4232, bool, object]

for stuff in all_my_stuff:
    try:
        tupley_thing = stuff + ('horse', 'sheep')
        print tupley_thing
    except Exception as e:
        print(e)
