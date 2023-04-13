def strStr(haystack: str, needle: str) -> int:
    lenn = len(needle)
    for i in range(len(haystack)-lenn):
        if haystack[i:i+lenn] == needle:
            return i
    print(haystack[0:lenn-1])
    return -1

print(strStr("sadbutsad", "sad"))