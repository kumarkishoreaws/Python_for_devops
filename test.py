# need to get john alone 

# step1: Split it like "an:aws:iam::123456789012:user" as separate and "john" as separate
# step2: give the occurance of 2nd pattern 
# step3: print the value


arn = "arn:aws:iam::123456789012:user/john"

print(arn.split("/")[1])