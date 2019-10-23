from collections import Counter

with open ("moby_clean.txt","r") as file:
    text= file.read()
    l= list(text.split())
    counts= Counter(l)
    print(counts.most_common(5))
