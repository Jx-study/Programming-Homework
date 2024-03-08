# 題目：
**Q20. 數字矩陣翻轉**
給定一個正整數n，產生一個n\*n的初始矩陣。初始矩陣中每個元素為一個數字，從1開始，由左到右、由上往下增加。例如：
n = 4 的初始矩陣  
&ensp;1&ensp;&ensp;2&ensp;&ensp;3&ensp;&ensp;4  
&ensp;5&ensp;&ensp;6&ensp;&ensp;7&ensp;&ensp;8  
&ensp;9&ensp;10&ensp;11&ensp;12  
13&ensp;14&ensp;15&ensp;16  
<br>
輸入n後，需要再輸入一串由L、R組成的字串，字串由左到右進行讀取，每次讀取一個字元。  
**L**表示將整個矩陣往***逆時針轉90度***，**R**表示將整個矩陣往***順時針轉90度***  
下面是n = 4 的初始矩陣讀取到**L**，往逆時針翻轉90度的範例：  
4&ensp;8&ensp;12&ensp;16  
3&ensp;7&ensp;11&ensp;15   
2&ensp;6&ensp;10&ensp;14   
1&ensp;5&ensp;&ensp;9&ensp;13   
<br>
下面是n = 4 的初始矩陣讀取到**R**，往順時針翻轉90度的範例：  
13&ensp;&ensp;9&ensp;5&ensp;1  
14&ensp;10&ensp;6&ensp;2    
15&ensp;11&ensp;7&ensp;3  
16&ensp;12&ensp;8&ensp;4  

當字串讀取完成後，輸出翻轉後的矩陣。  
**`注意，僅需要輸出完成所有翻轉後的結果，無需顯示過程`**  

## 輸入說明：  
**第一行：** 輸入一個正整數n，表示n\*n的矩陣（2 <= n <= 5）    
**第二行：** 輸入由L、R組成的字串，長度<=10。字串由左到右讀取每個字元，當讀取到L時將矩陣向逆時針翻轉90度，讀取到R時將矩陣向順時針翻轉90度。  

## 輸出說明：  
輸出一個矩陣，為初始矩陣經過翻轉後的結果。  

-----------------------
**範例輸入說明：**  
3  
>表示一個3\*3的初始矩陣，如下：  
1 2 3  
4 5 6  
7 8 9  

RRL
>表示對初始矩陣進行以下操作  
>1. R , 向順時針轉90度  
7 4 1  
8 5 2  
9 6 3
   
>2. R , 向順時針轉90度  
9 8 7  
6 5 4  
3 2 1  
   
>3. L , 向逆時針轉90度   
7 4 1
8 5 2
9 6 3

**範例輸出說明：**  
7 4 1
8 5 2
9 6 3
此為初始矩陣經過RRL三次翻轉後的結果

-----
# 測資
**Example Input 1：**    
```
3  
LLL
```
**Example Output 1：**  
>7 4 1  
8 5 2  
9 6 3  

**Example Input 2：**  
```
4  
LRLRRL
``` 
**Example Output 2：**  
>&ensp;1&ensp;&ensp;2&ensp;&ensp;3&ensp;&ensp;4  
&ensp;5&ensp;&ensp;6&ensp;&ensp;7&ensp;&ensp;8  
&ensp;9&ensp;10&ensp;11&ensp;12  
13&ensp;14&ensp;15&ensp;16  

**Example Input 3：**
```
5
RLLLRLLR
```
**Example Output 3：**  
>25&ensp;24&ensp;23&ensp;22&ensp;21  
20&ensp;19&ensp;18&ensp;17&ensp;16  
15&ensp;14&ensp;13&ensp;12&ensp;11  
10&ensp;&ensp;9&ensp;&ensp;8&ensp;&ensp;7&ensp;&ensp;6  
&ensp;5&ensp;&ensp;4&ensp;&ensp;3&ensp;&ensp;2&ensp;&ensp;1  

**Example Input 4：**  
```
4  
RLRRRLR
```
**Example Output 4：**  
>4&ensp;8&ensp;12&ensp;16  
3&ensp;7&ensp;11&ensp;15  
2&ensp;6&ensp;10&ensp;14  
1&ensp;5&ensp;&ensp;9&ensp;13  

