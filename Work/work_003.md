# 題目
分別輸入 num1 num2 求出兩數的 Sum,Difference,Product,Quotient。

結果須輸出到小數點第二位
***print("%.2f" %ans)***

---------------------------------------------------
## 輸入說明:  
第一行: 輸入數字num1  
第二行: 輸入數字num2  

---------------------------------------------------
## 輸出說明:  
第一行: Sum:num1+num2  
第二行: Difference:num1-num2  
第三行: Product:num1*num2  
第四行: Quotient:num1/num2  

加減乘除的結果，輸出到小數點後第二位  
***print("%.2f" %ans)***

---------------------------------------------------
**Example Input 1:**  
```
25  
2
```

**Example Output 1:**  
>Sum:27.00  
Difference:23.00  
Product:50.00  
Quotient:12.50  

--------------------------------
**Example Input 2:**  
```
-1  
6
```
 
**Example Output 2:**
>Sum:5.00  
Difference:-7.00  
Product:-6.00  
Quotient:-0.17  

--------------------------------
**Example Input 3:**  
```
0  
9
```  
**Example Output 3:**  
>Sum:9.00  
Difference:-9.00  
Product:0.00  
Quotient:0.00  


---
# 代碼
```python
# Type of Triangle
# 20230919
def getTriangle(a,b,c):

    if a+b <= c or a+c <= b or b+c <= a or a <= 0 or b <= 0 or c <= 0:
        return "not a triangle"
    
    if a==b and b==c: #OR a==b==c
        return"equilateral triangle"
    
    if a==b and (a**2 +b**2) > c**2 or b==c and (b**2 +c**2) > a**2 or a==c  and (a**2 +c**2) > b**2:
            return "isosceles triangle"
            
    x = [a,b,c]
    x.sort()
    if int(x[2])**2 == int(x[0])**2 + int(x[1])**2:
        return "right triangle"

    elif int(x[2])**2 < int(x[0])**2 + int(x[1])**2:
            return "acute triangle"

    elif int(x[2])**2 > int(x[0])**2 + int(x[1])**2:
            return "obtuse triangle"


a = int(input())
b = int(input())
c = int (input())

result = getTriangle(a, b, c)
print(result)
```
