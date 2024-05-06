# task1
"""
mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
def kvadrat(list):
    kvadrat_list=[]
    for x in list:
        if x>=0 and (x ** 0.5).is_integer(): 
             kvadrat_list.append(x)
    return( kvadrat_list)

print(kvadrat(mylist))

"""

# task2
"""
list_input= input("Listin elementlerini daxil edin: ")
def təkrarlanmayan(list_input):
    listt = []
    list = list_input.split()
    for x in list:
        if list.count(x) == 1:
            listt.append(x)
    return listt

result = təkrarlanmayan(list_input)
print(f"listin təkrarlanmayan elementləri: {result}")

"""

# task3
"""
eded_input=input("ededleri daxil edin: ")
def ededlerin_hasili(eded_input):
    ededler = eded_input.split()
    hasil = 1
    for x in ededler:
        hasil *= int(x)
    return hasil

result = ededlerin_hasili(eded_input)
print(f"Daxil etdiyiniz edədlərin hasilı: {result}")

"""

# task4
"""
eded=int(input("ededi daxil edin: "))
list=[x for x in range(1,eded+1) if eded % x == 0 ]
print(list)

"""

# task5
"""
aylar=['yanvar','fevral','mart','aprel','may','iyun','iyul','avquust','sentyabr','oktyabr','noyabr','dekabr']
dict={ay: len(ay) for ay in aylar}
print(dict)

"""

# task6
"""
list=["Rick Sanchez","Morty Smith","Summer Smith","Jerry Smith","Beth Smith"]
adlar_split=[ad.split(" ") for ad in list]
adlar=[ad[0].lower() for ad in adlar_split]
print(adlar)

"""

# task7
"""
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

def average():
    ortalama = []
    for i in range(min(len(list1), len(list2))):
        ortalama.append((list1[i] + list2[i]) / 2)
    print(ortalama)

average()
    
"""