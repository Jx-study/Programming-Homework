# 題目：
**008. 檢查輸入的三門課程是否衝堂**  
**依序輸入 :**  
課程編號 (科目名稱 + 4位數字)、  
上課小時數 (1-3 小時)、  
上課時間 (依小時數輸入上課時間, 星期 1-5, 第 1-9,a,b,c 節)。  

-----------------------------------------------------------------------------------------------
**輸入說明:**  
輸入三門課程的資訊  
每一門課程的資訊  
**第一行**：輸入課程編號(字串)  
**第二行**：上課小時數 H (整數，1<=H<=3)  
接下來有 ***H 行***  
每一行為一個字串，第一個字元表示星期幾，第二個字元表示第幾節  

**輸出說明:**
**情況一**：輸入任何錯誤，輸出 -1  
**情況二**：若無發生衝堂，則輸出correct  
**情況三**：若發生衝堂  
輸出所有衝堂的課程，每次輸出兩個衝堂的課程編號，以及在哪一天的哪一節衝突，參考下列格式 :  
{課程1編號},{課程2編號},{衝堂在哪天哪節}  
先輸入的課程為課程1，後輸入的課程為課程2  

-----------------------------------------------------------------------------------------------
**範例輸入說明:**

Chinese1001 (第一門課課程編號)  
3 (3小時，每節課1小時)  
11 (星期1 第1節課)  
12 (星期1 第2節課)  
13 (星期1 第3節課)  
English1002 (第二門課課程編號)  
3 (3小時，每節課1小時)  
21 (星期2 第1節課)  
22 (星期2 第2節課)  
23 (星期2 第3節課)  
Math1003 (第三門課課程編號)  
3 (3小時，每節課1小時)  
31 (星期3 第1節課)  
32 (星期3 第2節課)  
13 (星期1 第3節課)  

**範例輸出說明：**(兩課程編號衝突在哪幾節)  
Chinese1001,Math1003,13 (課程Chinese1001跟課程Math1003，在星期1第3節衝堂，因課程Chinese1001先輸入，所以課程Chinese1001放前面)  

-----------------------------------------------------------------------------------------------
**Example Input 1 :**  
Programming1002  
2  
3b  
4c  
Biology1003  
2  
11  
3b  
Math3003  
2  
11  
3b  

**Example Output 1:**  
Programming1002,Biology1003,3b  
Programming1002,Math3003,3b  
Biology1003,Math3003,11  
Biology1003,Math3003,3b  

-----------------------------------------------------------------------------------------------
**Example Input 2:**  
Physics3000  
1  
37  
Biology2004  
3  
2a  
2b  
2c  
Chemistry1003  
1  
1c  

**Example Output 2:**  
correct  

-----------------------------------------------------------------------------------------------
**Example Input 3:**  
Math1011  
1  
46  
Chinese1002  
2  
45  
46  
English1003  
2  
61  
5a  

**Example Output 3:**  
-1  

----
## 代碼：
**版本一**：版本一與二的差別就是這個是用set(無順序)，而版本二是用list（有順序）  
```python
# 檢查輸入的三門課程是否衝堂
# 20230929

def inputError(schedule):
    for time in schedule:
        if len(time) != 2 or time[0] not in "12345" or time[1] not in "123456789abc":
            print("-1")  # 輸入錯誤，輸出
            raise SystemExit()
    return None

course1 = set()
course1_code = input()
hours_1 = int(input())  # 上課小時數
schedule_1 = [input() for _ in range(hours_1)]
course1.update(schedule_1)  # 使用update将时间字符串添加到course1中

course2 = set()
course2_code = input()
hours_2 = int(input())  # 上課小時數
schedule_2 = [input() for _ in range(hours_2)]
course2.update(schedule_2)

course3 = set()
course3_code = input()
hours_3 = int(input())  # 上課小時數
schedule_3 = [input() for _ in range(hours_3)]
course3.update(schedule_3)

inputError(schedule_1)
inputError(schedule_2)
inputError(schedule_3)

def check(courseSchedule1, courseSchedule2, courseCode1, courseCode2):
    conflicts = set(courseSchedule1) & set(courseSchedule2)
    if conflicts:
        return f"{courseCode1},{courseCode2}", conflicts  # 返回冲突的课程和时间
    return None

conflicts = []
conflict1 = check(course1, course2, course1_code, course2_code)
if conflict1:
    course_codes, time_conflicts = conflict1
    for time in time_conflicts:
        print(f"{course_codes},{time}")
    conflicts.append(conflict1)
    
conflict2 = check(course1, course3, course1_code, course3_code)
if conflict2:
    course_codes, time_conflicts = conflict2
    for time in time_conflicts:
        print(f"{course_codes},{time}")
    conflicts.append(conflict2)

conflict3 = check(course2, course3, course2_code, course3_code)
if conflict3:
    course_codes, time_conflicts = conflict3
    for time in time_conflicts:
        print(f"{course_codes},{time}")
    conflicts.append(conflict3)
    
if not conflicts:
    print("correct")
```

**版本二：**
```python
# 檢查輸入的三門課程是否衝堂
# 20230927

# 用於檢查輸入的時間表是否符合輸入規則
def inputError(schedule):
    for time in schedule:
        if len(time) != 2 or time[0] not in "12345" or time[1] not in "123456789abc":
            print("-1")  # 輸入錯誤，輸出
            raise SystemExit()
    return None

# 創建三個課程的時間表
course1 = []
course1_code = input()
hours_1 = int(input())  # 上課小時數
schedule_1 = [input() for _ in range(hours_1)]
course1.extend(schedule_1)  # 使用extend将时间字符串添加到course1中

course2 = []
course2_code = input()
hours_2 = int(input())  # 上課小時數
schedule_2 = [input() for _ in range(hours_2)]
course2.extend(schedule_2)

course3 = []
course3_code = input()
hours_3 = int(input())  # 上課小時數
schedule_3 = [input() for _ in range(hours_3)]
course3.extend(schedule_3)

# 呼叫inputError(schedule_X)函數
inputError(schedule_1)
inputError(schedule_2)
inputError(schedule_3)

# 檢查兩個課程的時間表是否相同（存在衝堂）
def check(courseSchedule1, courseSchedule2, courseCode1, courseCode2):
    conflicts = []              # 存儲時間衝突的時間
    for time1 in courseSchedule1:
        if time1 in courseSchedule2:
            conflicts.append(time1)
    for time in conflicts:
        print(f"{courseCode1},{courseCode2},{time}")  # 单独输出每个时间冲突
    return conflicts

# 呼叫check函數
conflict1 = check(course1, course2, course1_code, course2_code)
conflict2 = check(course1, course3, course1_code, course3_code)
conflict3 = check(course2, course3, course2_code, course3_code)

# 檢查是否有任何衝堂存在
if not (conflict1 or conflict2 or conflict3):
    print("correct")
```
