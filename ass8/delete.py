Dict = {'Dict1': {'name': 'Ali', 'age': 19},'Dict2': {'name': 'Bob', 'age': 21}}
print("Initial nested dictionary:-")
print(Dict)
print("\nDeleting Dict2:-")
del Dict['Dict2']
print(Dict)
print("\nDeleting Dict1:-")
Dict.pop('Dict1')
print (Dict)