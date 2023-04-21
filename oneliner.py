import re
pi='3141592653589793238462643383279'
wantedlist=['314','49','9001', '15926535897','9323', '14', '8462643383279','4','793']
howmanyspaces= (g:=len([pi[x[0][0]:x[0][1]]  for x in zip(no1, no1[1:]) if (x[0][1] == x[1][0])])) if (no1:=[(x.span()[0],x.span()[1]) for x in re.finditer("|".join(sorted(wantedlist,reverse=True)),pi) ])[-1][-1] == len(pi) else g+1
print(howmanyspaces)
