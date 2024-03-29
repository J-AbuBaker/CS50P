file_name = input('File name: ').lower().strip().split('.')
image_ext = ['gif', 'jpg', 'jpeg', 'png']
doc_ext = ['pdf', 'txt', 'zip']

if len(file_name) > 1:  # Check if there's at least one extension provided
    if file_name[-1] in image_ext:
        if file_name[-1] == 'jpg':
            file_type = 'jpeg'
        else:
            file_type = file_name[-1]
        print(f'image/{file_type}')
    elif file_name[-1] == 'txt':
        print('text/plain')
    elif file_name[-1] in doc_ext:
        print(f'application/{file_name[-1]}')
    else:
        print('application/octet-stream')
else:
    print('application/octet-stream')
