words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
print words.replace("day"," month")
# finds and replace with another word
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
#prints max and min value of an array

a = ["hello",2,54,-2,7,12,98,"world"]
print a.sort()
print "List : ", a
# sorts in order
print "length :",len(a)
#prints length of an array



b=["hello",2,12,98,"world"]
print b[0]
print b[len(b)-1]


z = [19,2,54,-2,7,12,98,32,10,-3,6]
print z.sort()
print "List : ", z

result1 = z[:5]
result2 = z[5:11]

print ([result1] + result2)
#New List