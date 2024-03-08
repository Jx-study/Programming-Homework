# 題目：
**011. 線條（009的Pro版）**  
請計算出(L1、L2、L3…Ln)N條線在 X 軸上所涵蓋的長度(不含重複線段)  
**例如:** L1(x1,x2)表示L1線段為 X 軸上點 x1 到點 x2 的線  
依序輸入起點和終點(起點 < 終點)，且較小的起點先輸入  
<br>    
    
## 輸入說明  
第一行 : 輸入總共有多少條線段 (整數N, 1 <= N <= 40)  
第二行 : 輸入 L1 的 x1, x2 座標 (整數M, -20 <= M <= 20)  
第 三 ~ N 行 : 重複第二行步驟直到Ln也輸入完成  

## 輸出說明  
輸出N條線段所涵蓋的長度 (整數)  

---------------------------------------------------------------------------------------
**範例輸入說明:**  
3 (輸入總共有多少條線段)  
-1 1 (L1 的 (x1,x2) 座標為 (-1,1)) -> (最小的起點先輸入，並以空格隔開)  
0 2 (L2 的 (x1,x2) 座標為 (0,2)) -> (最小的起點先輸入，並以空格隔開)  
1 3 (L3 的 (x1,x2) 座標為 (1,3)) -> (最小的起點先輸入，並以空格隔開)  
![](https://i.imgur.com/PEZAd8S.png)  

**範例輸出說明:**  
4 (最左邊的點為-1，最右邊的點為3，因此三條線所涵蓋的長度為4)  
<br>
<br>

---------------------------------------------------------------------------------------
# 測資
**Example Input 1:**  
```
3  
-5 -1  
-2 2  
3 5  
```
**Example Output 1:**  
>9  
<br>

**Example Input 2:**  
```
5  
-5 -2   
-1 1  
2 5  
3 6  
19 20  
```
**Example Output 2:**  
>10  
<br>

**Example Input 3:**  
```4  
-7 -1  
-2 3  
1 9  
-10 10  
```
**Example Output 3:**  
>20
<br>
 
----
# 代碼：  
## 版本一
```python
# 計算N條綫在X軸所覆蓋的長度(思路出錯誤未修改完)
# 20231005
#！！！！！！！！！！！！！！！！！！！！！！！！
total_lines = int(input())

lines =[]

for _ in range(total_lines):
    input_coordinate = input().split(' ')
    x1 = int(input_coordinate[0])
    x2 = int(input_coordinate[1])
    lines.append((x1,x2))  #兩個括弧是因爲append只接受一个参数添加到列表中成爲单个元素

lines.sort(key=lambda x:x[0])
total_length = 0
covered = False # 初始化覆盖变量为False

for i in range(total_lines-1):
    x1_now, x2_now = lines[i]
    x1_next, x2_next = lines[i + 1]
           
    total_length += x2_now - x1_now
    
    # 當下一條綫段與現綫段重叠
    if x1_next < x2_now:
        total_length -= x2_now - x1_next
          
   
    # 異常現象-如一條綫完全覆蓋下一條綫段
    if x2_now > x2_next:
        total_length -=  x2_next - x1_next
        covered = True
    
    
# 如果没有线段覆盖最後一條綫段，加入最后一条线段的长度              
if not covered:            
    total_length += lines[-1][1] - lines[-1][0]

print(total_length)
```

## 版本二 
```python
# 計算N條綫在X軸所覆蓋的長度
# 20231005

total_lines = int(input())
# 用來儲存N條線段的起始和結束值
lines = []

for _ in range(total_lines):
    input_coordinate = input().split(' ') # 將輸入的數值分割為起始和結束值
    x1 = int(input_coordinate[0])
    x2 = int(input_coordinate[1])
    lines.append([x1, x2])

lines.sort(key=lambda x: x[0])
total_length = 0
prev_x2 = float('-inf') # 初始化prev_x2(将其设置为负无穷大的值)

for x1, x2 in lines:
    if x1 > prev_x2: # 表示兩個線段不重疊
        total_length += x2 - x1
    elif x2 > prev_x2: # 表示有部分重疊
        total_length += x2 - prev_x2
    prev_x2 = max(prev_x2, x2) # 更新prev_x2為當前線段和前一個線段

print(total_length)
```
