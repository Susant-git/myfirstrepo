def fibbo():
    first,second = 0,1
    while True:
        yield first
        first,second = second,first+second
g = fibbo()
for i in g:
    if i>=100:
        break
    else:
        print(i)