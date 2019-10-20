def max_sequence(seq):
    sum=0
    maxsum=0
    for i in range(len(seq)-4):
                   if seq[i]+seq[i+1]+ seq[i+2] + seq[i+3] + seq[i+4] > sum:
                       sum = seq[i]+seq[i+1]+ seq[i+2] + seq[i+3] + seq[i+4]
                       a,b,c,d,e=seq[i],seq[i+1],seq[i+2],seq[i+3],seq[i+4]
                          
    print(a,b,c,d,e)
     
