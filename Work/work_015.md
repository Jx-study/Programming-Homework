# 題目：
**015. BMI比較**  
給定n個人輸入身高與體重並計算BMI，BMI計算後需先***四捨六入五看偶***取到**小數點第二位**，
並以捨入後的結果計算BMI的**最大值、最小值、中位數、眾數**，再將計算結果進行四捨六入五看偶取到小數點第二位。

>BMI = 體重(公斤) / (身高*身高)(公尺)

**四捨六入五看偶規則:**  
保留位數的後一位如果是5，要根據應看尾數「5」的前一位決定是捨去還是進入，如果是**奇數**則進位，如果是**偶數**則捨去。  
**例如**：5.215保留兩位小數為5.22，而 5.225保留兩位小數為5.22。  

**中位數:**  
為一數列經過排序後，處數列**中間的數**  
**如：**[3,6,8,10,11] 則中位數 = 8  
若數列有**偶數個數**，則取中間兩數的平均為中位數，  
**如：**[2,3,5,8,13,21] 則中位數 = (5+8)/2 = 6.5  
![](https://images2015.cnblogs.com/blog/482045/201703/482045-20170326222206080-1922311580.png)

**眾數：**  
為一數列當中出現最多次的數。  
**如：**[1,2,2,3,3,3,4,4,5] 則眾數 = 3  
若有多個眾數，則取最小者做為眾數。  
**如：**[2,2,2,3,3,3,4,4] 則眾數 = 2  

---------------------------------------------------------------------------------------
**輸入說明**  
**第1行**：輸入一個整數，表示接下來將輸入n個人的身高體重（2<=n<=10）　  
**第2~n+1行**：輸入兩個浮點數，以空白隔開。第一個浮點數為身高(公尺,1.50<=身高<=2.50)，第二個浮點數為體重(公斤，0.0<=體重<=150.0)  

**輸出說明**  
**第1行**：輸出為一浮點數，表示n個人中BMI的最大值  
**第2行**：輸出為一浮點數，表示n個人中BMI的最小值  
**第3行**：輸出為一浮點數，表示n個人中BMI的中位數  
**第4行**：輸出為一浮點數，表示n個人中BMI的眾數  

---------------------------------------------------------------------------------------
**範例輸入說明:**  
4 (表示接下來將有4筆輸入)  
1.78 75.0 (第1個人，身高=1.78公尺，體重=75.0公斤)  
1.77 84.5 (第2個人，身高=1.77公尺，體重=84.5公斤)  
1.75 62.3 (第3個人，身高=1.75公尺，體重=62.3公斤)  
1.56 48.5 (第4個人，身高=1.56公尺，體重=48.5公斤)  

**範例輸出說明:**  
26.97 (4人中BMI最大為26.97)  
19.93 (4人中BMI最小為19.93)  
22.00 (4人的BMI中位數為22.00)  
19.93 (4人的BMI眾數為19.93)  

---------------------------------------------------------------------------------------
**Example Input 1:**  
5  
2.00 80.0  
1.88 85.3  
1.68 68.1  
1.53 48.2  
1.72 60.1  
**Example Output 1:**  
24.13  
20.00  
20.59  
24.13  

---------------------------------------------------------------------------------------
**Example Input 2:**  
5  
1.88 69.5  
1.52 52.8  
1.68 55.5  
1.72 65.2  
1.62 60.4  
**Example Output 2:**  
23.01  
19.66  
22.04  
19.66  

---------------------------------------------------------------------------------------
**Example Input 3:**  
7  
1.72 75.6  
1.52 38.4  
1.66 64.7  
1.68 80.2  
1.75 71.9  
1.62 74.6  
1.75 93.4  
**Example Output 3:**  
30.50  
16.62  
25.55  
23.48  

----
## 代碼：  
```python
# BMI比較
# 20231008

number_people = int(input())
bmi = []
for i in range(number_people):
    Input_value = input().split(' ')
    height, weight = float(Input_value[0]),float(Input_value[1])
    BMI = weight / height**2
    # 四捨六入五看偶
    a = int(BMI*1000)
    b = int((BMI*1000//10)*10)
    # int的原因是擔心減法時會有細微誤差（2-1=1.0000003）
    if int(a-b) == 5:
        if int(BMI * 100) % 2 == 0: #當保留數后一位為5時，判斷保留數是否為偶數
            BMI -= 0.001
        else:
            BMI += 0.001          
    BMI = round(BMI, 2)
    bmi.append(BMI)

bmi.sort()
maximum_bmi = max(bmi)
minimum_bmi = min(bmi)

# 判斷中位數
if len(bmi) % 2 == 0:  # 有偶数个数据
    middle1 = bmi[len(bmi) // 2 - 1]
    middle2 = bmi[len(bmi) // 2]
    median = (middle1 + middle2) / 2
else:  # 有奇数个数据
    median = bmi[len(bmi) // 2]
# 四捨六入五看偶    
x = int(median*1000)
y = int((median*1000//10)*10)
if int(x-y) == 5:
    if int(median * 100) % 2 == 0: #當保留數后一位為5時，判斷保留數是否為偶數
        median -= 0.001
    else:
        median += 0.001          
median = round(median, 2)


# 判斷衆數
"""
方一：
import statistics 
mode = statistics.mode(bmi)

方法二
def find_mode(bmi):
    # 初始化众数和計數器字典
    mode = 0
    count_dict = {}

    # 遍歷列表，建立計數器字典
    for data in bmi:
        if data in count_dict:
            count_dict[data] += 1
        else:
            count_dict[data] = 1

    # 找到最大的次數
    max_count = max(count_dict.values())

    # 找到所有众数
    for data, count in count_dict.items():
        if count == max_count:
            mode = data

    return mode

# 示例用法
result = find_mode(bmi)
print(result)
"""
mode_dict = {}
for data in bmi:
    if data in mode_dict:
        mode_dict[data] += 1
    else:
        mode_dict[data] = 1

# 找到出现次数最多的数字（众数）
max_count = max(mode_dict.values())
mode = [data for data, mode in mode_dict.items() if mode == max_count]
mode = sorted(mode)

# 輸出
print('%.2f' % maximum_bmi)
print('%.2f' % minimum_bmi)
print('%.2f' % median)
print('%.2f' % mode[0])
```
