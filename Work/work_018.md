# 題目：
**018. 圖形繪製**

請使用迴圈繪製4種不同的圖形  
圖形請參考***範例測資***   

>菱形：兩對角線長度為N且由"*"構成的菱形
>
>魚形：身體由"*"組成，是一個對角線長度皆為 N 的菱形，尾巴由"-"組成三角形
>
>三角形的最長邊(底邊)在右，頂端朝左，是一個底為(N-2)，高為((N-1)/2)的三角形  


## 輸入說明  
**第一行:** 輸入整數 C，1 <= C <= 4，代表接下來要畫的圖形種類  
  **C=1**為第一種圖形 正三角形 (參考 範例輸出 1)  
  **C=2**為第二種圖形 倒三角形 (參考 範例輸出 2)  
  **C=3**為第三種圖形 菱形 (參考 範例輸出 9)  
  **C=4**為第四種圖形 魚形 (參考 範例輸出 13)  
  
**第二行:** 輸入整數 N ，0 < N < 50，代表這個圖形有N行

## 輸出說明  
若N為奇數且3<=N<=49。  
根據輸入，畫出對應的圖形若N為偶數或者N<=2或N>=50。輸出 error

**`此題不考慮C<1或C>4的情況`**
<br>

------------
# 測資

**範例輸入 1：**  
```
1
5
```
**範例輸出 1：**  
![image](https://i.imgur.com/mE3IEjj.png)
<br>

**範例輸入 2：**  
```
2
5
```
**範例輸出 2：**
![image](https://i.imgur.com/coDIqRt.png)
<br>

**範例輸入 3：**  
```
1
11
```
**範例輸出 3：**  
![image](https://i.imgur.com/hl6D1df.png)
<br>

**範例輸入 4：**
```
2
11
```
**範例輸出 4：**
![image](https://i.imgur.com/6S1g4HT.png)
<br>

**範例輸入 5：**
```
1
19
```
**範例輸出 5：**
![image](https://i.imgur.com/YvmwL28.png)
<br>

**範例輸入 6：**
```
2
19
```
**範例輸出 6：**
![image](https://i.imgur.com/7wpT9iq.png)
<br>

**範例輸入 7：**
```
1
10
```
**範例輸出 7 ：**
> error
<br>

**範例輸入 8：**
```
2
10
```
**範例輸出 8：**
> error
<br>

**範例輸入 9：**
```
3
7
```
**範例輸出 9：**
![image](https://i.imgur.com/6ZWFwb1.png)
<br>

**範例輸入 10：**
```
3
51
```
**範例輸出 10：**
>error
<br>

**範例輸入 11：**
```
3
21
```
**範例輸出 11：**
![image](https://i.imgur.com/TzfgzZj.png)
<br>

**範例輸入 12：**
```
3
2
```
**範例輸出 12：**
>error
<br>

**範例輸入 13：**
```
4
15
```
**範例輸出 13：**
![image](https://i.imgur.com/CZmlLQP.png)
<br>

**範例輸入 14：**
```
4
21
```
**範例輸出 14：**
![image](https://i.imgur.com/QHysOb2.png)
<br>

**範例輸入 15：**
```
4
10
```
**範例輸出 15：**
>error  
<br>
**範例輸入 16：**
```
4
1
```
**範例輸出 16：**
>error  
<br>

----
# 代碼：  
```python
# 圖形繪製
# 20231019

# 檢查是否輸入有效
# 若輸入無效就會有返還"False"
def is_valid_N(N):
    if N % 2 == 0 or N <= 2 or N >= 50:
        return False
    return True

# 绘制正三角形
def draw_triangle(N):
    for i in range(N):
        hashtags = "#" * (N - i - 1)
        stars = "*" * (2 * i + 1)
        print(hashtags + stars + hashtags)

# 绘制倒三角形        
def draw_inverted_triangle(N):
    for i in range(N):
        hashtags = "#" * (i)
        stars = "*" * (2 * (N - i) - 1)
        print(hashtags + stars + hashtags)

# 绘制菱形
def draw_diamond(N):
    for i in range(int(N//2)+1):
        spaces = " " * (N // 2 - i)
        stars = "*" * (2 * i + 1)
        print(spaces + stars + spaces)
        
    for i in range(int(N//2)-1,-1,-1):
        spaces = " " * (N // 2 - i)
        stars = "*" * (2 * i + 1)
        print(spaces + stars + spaces)

# 绘制鱼形
def draw_fish(N):
    for i in range(int(N//2)+1):
        spaces = " " * (N // 2 - i)
        stars = "*" * (2 * i + 1)
        lines = "-" * (i)
        print(spaces + stars + spaces * 2 + lines)
        
    for i in range(int(N//2)-1,-1,-1):
        spaces = " " * (N // 2 - i)
        stars = "*" * (2 * i + 1)
        lines = "-" * (i)
        print(spaces + stars + spaces * 2 + lines)

C = int(input())
N = int(input())

# 輸入無效就會接收到"False"
if not is_valid_N(N):
    print('error')
    
# 根据C的值选择要绘制的图形
else:
    if C == 1:
        draw_triangle(N)
    elif C == 2:
        draw_inverted_triangle(N)
    elif C == 3:
        draw_diamond(N)
    elif C == 4:
        draw_fish(N)
```
