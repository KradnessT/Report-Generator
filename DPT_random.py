import random

# 設定執行次數
times = 1

# 設定壓力範圍
P_range_1_L = 39.5
P_range_1_H = 40.2
P_range_2_L = 24.5
P_range_2_H = 25.2
P_range_3_L = 9.5
P_range_3_H = 10.2

def P_random(P_range_1_L,P_range_1_H,
             P_range_2_L,P_range_2_H,
             P_range_3_L,P_range_3_H):
    
    range_1 = random.uniform(P_range_1_L,P_range_1_H)
    range_2 = random.uniform(P_range_2_L,P_range_2_H)
    range_3 = random.uniform(P_range_3_L,P_range_3_H)

    range_1_1 = round(range_1,1)
    range_2_1 = round(range_2,1)
    range_3_1 = round(range_3,1)
    
    print(range_1_1)
    print(range_2_1)
    print(range_3_1)

for i in range(times):

    P_random(P_range_1_L,P_range_1_H,
             P_range_2_L,P_range_2_H,
             P_range_3_L,P_range_3_H)
    
    count = i + 1
    if count == times:
        print(f"執行{count}次")