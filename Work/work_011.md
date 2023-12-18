# 題目：
**011. 計算書費**  
A、B、C三本書價格如下，一顧客欲購買A:ｘ本、B:ｙ本、C:ｚ本（ｘ、ｙ、ｚ為使用者輸入），請計算A、B、C各花費多少，以及總共需花費多少錢？  
|   | 定價 | 1~10本 | 11~20本| 21~30本 | 31本以上 |  
|-------|-------|-------|-------|-------|-------|
| A |  380 | 原價 | 打A1折 | 打A2折 | 打A3折 |
| B | 1200 | 原價 | 打B1折 |打B2折 | 打B3折 |
| C |  180 | 原價 | 打C1折 | 打C2折 | 打C3折 |

-----------------------------------------------------------------------------------------
**輸入說明:**  
**第一行**:A 書本數量(整數,0~100),A1,A2,A3  
**第二行**:B 書本數量(整數,0~100),B1,B2,B3  
**第三行**:C 書本數量(整數,0~100),C1,C2,C3  
A1~C3為整數0~100，若85為85折，即為*0.85   

**輸出說明:**   
**第一行**:花費最多的書本名稱、費用(中間以逗號隔開)  
**第二行**:花費中間的書本名稱、費用(中間以逗號隔開)  
**第三行**:花費最少的書本名稱、費用(中間以逗號隔開)  
**第四行**:總費用  
每本書的費用，最後以無條件進位法到整數。  
如果兩本書費用相同，按照***A>B>C***的順序輸出  
總費用為每本書最後整數費用的加總  

-----------------------------------------------------------------------------------------
**範例輸入說明**  
6,95,80,75 (A書本的數量,A1,A2,A3)  
12,95,80,70 (B書本的數量,B1,B2,B3)  
30,90,80,75 (C書本的數量,C1,C2,C3)  

**範例輸出的說明**  
B,13680 (花費最多的書本名稱,費用)  
C,4320 (花費中間的書本名稱,費用)  
A,2280 (花費最少的書本名稱，費用)  
20280 (總金額為13680+4320+2280=20280)  

-----------------------------------------------------------------------------------------
**Example Input1:**  
6,95,80,75  
12,95,80,70  
30,90,80,75  

**Example Output1:**  
B,13680  
C,4320  
A,2280  
20280  

---------------------------------------------------------------------------------------------------------------
**Example Input2:**  
1,75,68,42  
1,79,63,57  
1,78,66,59  

**Example Output2:**  
B,1200  
A,380  
C,180  
1760  

-------------------------------------------------------------------------------------------
**Example Input3:**  
12,99,89,79  
22,98,88,78  
34,97,87,77  

**Example Output3:**  
B,23232  
C,4713  
A,4515  
32460  

----
## 代碼：  
**版本一：**  
```python 
# 計算書費
# 20230927
import math
Input_value1 = input().split(',')
x,A1,A2,A3 = int(Input_value1[0]),int(Input_value1[1]),int(Input_value1[2]),int(Input_value1[3])

Input_value2 = input().split(',')
y,B1,B2,B3 = int(Input_value2[0]),int(Input_value2[1]),int(Input_value2[2]),int(Input_value2[3])

Input_value3 = input().split(',')
z,C1,C2,C3 = int(Input_value3[0]),int(Input_value3[1]),int(Input_value3[2]),int(Input_value3[3])


def discount(quantity,base_price,price1,price2,price3):
    if quantity <= 10:
        return quantity * base_price
    elif quantity <= 20:
        return quantity * base_price * price1/100
    elif quantity <= 30:
        return quantity * base_price* price2/100
    else:
        return quantity * base_price * price3/100

cost_A = math.ceil(discount(x,380,A1,A2,A3))
cost_B = math.ceil(discount(y,1200,B1,B2,B3))
cost_C = math.ceil(discount(z,180,C1,C2,C3))

book_cost = [['A',cost_A],['B',cost_B],['C',cost_C]]
book_cost.sort(key=lambda x: x[1]) #可調整成順序或逆序(若是逆序-大到小（.sort(key=lambda x: -x[1])）)

highest_cost = book_cost[2]
mid_cost     = book_cost[1]
lowest_cost  = book_cost[0]

print(f"{highest_cost[0]},{highest_cost[1]}")
print(f"{mid_cost[0]},{mid_cost[1]}")
print(f"{lowest_cost[0]},{lowest_cost[1]}")

total_price = cost_A + cost_B + cost_C
print(total_price)
```

**版本二：**  
```python
# 計算書費
# 20230927
import math
input_A = input().split(',')
input_B = input().split(',')
input_C = input().split(',')

# 解析輸入
x, A1, A2, A3 = map(int, input_A)
y, B1, B2, B3 = map(int, input_B)
z, C1, C2, C3 = map(int, input_C)

# 計算各書的花費
def calculate_cost(quantity, price, discount1, discount2, discount3):
    cost = quantity * price
    if quantity <= 10:
        cost *= discount1
    elif quantity <= 20:
        cost *= discount2
    else:
        cost *= discount3
    return math.ceil(cost)

cost_A = calculate_cost(x, 380, A1, A2, A3)
cost_B = calculate_cost(y, 1200, B1, B2, B3)
cost_C = calculate_cost(z, 180, C1, C2, C3)

# 計算總費用
total_cost = cost_A + cost_B + cost_C

# 找到花費最多、中間和最少的書本
book_costs = [("A", cost_A), ("B", cost_B), ("C", cost_C)]
book_costs.sort(key=lambda x: x[1], reverse=True)

most_expensive = book_costs[0]
middle_expensive = book_costs[1]
least_expensive = book_costs[2]

# 輸出結果
print(f"{most_expensive[0]},{most_expensive[1]}")
print(f"{middle_expensive[0]},{middle_expensive[1]}")
print(f"{least_expensive[0]},{least_expensive[1]}")
print(total_cost)
```
