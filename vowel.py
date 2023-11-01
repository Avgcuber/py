def vowel(s):
    v="aeiouAEIOU"
    l2=[l1 for l1 in s if l1 in v]
    print(l2,"-",len(l2))
vowel("When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.")
