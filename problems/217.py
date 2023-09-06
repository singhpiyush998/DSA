def containsDuplicate(nums):
    dt = {}
    for i in nums:
        if dt.get(i) != None:
            return True
        dt[i] = True
    return False
