import sys

dict = {} #create new dictionary to hold data
filename = "../terravSphere/Swarm/swarm.tfvars"
with open(filename) as file:
    for line in file: # process file line by line
        # parse using index of '=' as reference and put into dict
        key = line[0:line.find('=')-1] # store key
        value = line[line.find('=')+2:].rstrip() # store value; strip out '\n'
        print ("KEY = " + key + "; VALUE = "+ value )
        dict[key] = value

# start building out file