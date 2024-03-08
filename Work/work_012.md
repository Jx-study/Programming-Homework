# 題目：
**012. 撲克牌**   
撲克牌的牌面符號A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K，對應的點數：  
2\~10 點數為 2~10，A, J, Q, K 為 0.5。  
一位玩家一位莊家，各發三張撲克牌，加總點數**越接近 10.5** 的贏；  
如果總點數相同，則雙方**平手 (Tie)**    
總點數超過***10.5 (不含10.5)***，點數變為 0。  

以兩種規則決定**勝負**：  
**規則一**：先加總玩家總點數，如果玩家點數為0則不需加總莊家點數，此時莊家獲勝。  
**規則二**：玩家與莊家總點數都計算完後才判斷勝負。   


## 輸入說明  
**第一行**：輸入玩家的名字(字串)  
**第二 ~ 四行**：輸入玩家的三張撲克牌  
**第五行**：輸入莊家的名字(字串)  
**第六 ~ 八行**：輸入莊家的三張撲克牌  

## 輸出說明  
**第一行**：以第一種規則判斷，輸出「勝利者的名字 Win」，若雙方平手，輸出Tie  
**第二行**：以第二種規則判斷，輸出「勝利者的名字 Win」，若雙方平手，輸出Tie  

-------------------------------------------------------------------
**範例輸入說明:**  
X (玩家的 名字 為 X)  
A (玩家的 第一張 撲克牌為 A)  
9 (玩家的 第二張 撲克牌為 9)  
3 (玩家的 第三張 撲克牌為 3)  
Y (莊家的 名字 為 Y)  
6 (莊家的 第一張 撲克牌為 4)  
8 (莊家的 第二張 撲克牌為 8)  
Q (莊家的 第三張 撲克牌為 Q)  

**範例輸出說明:**  
Y Win  
(以第一種規則判斷：玩家的總點數為0.5 + 9 + 3 = 12.5，因為玩家總點數超過10.5，所以玩家點數變為0，莊家獲勝)  
Tie  
(以第二種規則判斷：莊家的總點數為 6 + 8 + 0.5 = 14.5，因為玩家與莊家總點數都超過10.5，所以玩家與莊家總點數都變為0**平手**)  

-------------------------------------------------------------------
# 測資  
**Example Input 1：**  
```
C  
A  
6  
J  
D  
2  
K  
4  
```
**Example Output:**  
>C Win  
C Win  


**Example Input 2：**  
```
C  
2  
6  
K  
D  
A  
5   
3  
```
**Example Output 2：**  
>Tie  
Tie  


**Example Input 3：**  
```
S  
4  
2  
3  
R  
8  
2  
Q  
```
**Example Output 3：**  
>R Win  
R Win  


**Example Input 4：**  
```
C  
10  
9  
8  
D  
8  
9  
10  
```  
**Example Output 4：**  
>D Win  
Tie  


------
# 代碼：  
## 版本一  
```python
# 計算撲克牌點數
#20230928

player_name = input()
player_card1 = input()
player_card2 = input()
player_card3 = input()
banker_name = input()
banker_card1 = input()
banker_card2 = input()
banker_card3 = input()

A = J = Q = K = 0.5

def point(card1,card2,card3):
    def card_value(card):
        if card in ('A', 'J', 'Q', 'K'):
            return 0.5
        return float(card)
    
    sum_point = card_value(card1) + card_value(card2) + card_value(card3)
    if sum_point > 10.5:
        return 0
    return sum_point

point_player = point(player_card1,player_card2,player_card3)
point_banker = point(banker_card1,banker_card2,banker_card3)

def judgment():
    if point_player > point_banker:
        return f'{player_name} Win'
        
    elif point_player < point_banker:
        return f'{banker_name} Win'
    
    elif point_player == point_banker:
        return "Tie"
        
if point_player == 0:
    print(f'{banker_name} Win')
    
else:
    result = judgment()
    print(result)
    
result = judgment()
print(result)
```

## 版本二  
```python
# 输入玩家和莊家的名字
player_name = input()
player_cards = [input() for _ in range(3)]
banker_name = input()
banker_cards = [input() for _ in range(3)]

# 定义牌面点数映射
card_values = {'A': 0.5, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 0.5, 'Q': 0.5, 'K': 0.5}

# 计算玩家和莊家的点数
def calculate_points(cards):
    total_points = 0
    for card in cards:
        total_points += card_values.get(card, 0)  # 使用映射获取点数，未找到则默认为0
    if total_points > 10.5:
        return 0
    return total_points

player_points = calculate_points(player_cards)
banker_points = calculate_points(banker_cards)

# 根据第一种规则判定胜负
if player_points == 0:
    print(f'{banker_name} Win')
else:
    print(f'{player_name} Win' if player_points > banker_points else f'{banker_name} Win' if player_points < banker_points else 'Tie')

# 根据第二种规则判定胜负
if player_points > banker_points:
    print(f'{player_name} Win')
elif player_points < banker_points:
    print(f'{banker_name} Win')
else:
    print('Tie')
```
