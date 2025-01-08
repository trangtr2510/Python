# Open file in append mode to write data
f1 = open('C:\\Users\\TV\\Documents\\BTTH_Python\\Test.txt', 'a')  # 'a' allows appending to the file
stghi = 'Hello! Xin chao'
f1.write('\n' + stghi)  # Add a newline for better formatting
f1.close()

# Open file in read mode to read updated content
f1 = open('C:\\Users\\TV\\Documents\\BTTH_Python\\Test.txt', 'r')
print(f1.read())
f1.close()
