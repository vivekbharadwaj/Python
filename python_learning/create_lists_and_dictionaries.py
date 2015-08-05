# put lists into dictionaries
ingredients={}
ingredients["BLT"]=["bread","bacon","lettuce","tomato"]
print ingredients

#put dictionaries into lists
europe=[]
germany={"name":"germany","population":81000000.0} #data type is automatically calculated based on the value. simply typing 81000000 automatically puts this as an integer.
europe.append(germany)
print germany
print europe
spain={"name":"spain","population":51200000.0,"gender bias":True}
europe.append(spain)
print europe

#this is used to get dictionary values, square brackets even though dictionaries have curly braces
print germany["population"]/spain["population"] 

print europe[0] #this can give you the elements of the list
print europe[0].keys() #this gives the keys or attributes used inside the dictionary...notice that these are arranged in alphabetical order. not in the order that you stored them in.
print europe[0].keys()[1] #this references and names the specific keys or attributes used inside the dictionary
print europe[0].items()[1] #this is for getting the key names and the corresponding values.
print europe[0].values()[1] #this is only for the values inside the dictionary


print europe[0]["population"]/europe[1]["population"] #better to do it this way rather than indirect referencing because the number would be different. 

#similarly, we can create lists within lists and dictionaries within dictionaries...