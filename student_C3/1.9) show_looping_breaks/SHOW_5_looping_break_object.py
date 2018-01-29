all_my_stuff = ['book', 'dog', 3, ('cat', 'dog'), 12.4232, bool, object]

for stuff in all_my_stuff:
    try:
        objecty_thing = stuff()
        print(objecty_thing)
    except Exception as e:
        print(e)
