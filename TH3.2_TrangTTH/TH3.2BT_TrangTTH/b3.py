# Mo file voi che do ghi tiep
f1 = open('C:\\Users\\TV\\Documents\\BTTH_Python\\Test.txt', 'r')
# doc 10 ky tu dau tien cua file
st1 = f1.read(10)
print(st1,'--So ky tu la : ',len(st1))
f2 = open('C:\\Users\\TV\\Documents\\BTTH_Python\\Test.txt', 'r')
print(f2.read())
#doc tung dong cua file
print(f2.readline())