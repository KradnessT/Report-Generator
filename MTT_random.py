import random

# 設定執行次數
times = 1

# 設定溫度範圍
T_range_1_L = 18.7
T_range_1_H = 19.4
T_range_2_L = 22.7
T_range_2_H = 23.4
T_range_3_L = 26.7
T_range_3_H = 27.4

# 設定濕度範圍
M_range_1_L = 58.5
M_range_1_H = 61.5
M_range_2_L = 48.5
M_range_2_H = 51.5
M_range_3_L = 38.5
M_range_3_H = 41.5


def T_random(T_range_1_L,T_range_1_H,
             T_range_2_L,T_range_2_H,
             T_range_3_L,T_range_3_H):
    
    range_1 = random.uniform(T_range_1_L,T_range_1_H)
    range_2 = random.uniform(T_range_2_L,T_range_2_H)
    range_3 = random.uniform(T_range_3_L,T_range_3_H)

    range_1_1 = round(range_1,1)
    range_2_1 = round(range_2,1)
    range_3_1 = round(range_3,1)
     
    print(range_1_1)
    print(range_2_1)
    print(range_3_1)

def M_random(M_range_1_L,M_range_1_H,
             M_range_2_L,M_range_2_H,
             M_range_3_L,M_range_3_H):
    
    range_4 = random.uniform(M_range_1_L,M_range_1_H)
    range_5 = random.uniform(M_range_2_L,M_range_2_H)
    range_6 = random.uniform(M_range_3_L,M_range_3_H)

    range_4_1 = round(range_4,1)
    range_5_1 = round(range_5,1)
    range_6_1 = round(range_6,1)
     
    print(range_4_1)
    print(range_5_1)
    print(range_6_1)

for i in range(times):

    T_random(T_range_1_L,T_range_1_H,
             T_range_2_L,T_range_2_H,
             T_range_3_L,T_range_3_H)
    
    M_random(M_range_1_L,M_range_1_H,
             M_range_2_L,M_range_2_H,
             M_range_3_L,M_range_3_H)

    count = i + 1
    if count == times:
        print(f"執行{count}次")