---
# 代碼
## 版本一
```
# 數字矩陣
# 20231019

# 用途：生成一个nxn的矩阵
def matrix(n):
    matrix = []  # 创建一个空列表 matrix 用于存储矩阵
    for i in range(n):  # 创建 n 行
        row = []  # 创建一个空列表 row 用于存储矩阵的一行
        for j in range(n):  # 创建 n 列
            row.append(i * n + j + 1)  # 计算并添加矩阵中的元素
        matrix.append(row)  # 将一行添加到矩阵中
    return matrix 

# 用途：将矩阵逆时针旋转 90 度（左旋）
def function_L(matrix,n):
    rotated_matrix = []  # 创建一个新的空矩阵，用于存储旋转后的矩阵
    for _ in range(n):  # 创建 n 行
        row = [0] * n  # 创建一个 n 元素的全零列表，用于存储旋转后的矩阵的一行
        rotated_matrix.append(row)  # 将一行添加到旋转后的矩阵中
    for i in range(n):  # 行
        for j in range(n):  # 列
            rotated_matrix[i][j] = matrix[j][n - i - 1]  # 将原矩阵中的元素旋转后放入新矩阵
    return rotated_matrix
    
# 用途：将矩阵顺时针旋转 90 度（右旋）
def function_R(matrix,n):
    rotated_matrix = []  # 创建一个新的空矩阵，用于存储旋转后的矩阵
    for _ in range(n):  # 创建 n 行
        row = [0] * n  # 创建一个 n 元素的全零列表，用于存储旋转后的矩阵的一行
        rotated_matrix.append(row)  # 将一行添加到旋转后的矩阵中
    for i in range(n):  # 行
        for j in range(n):  # 列
            rotated_matrix[i][j] = matrix[n - j - 1][i]  # 将原矩阵中的元素旋转后放入新矩阵
    return rotated_matrix

n = int(input())  # 从用户输入获取矩阵的大小 n
initial_matrix = matrix(n)  # 生成初始矩阵
operations = input()  # 从用户输入获取操作序列

for op in operations:
    if op == 'L':  
        initial_matrix = function_L(initial_matrix,n)
    elif op == 'R': 
        initial_matrix = function_R(initial_matrix,n)
"""
省略寫法
initial_matrix = [function_L(initial_matrix) if op == 'L' else function_R(initial_matrix) for op in operations]
"""

for row in initial_matrix:  # 遍历最终的矩阵的每一行
    for x in row:  # 遍历每一行中的元素
        print(x, end=" ")  # 输出矩阵中的元素，用空格分隔
    print()  # 换行输出下一行
```
## 版本二
```
# 數字矩陣(新增上下翻轉和左右翻轉的功能)
# 20231019

# 用途：生成一个nxn的矩阵
def matrix(n):
    matrix = []  # 创建一个空列表 matrix 用于存储矩阵
    for i in range(n):  # 创建 n 行
        row = []  # 创建一个空列表 row 用于存储矩阵的一行
        for j in range(n):  # 创建 n 列
            row.append(i * n + j + 1)  # 计算并添加矩阵中的元素
        matrix.append(row)  # 将一行添加到矩阵中
    return matrix 

# 用途：将矩阵逆时针旋转 90 度（左旋）
def function_L(matrix):
    n = len(matrix)
    # 先进行矩阵转置
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 然后逆序每一行
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix

# 用途：将矩阵顺时针旋转 90 度（右旋）
def function_R(matrix):
    n = len(matrix)
    # 先进行矩阵转置
    for i in range(n):
        for j in range(i, n):
            # 交换矩阵的元素，将原矩阵的行和列交换位置
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 然后逆序每一列
    for i in range(n):
        # 使用切片 [::-1] 将每一列逆序
        matrix[i] = matrix[i][::-1]
    return matrix

# 用途：上下翻转矩阵
def function_U(matrix):
    return matrix[::-1]  # 使用切片[::-1]逆序矩阵的行来实现上下翻转

# 用途：左右翻转矩阵
def function_D(matrix):
    return [row[::-1] for row in matrix]  # 使用切片[::-1]逆序矩阵的每一行来实现左右翻转

n = int(input())  # 从用户输入获取矩阵的大小 n
initial_matrix = matrix(n)  # 生成初始矩阵
operations = input()  # 从用户输入获取操作序列

for op in operations:
    if op == 'L':  
        initial_matrix = function_L(initial_matrix)
    elif op == 'R': 
        initial_matrix = function_R(initial_matrix)
        
    elif op == 'U':
        initial_matrix = function_U(initial_matrix)
    elif op == 'D':
        initial_matrix = function_D(initial_matrix)
"""
省略寫法
initial_matrix = [function_L(initial_matrix) if op == 'L' else function_R(initial_matrix) for op in operations]
"""

for row in initial_matrix:  # 遍历最终的矩阵的每一行
    for x in row:  # 遍历每一行中的元素
        print(x, end=" ")  # 输出矩阵中的元素，用空格分隔
    print()  # 换行输出下一行
```
