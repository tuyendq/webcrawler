import os # imports the module for manipulating files

def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)

def create_project_dir(directory): # create a folder for each website
    if not os.path.exists(directory): # create folder if not exists
        print('Creating project ' + directory)
        os.makedirs(directory)

def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url) # create file and insert homepage url
    if not os.path.isfile(crawled):
        write_file(crawled, '')     # create empty file

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete_file_contents(path):
    with open(path, 'w'):
        pass



# Test 1
create_project_dir('GeekUniversity')
create_data_files('GeekUniversity', 'https://geek-university.com') 
