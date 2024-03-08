# 題目 
一元二次方程式，ax^2 + bx + c = 0，輸入a, b, c, 求 方程式的兩個實根。
-----------------------------
## 輸入說明:  
第一個數(int) a  
第二個數(int) b  
第三個數(int) c  

-----------------------------
## 輸出說明:  
第一個實根 x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)  
第二個實根 x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)  

x1, x2 輸出到小數點第一位  
print("%.1f" %x1)  

-----------------------------
**Example Input 1**  
```
1  
-2  
1
```
 
**Example Output 1**  
>1.0  
1.0  

-------------------
**Example Input 2**  
```
7  
0  
0
```
**Example Output 2**  
>0.0  
0.0  

-------------------
**Example Input 3**  
```
1  
0  
-1
``` 
**Example Output 3**  
>1.0  
-1.0  

-------------------
**Example Input 4**  
```
41  
17  
-27
```
**Example Output 4**  
>0.6  
-1.0  

-------------------
**Example Input 5**  
```
-100  
100  
100  
```
**Example Output 5**  
>-0.6  
1.6  

---
# 代碼
``` python
import math
a = int(input())
b = int(input())
c = int(input())

x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
print("%.1f" %x1)
print("%.1f" %x2)
```
