
f1 = open('C:\\Users\\TV\\Documents\\BTTH_Python\\Test.txt', 'a') 
stghi = 'Hello! Xin chao'
f1.write('\n' + stghi) 
f1.close()

# Open file in read mode to read updated content
f1 = open('C:\\Users\\TV\\Documents\\BTTH_Python\\Test.txt', 'r')
print(f1.read())
f1.close()
