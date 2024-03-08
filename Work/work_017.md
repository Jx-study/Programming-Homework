# 題目：
**017. 課程衝堂（008的Pro版）**  
給定N門課程資料，檢查課程是否衝堂或輸入錯誤，輸出檢查結果。  
**依序輸入**:  
課程編號 (科目名稱 + 4位數字)、  
上課小時數 (1-3 小時)、  
上課時間 (依小時數輸入上課時間, 星期 1-5, 第 1-9,a,b,c 節)。  

-----------------------------------------------------------------------------------------------
## 輸入說明  
**第一行**：輸入整數N(2 <= N <= 10)  
接著輸入**N門課程**的資訊，每一門課程的輸入如下：  
　　**第一行**：輸入課程名稱及編號(字串)  
　　**第二行**：上課小時數，整數 H (1<=H<=3)  
　　接下來**H**行：  
　　　　每一行為一個字串，第一個字元表示星期幾，第二個字元表示第幾節  

## 輸出說明  
輸入有任何錯誤，輸出 -1  
若無發生衝堂，則輸出correct  
若發生衝堂，輸出所有衝堂的課程，每次輸出兩個衝堂的課程編號，以及在哪一天的哪一節衝突，參考下列格式 :  
***{課程1編號},{課程2編號},{衝堂在哪天哪節}***  
先輸入的課程為課程1，後輸入的課程為課程2   

-----------------------------------------------------------------------------------------------
**範例輸入說明**  
3 (總共有三門課程)  
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
**範例輸出說明**(兩課程編號衝突在哪幾節)  
Chinese1001,Math1003,13 (課程Chinese1001跟課程Math1003，在星期1第3節衝堂，因課程Chinese1001先輸入，所以課程Chinese1001放前面)  
<br>

-----------------------------------------------------------------------------------------------
# 測資
**Example Input 1**  
```
4  
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
History4001  
1  
23
```
**Example Output 1**  
>Programming1002,Biology1003,3b  
Programming1002,Math3003,3b  
Biology1003,Math3003,11  
Biology1003,Math3003,3b  
<br>

**Example Input 2**  
```
5  
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
Chinese5001  
2  
31  
32  
Math5002  
3  
42  
43  
44
```
**Example Output 2**  
>correct  
<br>

**Example Input 3**  
```
7  
Math1011  
2  
45  
46  
Chinese1002  
2  
45  
61  
English1003  
2  
45  
5a  
Chemistry1004  
1  
4c  
Biology2001  
3  
46  
47  
48  
Physics2002  
2  
5a  
5b  
Programming2003  
3  
45  
46  
47
```
**Example Output 3**  
>-1  
<br>

----
# 代碼：  
```python
# 課程衝堂
# 20231009

# 功能：用於檢查輸入的時間表是否符合輸入規則
def inputError(schedule):
    for time in schedule:
        if len(time) != 2 or time[0] not in "12345" or time[1] not in "123456789abc":
            print("-1")  # 輸入錯誤，輸出
            raise SystemExit()
    return None

# 功能：檢查兩個課程的時間表是否相同（存在衝堂）
def check(courseSchedule1, courseSchedule2, courseCode1, courseCode2):
    conflicts = []              # 存儲時間衝突的時間
    for time1 in courseSchedule1:
        if time1 in courseSchedule2:
            conflicts.append(time1)
    for time in conflicts:
        print(f"{courseCode1},{courseCode2},{time}")  # 单独输出每个时间冲突
    return conflicts

number_course = int(input())
courses = [] # 用來存儲課程信息的列表
for i in range(number_course):
    course_name = input()
    course_hour = int(input())
    schedules = []   # 用來存儲課程時間表的列表
    for time in range(course_hour):
        time = input()
        schedules.append(time)
    courses.append((course_name, schedules))

# 检查课程时间是否有错误    
for course_name, schedule in schedules:
    inputError(schedule)

# 檢查冲堂
conflicts_exist = False
for i in range(number_course - 1):
    for j in range(i + 1, number_course):
        course1_name, course1_schedule = courses[i]
        course2_name, course2_schedule = courses[j]
        if check(course1_schedule, course2_schedule, course1_name, course2_name):
            conflicts_exist = True

# 如果存在衝堂，不輸出 "correct"；否則，輸出 "correct"
if not conflicts_exist:
    print("correct")
```
