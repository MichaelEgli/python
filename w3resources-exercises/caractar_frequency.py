file_path = 'example.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

print('file content: ' + file_content)
print('length of file_content: ', file_content.__len__())
