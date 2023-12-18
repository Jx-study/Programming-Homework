# 題目：  
**010. 計算保齡球分數(第9+10局)**  
小明到保齡球館打保齡球,一輪有十局,假設小明一到八局都拿零分,剩下最後兩局，試算總分，保齡球規則如下:   
(1) 每局有10個保齡球瓶，擊倒1個球瓶得1分  
(2) 每局最多有兩次投球機會  
(3) 當局如果第一球將10個保齡球瓶全部擊倒(稱為strike)，當局只有一次投球機會，此局計分除了10分外，再加上後面兩球擊倒的球瓶數。  
(1) 當局如果第一球未將10個保齡球瓶全部擊倒，但加上第二球則將10個保齡球瓶全部擊倒(稱為spare)，此局計分除了10分外，再加上後面一球擊倒的球瓶數。  
(5)當局若兩球都無法將球瓶全部擊倒，此局計分為兩球擊倒的球瓶數。  
(6)第10局如果第一球將球瓶全部擊倒，後面還有2次投球機會。  
(7) 第10局如果第二球才將球瓶全部擊倒，後面還有1次投球機會。  
(8) 第10局若兩球都無法將球瓶全部擊倒，則結束比賽。  
(9)總分為10局分數總合。  

-----------------------------------------------------------------------------------------------------------------------
**輸入說明:**  
**第一行**：第9局第一球分數 (int,0~10)  
**第二行**：第9局第二球分數(上一球為10則省略) (int,和上一球總和最多為10)  
**第三行**：第10局第一球分數 (int,0~10)  
**第四行**：第10局第二球分數(上一球為10則省略) (int,和上一球總和最多為10)  
**第五行**：第一次額外投球分數(第10局投球總分為10才輸入) (int,0~10)  
**第六行**：第二次額外投球分數(第10局第一球為10才輸入) (int,0~10)  

**輸出說明:**  
總分 (int)  

---------------------------------------------------------------------------------------------------------------------
**範例輸入說明**  
5(第9局第一球)  
5(第9局第二球)  
10(第10局第一球)  
0(因為第10局第一次就全倒，第一次額外投球)  
8(因為第10局第一次就全倒，第二次額外投球)  

**範例輸出說明**  
34(第9局兩次全倒，分數為5+5+10=20。第10局一次全倒，分數為10+0+8=18。總分為20+18=38)  

---------------------------------------------------------------------------------------------------------------------
**Example Input1:**  
2  
5  
7  
1  
**Example Output1:**  
15  

----------------------------------------------------------------------------------------------------------------------
**Example Input2:**  
5  
5  
10  
0  
8  
**Example Output2:**  
38  

------------------------------------------------------------------------------------------------------------------
**Example Input3:**  
3  
1  
10  
1  
3  
**Example Output3:**
18  

----
## 代碼：
```python
#計算保齡球分數
#20230927

FirstRoll_9 = int(input())
total_score = 0

# 计算第9局总分
total_score += FirstRoll_9
if FirstRoll_9 < 10:
    SecondRoll_9 = int(input())
    FirstRoll_10 = int(input())
    if FirstRoll_9 + SecondRoll_9 == 10:
        total_score += SecondRoll_9 + FirstRoll_10
    else:
        total_score += SecondRoll_9

elif FirstRoll_9 ==10:
    if FirstRoll_10 == 10:
        FirstRoll_extra = int(input())
        total_score += FirstRoll_10 + FirstRoll_extra
    else:
        SecondRoll_10 = int(input())
        total_score += FirstRoll_10 + SecondRoll_10
        
total_score += FirstRoll_10
if FirstRoll_10 < 10:
    SecondRoll_10 = int(input())
    total_score += SecondRoll_10
    if FirstRoll_10 + SecondRoll_10 == 10:  # 如果第10局是spare
        FirstRoll_extra = int(input())
        total_score += FirstRoll_extra

elif FirstRoll_10 == 10:  # 如果第10局第一球是strike  
    FirstRoll_extra = int(input())
    SecondRoll_extra = int(input())
    total_score += FirstRoll_extra + SecondRoll_extra

print(total_score)
```