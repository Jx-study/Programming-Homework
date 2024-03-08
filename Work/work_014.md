# 題目：
**014. 保齡球**  
小明到保齡球館打保齡球,一輪有十局，試算總分，保齡球規則如下:  
(1)每局有10個保齡球瓶，擊倒1個球瓶得1分  
(2)每局最多有兩次投球機會  
(3)當局如果第一球將10個保齡球瓶全部擊倒(稱為**strike**)，當局只有一次投球機會， 此局計分除了10分外，再加上後面兩球擊倒的球瓶數。  
(4)當局如果第一球未將10個保齡球瓶全部擊倒，但加上第二球則將10個保齡球瓶全部擊倒(稱為**spare**)，此局計分除了10分外，再加上後面一球擊倒的球瓶數。  
(5)當局若兩球都無法將球瓶全部擊倒，此局計分為兩球擊倒的球瓶數。  
(6)第10局如果第一球將球瓶全部擊倒，後面還有2次投球機會。  
(7)第10局如果第二球才將球瓶全部擊倒，後面還有1次投球機會。  
(8)第10局若兩球都無法將球瓶全部擊倒，則結束比賽。  
(9)總分為10局分數總合。  


## 輸入說明 
第1局第一球分數(int,0\~10)  
第1局第二球分數(上一球為10則省略) (int,和上一球總和最多為10)  
:    
:    
第9局第一球分數 (int,0\~10)  
第9局第二球分數(上一球為10則省略) (int,和上一球總和最多為10)  
第10局第一球分數 (int,0~10)  
第10局第二球分數(上一球為10則省略) (int,和上一球總和最多為10)  
第一次額外投球分數(第10局投球總分為10才輸入) (int,0\~10)  
第二次額外投球分數(第10局第一球為10才輸入) (int,0\~10)  

## 輸出說明
總分 (int)  
<br>

---------------------------------------------------------------------------------------------------------------------
**範例輸入說明:**  
5(第1局第一球)  
5(第1局第二球) (因為spare，第一局分數為該局投球得分加下一次投球分數，為13分)  
3(第2局第一球)   
2(第2局第二球)(第二局分數為該局得分，為5分)  
6(第3局第一球)  
4(第3局第二球)(因為spare，第三局分數為該局投球得分加下一次投球分數，為20分)  
10(第4局第一球)(因為strike，第四局分數為該局投球得分加下二次投球分數，為19分)  
7(第5局第一球)  
2(第5局第二球)(第五局分數為該局投球得分，為9分)  
9(第6局第一球)  
1(第6局第二球)(因為spare，第六局分數為該局投球得分加下一次投球分數，為20分)  
10(第7局第一球)(因為strike，第七局分數為該局投球得分加下二次投球分數，為20分)  
8(第8局第一球)  
2(第8局第二球)(因為spare，第八局分數為該局投球得分加下一次投球分數，為16分)  
6(第9局第一球)   
2(第9局第二球)(第九局分數為該局投球得分，為8分)  
10(第10局第一球)(因為strike，第十局分數為該局投球得分加下二次投球分數，為18分)  
0(因為第10局第一次就全倒，第一次額外投球)  
8(因為第10局第一次就全倒，第二次額外投球)  

![](https://i.imgur.com/bArZ2St.png)

**範例輸出說明:**  
148 (每局分數總和。為13+5+20+19+20+20+16+8+18)  
<br>

---------------------------------------------------------------------------------------------------------------------
# 測資
**Example Input 1:**  
```
2  
5  
7  
1  
3  
4  
6  
2  
4  
3  
5  
1  
6  
3  
7  
2  
8  
1  
3  
5  
```
![](https://i.imgur.com/8Uq8kJ2.png)  

**Example Output 1:**   
>78  
<br>

**Example Input 2:**  
```
10  
5  
5  
10  
2  
8  
10  
4  
6  
10  
7  
3  
10  
1  
9  
10  
```
![](https://i.imgur.com/AS5itc0.png)  

**Example Output 2:**  
>200  
<br>

----
# 代碼：  
## 版本一  
```python
# 計算保齡球分數(未完成-有漏洞)
# 20231006

def calculateScore(scores):
    total_score = 0
    frame = 1
    roll = 1 
    
    for i in range(len(scores)):
        score = scores[i]
        total_score += score
        print(total_score)
        if frame < 10:
            if roll == 1:
                if score == 10:  # Strike-加后两球
                    total_score += scores[i + 2] + scores[i + 3] # 因爲下一項(第二項)為0
                    frame += 1
                else:
                    roll = 2
            else:
                if roll == 2 and scores[i - 1] + score == 10:  # 打了两球没有全倒
                    total_score += scores[i + 1]
                frame += 1
                roll = 1

        elif frame == 10:
            if roll == 1 and score == 10:  # 第十局strike
                extra_roll_1 = scores[i + 1]
                extra_roll_2 = scores[i + 2] if i + 2 < len(scores) else 0  # 检查是否有足够的数据
                total_score += extra_roll_1 + extra_roll_2
                break  
            elif roll == 2 and score + scores[i - 1] == 10:  # 第十局spare
                extra_roll_1 = scores[i + 1]
                total_score += extra_roll_1
                break
    return total_score
        
# 存储分数
scores = []
for i in range(10):
    firstRoll = int(input())
    
    if firstRoll != 10:
        secondRoll = int(input())
    else:
        secondRoll = 0  # 如果为strike   
    scores.extend([firstRoll, secondRoll])

# 處理第10局的額外球-第一球是strike
if scores[-2] == 10:
    extraRoll_1 = int(input())
    extraRoll_2 = int(input())
    scores.extend([extraRoll_1, extraRoll_2])

# 第十局为spare
elif scores[-1] + scores[-2] == 10:
    extraRoll_1 = int(input())
    extraRoll_2 = 0
    scores.extend([extraRoll_1, extraRoll_2])

total_score = calculateScore(scores)
print(total_score)
```

## 版本二  
```python
# 計算保齡球分數
# 20231006

scores = []

# 输入每一局的分数，并将其添加到scores中
for i in range(1, 11):
    frame = []  # 表示一局的分数
    firstRoll = int(input())
    
    if firstRoll != 10:
        secondRoll = int(input())
    else:
        secondRoll = 0  # 如果为strike   
    frame.extend([firstRoll, secondRoll])
        
    scores.append(frame)

# 如果第10局的第一球是strike，有两个额外球
extra = []
if scores[9][0] == 10:
    extraBall_1 = int(input())
    extraBall_2 = int(input())
    extra.extend([extraBall_1,extraBall_2])
    
# 如果第10局的第一球是spare，有一个额外球
elif sum(scores[9]) == 10:
    extraBall_1 = int(input())
    extra.append(extraBall_1)

# 计算总分
total_score = 0
for i in range(10):
    frame = scores[i]
    total_score += sum(frame)
    
    if i < 9:
        # 如果是strike，计算额外的分数
        if frame[0] == 10:
            if scores[i + 1][0] == 10: # 若下一局是strike
                if i + 2 < 10:
                    total_score += scores[i + 1][0] + scores[i + 2][0]
                else:
                    total_score += scores[i + 1][0] + extra[0]
            else:
                total_score += sum(scores[i + 1])
        
        # spare
        elif sum(frame) == 10:
            total_score += scores[i + 1][0]
    
    else:
        total_score += sum(extra)
    
# 输出总分
print(total_score)
```
