# # when we just start and empty {} it becomes distionary
# d = {}
# print(type(d))
#
# d['sudarshan']=9898989898989
# d['abhishek']=96969696969
# d['ravi']=7474747474747
#
# print(d)
#
# print(d['sudarshan'])

Malgudi=['It', 'was', 'Monday', 'morning', 'Swaminathan', 'was', 'reluctant', 'to', 'open', 'his', 'eyes', 'he', 'considered', 'Monday','specially', 'unpleasant', 'in', 'the', 'calendar', 'After', 'the', 'delicious', 'freedom', 'of', 'saturday', 'and', 'sunday', 'it', 'was', 'difficult', 'to', 'get', 'into', 'the', 'Monday', 'mood', 'of', 'work', 'and', 'discipline', 'He', 'shuddered', 'at', 'the','very', 'thought', 'of', 'school', 'the', 'dismal', 'yellow', 'building', 'the', 'fire', 'eyed', 'Vednayagam', 'his', 'class','teacher', 'and', 'headmaster', 'with', 'his', 'thin', 'long', 'cane']

# print(len(Malgudi))

s=set(Malgudi)
# print(s)
# len(s)

# for x in Malgudi:
#     print(x)

d = {}

for x in s:
    d[x]=0

# print(d)


# d = {}

for x in Malgudi:
    d[x] = d[x] + 1

# print(d)

# print(d['his'])

max = 0
word = ''
d={}
for x in s:
    d[x]=0

# print(d)

for x in Malgudi:
    d[x] = d[x] + 1
    if d[x] > max:
        max = d[x]
        word = x

print(max, word)

