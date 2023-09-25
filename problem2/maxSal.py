

def findMaxSal(employees):
    maxSal = max(employees,key=lambda x:x["salary"])
    return maxSal

employees = [
    {
        "name" : "John", "salary" : 3000, "designation" : "developer"
    },
    {
        "name" : "Emma", "salary" : 4000, "designation" : "manager"
    },
    {
        "name" : "Kelly", "salary" : 3500, "designation" : "tester"
    },
]

maxSal = findMaxSal(employees)
print(maxSal)