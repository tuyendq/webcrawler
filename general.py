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

def file_to_set(file_name):
	"""Read a file and convert each line to set items"""
	results = set() # create an empty set
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results

def set_to_file(links, file_name):
	"""Iterate through a set, each item will be a line in a file"""
	with open(file_name, 'w') as f:
		for l in sorted(links):
			f.write(l+"\n")
# Test 1
create_project_dir('GeekUniversity')
create_data_files('GeekUniversity', 'https://geek-university.com') 
