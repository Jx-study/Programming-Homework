# 題目：
**009.計算出 a,b,c 三條線在 X 軸上所涵蓋的長度(不含重複線段)**  
例如: a(x1,x2)表示 a 線段為 X 軸上點 x1 到點 x2 的線
依序輸入起點和終點(起點 < 終點)，且較小的起點先輸入

---
**輸入說明**  
- 第一行 : 輸入 a 的 x1 座標 (整數, -20 ~ 20)  
- 第二行 : 輸入 a 的 x2 座標 (整數, -20 ~ 20)  
- 第三行 : 輸入 b 的 x1 座標 (整數, -20 ~ 20)  
- 第四行 : 輸入 b 的 x2 座標 (整數, -20 ~ 20)  
- 第五行 : 輸入 c 的 x1 座標 (整數, -20 ~ 20)  
- 第六行 : 輸入 c 的 x2 座標 (整數, -20 ~ 20)  
<img src="https://i.imgur.com/Ea6Je4i.png" alt="示例圖片" width="700">  

**輸出說明**  
輸出三條線段所涵蓋的長度 (整數)  

---
**範例輸入說明:**  
-1 (a 的 x1 座標為 -1)  A Line起點 : -1 (最小的起點，先輸入)  
1 (a 的 x2 座標為 1)  
0 (b 的 x1 座標為 0)    B Line起點 : 0 (次之)  
2 (b 的 x2 座標為 2)  
1 (c 的 x1 座標為 1)    C Line起點 : 1 (最後輸入)  
3 (c 的 x2 座標為 3)  

**範例輸出說明:**  
4 (最左邊的點為-1，最右邊的點為3，因此三條線所涵蓋的長度為4)  

---
**Example Input 1:**  
-5  
-1  
-2  
2  
3  
5  

**Example Output 1:**  
9  

---
**Example Input 2:**  
-3  
0  
1  
3  
5  
7  

**Example Output 2:**  
7  

---
**Example Input 3:**  
-7  
4  
-6  
-3  
1  
2  

**Example Output 3:**  
11  

----
## 代碼：
``` python
#計算三條綫在x軸所覆蓋的長度
#20230926

a_x1 = int(input())
a_x2 = int(input())
b_x1 = int(input())
b_x2 = int(input())
c_x1 = int(input())
c_x2 = int(input())

total_length = 0
# 計算a線段覆蓋的部分
total_length += a_x2 - a_x1

# 計算b線段覆蓋的部分
 #如果b的起点沒在a綫段中
if b_x1 > a_x2:          
    total_length += b_x2 - b_x1
# 如果b的起点在a綫段中，且b的终点沒被a綫段覆蓋
elif b_x1 < a_x2 and b_x2 > a_x2:
    total_length += b_x2 - a_x2

# 計算c線段所覆蓋的部分
# 如果c的起點沒在a和b綫段中
if c_x1 > a_x2 and c_x1 > b_x2:
    total_length += c_x2 - c_x1
# 如果c的起點在a之間，但c的終點沒被a綫段覆蓋
elif c_x1 < a_x2 and c_x2 > a_x2:
    total_length += c_x2 - a_x2
# 如果c的起點在b之間，但c的終點沒被b綫段覆蓋
    if c_x1 < b_x2 and c_x2 >b_x2:
        total_length += c_x2 - a_x2

print(total_length)
```
