txt = "GEEKSFORGEEKS"
pat = "EKS"

post = txt.find(pat)
while post>=0:
    print(post,end=" ")
    post = txt.find(pat, post+1)
