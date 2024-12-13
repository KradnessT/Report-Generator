import random

# 設定執行次數
times = 1

# 設定壓力範圍
P_range_1_L = 290
P_range_1_H = 310
P_range_2_L = 590
P_range_2_H = 610
P_range_3_L = 890
P_range_3_H = 910

def P_random(P_range_1_L,P_range_1_H,
             P_range_2_L,P_range_2_H,
             P_range_3_L,P_range_3_H):
    
    range_1 = random.randint(P_range_1_L,P_range_1_H)
    range_2 = random.randint(P_range_2_L,P_range_2_H)
    range_3 = random.randint(P_range_3_L,P_range_3_H)
    
    print(range_1)
    print(range_2)
    print(range_3)


for i in range(times):
    P_random(P_range_1_L,P_range_1_H,
             P_range_2_L,P_range_2_H,
             P_range_3_L,P_range_3_H)

    count = i + 1
    if count == times:
        print(f"執行{count}次")