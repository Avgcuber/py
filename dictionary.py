import operator
d={'b':4,'c':2,'a':1,'d':3}
sasc=dict(sorted(d.items(),key=operator.itemgetter(1)))
sasc1=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
sdesc=dict(sorted(d.items(),key=operator.itemgetter(0)))
sdesc1=dict(sorted(d.items(),key=operator.itemgetter(0),reverse=True))
print("Original Dictionary : ",d)
print("Ascending Order by Value : ",sasc)
print("Descending Order by Value : ",sasc1)
print("Ascending Order by Key : ",sdesc)
print("Descending Order by Key : ",sdesc1)
