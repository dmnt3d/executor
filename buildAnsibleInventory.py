import sys

dict = {} #create new dictionary to hold data
# filename = "~/Projects/terravSphere/Swarm/swarm.tfvars"
filename = sys.argv[1]
with open(filename) as file:
    for line in file: # process file line by line
        # parse using index of '=' as reference and put into dict
        key = line[0:line.find('=')-1] # store key
        value = line[line.find('=')+2:].rstrip().replace("\"","") # store value; strip out '\n' ; remove double quotes ""
        print ("KEY = " + key + "; VALUE = "+ value )
        dict[key] = value
file.close()

# start building out file
# convert to INT
# export to file
exportfile = "/home/master/Projects/host-Config/inventory/inventory-swarm"
fileEx = open (exportfile,"w+")
count  = int(dict["count"])
for x in range (count):
    # format : 172.16.0.210 s
    # server_name=nodedr03.ldc.int server=nodedr03
    name = '{:02}'.format(x+1) # put leading 0's
    fileEx.write(dict["ipv4"] + str(x+1) + " server_name=" + dict["prefix"] + name +"."+ dict["domain"] + " server=" + dict["prefix"] + str(name))
    fileEx.write('\n')
    

fileEx.close()
print ("------ Done building ansible inventory")





