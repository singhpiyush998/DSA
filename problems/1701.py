"""

"""

def averageWaitingTime(customers: list[list[int]]) -> float:
    eTime, totalWaitTime = 0, 0
    for customer in customers:
        aTime, pTime = customer
        if aTime >= eTime:
            eTime = aTime + pTime
        else:
            eTime = eTime + pTime

        totalWaitTime += eTime - aTime

    return totalWaitTime / len(customers)

print(averageWaitingTime([[1,2],[2,5],[4,3]]))
print(averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
