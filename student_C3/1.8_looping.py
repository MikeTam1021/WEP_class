artifacts = ['pencil', 'paper', 'book', 'computer', 'door']
new_artifacts = []

print artifacts[1]

for item in artifacts:
    print(item)
    new_item = item + 'case'
    new_artifacts.append(new_item)

print(new_artifacts)
