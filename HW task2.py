Space = int(input()) 
des = 1
while space > -1:
        print(' '*space + '@'*des)
        des += 2
        space -= 1
