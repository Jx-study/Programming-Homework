# 題目
某一學生修國文Chinese、計算機概論CS、計算機程式設計PD三科，使用者輸入名字(string)、學號(int)、三科成績(int)。
請輸出學生名字、學號，並計算其平均成績與總分。

---------------------------------------------------

輸入說明 :  
第一行，輸入學生名字  
第二行，輸入學生學號  
第三行，輸入學生國文成績  
第四行，輸入學生計算機概論成績  
第五行，輸入學生計算機程式設計成績  

輸出說明 :  
第一行輸出 Name:學生名字  
第二行輸出 ID:學生學號  
第三行輸出 Average:學生三科成績之平均 (保留整數即可)  
第四行輸出 Total:學生三科成績之總分  

---------------------------------------------------
Example Input 1:  
```
Tom  
905067  
100  
100  
100  
```

Example Output 1:  
>Name:Tom  
ID:905067  
Average:100  
Total:300  

-------------------------
Example Input 2:  
```
Ray  
106590035  
99  
90  
82  
```

Example Output 2:  
>Name:Ray  
ID:106590035  
Average:90  
Total:271  

-------------------------  
Example Input3:  
```
David  
42015632  
0  
0  
0  
```

Example Output 3:  
>Name:David  
ID:42015632  
Average:0  
Total:0  

---
## 代碼
```python
name = str(input())
studentID = int(input())
Chinese = int(input())
CS = int(input())
PD = int(input())

Total = Chinese + CS + PD
A = Total//3

"""
可使用1)"字串..."+變數名稱（備注：如果是數字需在前面加str，將數字改爲字串）
      2）f"字串.....{變數名稱}"
"""
print( "\nName:" +name)
print("ID:"+str(studentID))
print("Average:"+str(A))
print(f'Total:{Total}')
```
