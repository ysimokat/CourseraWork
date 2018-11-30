
def data():
    ''' reads two datafiles into memory storing them in two lists.'''

    #read the datafile 'namesBoys' and store boy names in a list called boys
    file1 = open('namesBoys.txt','r')   
    boys=file1.read().strip().split()

    #read the datafile 'namesGirls and store girl names in a list called girls'
    file2 = open('namesGirls.txt','r')
    girls=file2.read().strip().split()

    #close this two datafiles
    file1.close()
    file2.close()
    #return two lists
    return boys,girls

#set b as boys, g as girls 
b,g=data()
#check the output of the function data()
#print('This is the list of boy names: {}'.format(b))
#print('This is the list of girl names: {}'.format(g))

#create three dictionaries
d = {'Ending':['Boys', 'Girls']}
boys={}
girls={}

# create a list that contains the last letter on each boy's name
boy_end = [i[-1] for i in b]
# create a list that contains the last letter on each girl's name
girl_end = [i[-1] for i in g]

# count the number of times a boy names ends in a particular letter
for i in sorted(boy_end):
    if i not in boys.keys():
        boys[i]=boy_end.count(i)  

# count the number of times a girl names ends in a particular letter
for i in sorted(girl_end):
    if i not in girls.keys():
        girls[i]=girl_end.count(i)  

# combine dictionaries boys and girls into dictionary d
for k,v in boys.items():
    for k1,v1 in girls.items():
        if k == k1:   #if they have same key, then store the values in a list
            d[k]=[v,v1]
        if k not in d.keys():  #if there is no same key exits, check the key exits in d or not
            d[k]=[v,0]
        if k1 not in d.keys():
            d[k1]=[0,v1]


#print(boys)
#print(girls)
#print the counts in a nice format and sorted columns
for k in sorted(d.keys()):
    print('{:10} {:<10} {:<10}'.format(k, d[k][0], d[k][1]))
    

# Looking at the counts we see that for girls the most common names end with “a”, ”e”, ”n”, “y”, and “h” 
# for boys the most common names end with “n”, “e”, “o”, “y”, and “r” between both boys and  girls the most common letters are “e”, “n”, and “y”.