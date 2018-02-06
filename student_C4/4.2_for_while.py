# show how a while loop can be used on a list

artifact_list = ['pencil', 'paper', 'book', 'computer', 'door']

number_of_artifacts = len(artifacts)
n = 0

while n < number_of_artifacts:
    print(artifacts[n])
    n += 1                      # n += 1 is special syntax for n = n + 1
