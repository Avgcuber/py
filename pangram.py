def isp(s):
    a="abcdefghijklmnopqrstuvwxyz"
    for ch in a:
        if ch not in s.lower():
            return False
        return True
s="the quick brwon fox jumps over the lazy dog"
if isp(s)==True:
    print(s,"- IS A PANGRAM")
else:
    print(s,"- IS NOT A PANGRAM")
