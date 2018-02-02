all_my_stuff = ['book', 'dog', 3, ('cat', 'dog'), 12.4232, bool, object]

#what happens with each one?

for stuff in all_my_stuff:
    try:
        stuffy_thing = type(stuff)
        print(stuffy_thing)
    except Exception as e:
        print(e)
