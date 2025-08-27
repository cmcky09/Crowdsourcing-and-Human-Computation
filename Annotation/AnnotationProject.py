from collections import defaultdict
x1 = [10,8, 8, 8, 8, 2, 9, 7, 8, 8, 2, 8, 7, 8, 2,10, 8, 8,10,10, 2, 7, 2, 2, 2, 2, 8, 2, 2, 2, 2, 2, 8, 2, 2, 2, 8, 8, 8, 8, 2, 7, 7, 7, 2, 2, 7, 8, 7, 2, 7, 7, 7, 7, 2, 7, 7, 7, 2, 7, 7, 7, 7, 7, 7, 7, 2, 7, 2, 2, 2, 2, 7, 7, 7, 2, 7, 2, 7, 7, 2, 7, 7, 7, 7, 7, 2, 7, 7, 7, 7, 2, 7, 7, 7, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]

x2 = [8, 8, 8, 8, 8, 8, 2, 9, 7, 8, 7, 6, 7, 8, 2, 9, 8, 8, 6, 6, 2, 8, 6, 8, 5, 8, 6, 5, 8, 4, 8, 3, 5, 6, 8, 2, 5, 8, 8, 8, 8, 8, 8, 8, 6, 8, 8, 8, 8, 7, 8, 8, 7, 8, 7, 8, 8, 8, 6, 7, 8, 8, 8, 7, 6, 8, 7, 7, 7, 7, 7, 7, 4, 8, 6, 6, 8, 6, 8, 6, 7, 7, 7, 7, 8, 6, 7, 6, 8, 6, 8, 6, 6, 6, 8, 8, 1, 7, 8, 7, 1, 8, 7, 8, 6, 8, 9, 7]


#Calculate Scott's pi for P1:
x1_count = defaultdict(lambda :0)
x2_count = defaultdict(lambda :0)
agreement = 0
num_items = len(x1)
ratings = num_items*2
num_categories = 10

for i in range(len(x1)):
    x1_choice = x1[i]
    x2_choice = x2[i]
    x1_count[x1_choice]+=1
    x2_count[x2_choice]+=1
    if x1_choice==x2_choice:
        agreement+=1

PrA = agreement/num_items

PrE = 0

for i in range(1,num_categories+1):
    PrE += ((x1_count[i]+x2_count[i])/ratings)**2

scottsPi = (PrA-PrE)/(1-PrE)
print(scottsPi)
'''
Scott's pi:
-0.006269051590268599
'''
