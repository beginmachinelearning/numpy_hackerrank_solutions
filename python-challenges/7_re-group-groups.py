str = str(int(input()))
h={}
p=-1
done=0
for ch in str:
 
        # If character is already present
        # in hash, return char
        if (ch == h and done==0):
            p=ch;
            done=1
 
        # Add ch to hash
        else:
            h[ch] = 0