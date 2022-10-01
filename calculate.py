def calculate(min, max, step):
# 請用你的程式補完這個函式的區塊
    sum=0
    for x in range(min,max+1,step):
        sum+=x
    print(sum)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def avg(data):
# 請用你的程式補完這個函式的區塊
    i=0
    totalsalary=0
    round=0
    for x in range(i,len(data["employees"])):
        # print(data["employees"])

        if data["employees"][x]["manager"]==False:
            totalsalary+=data["employees"][x]["salary"]
            round+=1
    avg=totalsalary/round
    print(avg)
avg({
    "employees":[
                {
                "name":"John",
                "salary":30000,
                "manager":False
                },
                {
                "name":"Bob",
                "salary":60000,
                "manager":True
                },
                {
                "name":"Jenny",
                "salary":50000,
                "manager":False
                },
                {
                "name":"Tony",
                "salary":40000,
                "manager":False
                }
                ]
    }) 
    # 呼叫 avg 函式


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 關鍵字:inner

def func(a):
# 請用你的程式補完這個函式的區塊
    def func(b,c):
        print(a+(b*c))
    return func
    

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    max1=0
    max2=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            product = nums[i]*nums[j]
            if(product > max1):
                max1 = product
            elif(product < max2):
                max2 = product
                max1 = max2
    print(max1)
                
            

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def twoSum(nums, target):
# your code here
    dict = {}
    list = []
    for x in range(len(nums)):
        targetTemp = nums[x]
        key = target - targetTemp
        if(key in dict):
            list.append(dict[key])
            list.append(x)
            return list
        else:
            dict[targetTemp] = x 


result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


            