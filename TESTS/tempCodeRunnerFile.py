 r

    while l < r:
        mid = (r - l) // 2
        resh = 0
        for p in piles:
            resh += p // mid + 1
        
        if resh <= h:
            res = min(res, mid)
            r = mid - 1
        elif resh > h:
            l = mid + 1
    return res