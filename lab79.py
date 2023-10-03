X = input("enter the sentence:")
is_pangram = True
for ch in range(ord('a'),ord('z') + 1):
    char = chr(ch)
    if char not in X.lower():
        is_pangram = False
        break
    
if is_pangram:
    print("it is pangram")
else:
    print("it is not pangram")
     
  
        