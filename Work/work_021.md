# 題目：
**Q021. 梭哈類型**  
輸入5張牌，輸出牌型的類別編號，每張牌由牌面與花色組成，牌面與花色的表示如下：  
**牌面：** A、2~10、J、Q、K    
**花色：** S (Spade,黑桃), H (Heart,紅心), D (Diamond,方塊), C (Club,梅花)  
**例如：** 7S 表示黑桃7  

**牌型編號(編號越大代表牌型越大)：**  
1.	High Card : 單一張牌。  
2.	One pair: 兩張牌數字一樣  
3.	Two pairs : 兩組 Pair 的牌。  
4.	Three of a kind : 三張牌數字一樣。  
5.	Straight : 數字連續的五張牌，頭尾相接亦視為Straight。例如[2,3,4,5,6],..,[Q,K,A,2,3],[K,A,2,3,4], [A,2,3,4,5]  
6.	Flush : 五張同一花色的牌  
7.	Full House : Three of a Kind 加一個 Pair  
8.	Four of a kind: : 四張牌數字一樣  
9.	Straight flush : 數字連續的五張牌且花色一樣  

## 輸入說明：  
第一行：輸入一行字串，包含五張牌，每張牌中間以空白隔開  

## 輸出說明：    
第一行：輸出一個整數（1~9），表示最大的牌型編號  

**特別要求：**  
1.	如果一副牌中有不合法的輸入，像是不存在的牌面、花色，則輸出 ***Error input***  
2.	如果一副牌中有重複的牌出現，即一副牌當中有兩張以上牌面跟花色一模一樣，則輸出***Duplicate deal***"  
3.	如果"Error input"和"Duplicate deal"同時發生，則輸出***Error input***  

--------------
**範例輸入說明：**  
7S 7H 7D 6C 6S（表示 黑桃7 紅心7 方塊7 梅花6 黑桃6）  

**範例輸出說明：** 
7 （對應牌型為編號7的Full house）  

------------
# 測資  
**Example Input 1：**    
```
5S 5H 5D 5C 5R
```
**Example Output 1：**    
Error input  


**Example Input 2：**  
```
6S 6H 6D 6C 6S
```
**Example Output 2：**  
Duplicate deal


**Example Input 3：**  
AS 2H 3D 5C 6SS
**Example Output 3：**  
Error input


**Example Input 4：**  
AS 5C 3D 5C 6SS
**Example Output 4：**  
Error input


**Example Input 5：**  
AS 3S 5S 7S 9S
**Example Output 5：**  
6


**Example Input 6：**  
AS 3S 5S 7S 9D
**Example Output 6：**  
1


**Example Input 7：**  
JS QS AS 10S KS
**Example Output 7：**  
9


**Example Input 8：**  
AS JH JD AD 5C
**Example Output 8：**  
3


**Example Input 9：**  
6S 4S 6H 10S 2D
**Example Output 9：**  
2


**Example Input 10：**  
3S 3H 9D 3D 3C
**Example Output 10：**  
8


**Example Input 11：**  
AS 8D 5C 8C 8H
**Example Output 11：**  
4


**Example Input 12：**  
JS 9S KS 10S QD
**Example Output 12：**  
5


**Example Input 13：**  
7S 7H 7D 6C 6S
**Example Output 13：**  
7


**Example Input 14：**  
AH QH 3H KH 2H
**Example Output 14：**  
9


**Example Input 15：**  
8C 8D 7S 3H 9D
**Example Output 15：**  
2
