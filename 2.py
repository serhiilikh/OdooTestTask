res = ""
for i in range(20):
    for x in range(26):
        tmp = chr(x+97)
        for y in range(26):
            tmp2 = chr(y+97)
            for z in range(26):
                tmp3 = chr(z+97)
                res += tmp+tmp2+tmp3
res = res[:1000000]
# проверка
# print(res.count("a"))
# print(res.count("ab"))
# print(res.count("abc"))
