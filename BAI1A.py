def Sonhohon30(n): #Ham kiem tra so nt
    if(n>30):
        return False
    else:
        return True
A=[1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]  # Khai bao mot list a
print("\n List A: ")
for i in A:
    print (i, end=" ")
print("\n")
print("{:-^30}".format(" SO NHỎ HƠN 30"))
# Doan tren chi de in ra cho dep thoi ^^
for i in A:
    if(Sonhohon30(i)): # Goi toi ham kiem tra
        print(i, end= " ")