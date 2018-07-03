N, digits_sum = [int(i) for i in input().split()]
tickets = []

def func(N, res):
    if N < 0:
        tickets.append(res)
        return
    res1 = res+"1"
    res2 = res+"0"
    func(N-1, res1)
    func(N-1, res2)


func(N-1, "")

count = 0
for ticket in tickets:
    if (ticket[0:int(N/2)].count("1") == ticket[int(N/2):].count("1") and
    ticket.count("1") == digits_sum):
        count += 1
        print(ticket)
print(count)
