import os

def generate_negative_description_file():
    with open('neg.txt', 'w') as f:
        #loop over all the filenames
        for filename in os.listdir('negative'):
            f.write('negative/'+filename+'\n')