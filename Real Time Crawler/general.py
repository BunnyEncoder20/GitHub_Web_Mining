# This file contains only the file reading and writing general functions 


import os   #each project(Website whill be stored in different directories. OS helps in making new directories)


# This function creaates the new dir for the website if it doesn't exist already
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating a new Project : '+directory)
        os.makedirs(directory)

# This function creates the queue and data files (links files) if not already created
def create_data_files(project_name,root_url):
    queue = project_name + '/queue.txt'                  # These are file paths
    crawled = project_name + '/crawled.txt'           # These are file paths

    if not os.path.exists(queue):
        write_file(queue,root_url)  # when we make the queue file we must send it some data by default so me send the base url as the first link init 
    
    if not os.path.exists(crawled):
        write_file(crawled,'')


# This function creates a new file :
def write_file(path,data):
    file = open(path,'w')       # opening the file in write mode
    file.write(data)             # writing data to the file
    file.close()                    # closing the file to avoid data leaks and memory delays

# Function adds data to n existing file
def append_to_file(path,data):
    file = open(path,'a')       # opening the file in append mode
    file.write(data+'\n')      # appending the file with the new data
    file.close()                    # closing the file 

# Function to delete the file contents 
def delete_file_contents(path):
    with open(path,'w'):       # opening file in write mode just overwrites the contents and hence writing nothing = deleting all file contents  
        pass

# We use the sets data Structure to get only the unique links
# read a file and convert each line to set items  (Mostly for the waiting list file (which has all the link waiting to be crawled))
def file_to_set(file_name): 
    results = set()
    with open(file_name,'rt') as file:          # 'rt' = read text file
        for line in file:                                  # adding each line into the set
            results.add(line.replace('\n',''))     # replace the newline character with nothing                     
    return results

# Iterate through a set and each item will be a new line in the file 
def set_to_file(links,file):
    #whatever is in the file is the old data
    #links contains the new dat so we store those
    
    delete_file_contents(file)
    for link in sorted(links) :                     #sorting the links in order 
        append_to_file(file,link)
        


# create_data_files('wikipedia','https://en.wikipedia.org/wiki/Toyota_Supra')