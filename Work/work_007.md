# 題目  
**007. 最佳資費選擇**  
輸入每月網內、網外、市話、通話時間(秒)及網內、網外簡訊則數、網路流量，求最佳資費。  
費率如下表：  
![GitHub 图标](https://i.imgur.com/j14Hm41.png))

**優惠內容月租費可抵等額通信費 :**  
若低於該資費類型的費用，則以該資費類型的費用進行收費。  

**例如:**  
選擇183型，總通信費為200元，則應繳金額為200元  
若總通信費為150元，則應繳金額為183元。  

---------------------------------------------------
**輸入說明：**  

**第一行**：輸入網內語音(秒, Integer)    
**第二行**：輸入網外語音(秒, Integer)  
**第三行**：輸入市話(秒, Integer)  
**第四行**：輸入網內簡訊數(Integer)  
**第五行**：輸入網外簡訊數(Integer)  
**第六行**：輸入網路流量(G)(Integer)  

---------------------------------------------------
**輸出說明：**  

**第一行**：輸出費用(Integer)  
**第二行**：輸出最佳資費類型，(183, 383, 983, 1283)  

---------------------------------------------------
**Example Input 1**  
100  
200  
10  
10  
10  
2  
**Example Output 1**  
313  
183  

---------------
**Example Input 2 **  
1500  
1800  
100  
30  
30  
2  
**Example Output 2**  
429  
383  

---------------
**Example Input 3**  
1000  
2000  
50  
50  
20  
7  
**Example Output 3**  
983  
983  

---------------
**Example Input 4**  
9000  
9000  
60  
200    
50  
3  
**Example Output 4**  
1655  
1283  

----
## 代碼：
#### 版本一
```python
incall = int(input()) #網內語音
outcall = int(input()) #網外語音
citycall = int(input()) #市話
inmsg = int(input()) #網內簡訊數
outmsg = int(input()) #網外簡訊數
internet1 = int(input()) #網路流量
internet2 = internet1
internet3 = internet1

# 處理網路流量的特殊情況（如沒用流量）
# 確保網路流量不會小於某個最低值，以便計算費用
if (internet1 == 0):
    internet1 = 1
elif(internet2 <3):
    internet2 = 3
elif(internet3 < 5):
    internet3 = 5

# 判斷縂通信費高於還是低於資費類型的費用
fee1 = max(incall*0.08 + outcall*0.139 + citycall*0.135 + inmsg*1.128 +outmsg*1.483+ (internet1-1)*250,183)
fee2 = max(incall*0.07 + outcall*0.130 + citycall*0.121 + inmsg*1.128 +outmsg*1.483+ (internet2-3)*200,383)
fee3 = max(incall*0.06 + outcall*0.108 + citycall*0.101 + inmsg*1.128 +outmsg*1.483+ (internet3-5)*150,983)
fee4 = max(incall*0.05 + outcall*0.100 + citycall*0.090 + inmsg*1.128 +outmsg*1.483,1283)

# 輸出費用
fee = int(min(fee1,fee2,fee3,fee4))
print(fee)

# 輸出最佳的配套
if(fee < 383):
    print("183")
elif(fee < 983):
    print("383")
elif(fee < 1283):
    print("983")
else: 
    print("1283")
```

### 版本二
```python
incall = int(input())  # 網內語音(秒)
outcall = int(input())  # 網外語音(秒)
citycall = int(input())  # 市話(秒)
inmsg = int(input())  # 網內簡訊數
outmsg = int(input())  # 網外簡訊數
internet1 = int(input())  # 網路流量(G)

# 定義資費類型和對應的費率
fee_plans = {
    183: {"voice_in": 0.08, "voice_out": 0.139, "landline": 0.135, "sms_in": 1.128, "sms_out": 1.483, "data_base": 30},
    383: {"voice_in": 0.07, "voice_out": 0.130, "landline": 0.121, "sms_in": 1.128, "sms_out": 1.483, "data_base": 50},
    983: {"voice_in": 0.06, "voice_out": 0.108, "landline": 0.101, "sms_in": 1.128, "sms_out": 1.483, "data_base": 100},
    1283: {"voice_in": 0.05, "voice_out": 0.100, "landline": 0.090, "sms_in": 1.128, "sms_out": 1.483, "data_base": 200}
}

# 計算網路流量費用，至少為基本費用
internet1_fee = max((internet1 - 1) * 250, fee_plans[183]["data_base"])
internet2_fee = max((internet1 - 3) * 200, fee_plans[383]["data_base"])
internet3_fee = max((internet1 - 5) * 150, fee_plans[983]["data_base"])

# 計算各種資費類型的費用
fees = {
    183: incall * fee_plans[183]["voice_in"] + outcall * fee_plans[183]["voice_out"] +
         citycall * fee_plans[183]["landline"] + inmsg * fee_plans[183]["sms_in"] +
         outmsg * fee_plans[183]["sms_out"] + internet1_fee,
    
    383: incall * fee_plans[383]["voice_in"] + outcall * fee_plans[383]["voice_out"] +
         citycall * fee_plans[383]["landline"] + inmsg * fee_plans[383]["sms_in"] +
         outmsg * fee_plans[383]["sms_out"] + internet2_fee,
    
    983: incall * fee_plans[983]["voice_in"] + outcall * fee_plans[983]["voice_out"] +
         citycall * fee_plans[983]["landline"] + inmsg * fee_plans[983]["sms_in"] +
         outmsg * fee_plans[983]["sms_out"] + internet3_fee,
    
    1283: incall * fee_plans[1283]["voice_in"] + outcall * fee_plans[1283]["voice_out"] +
          citycall * fee_plans[1283]["landline"] + inmsg * fee_plans[1283]["sms_in"] +
          outmsg * fee_plans[1283]["sms_out"] + internet1_fee
}

# 找出最低費用和對應的資費類型
best_plan, best_cost = min(fees.items(), key=lambda x: x[1])

# 輸出結果
print(best_cost)
print(best_plan)
```
