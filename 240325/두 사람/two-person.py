[age_a,gender_a]=input().split()
[age_b,gender_b]=input().split()

if (int(age_a) > 18 and gender_a=='M') or (int(age_b)>18 and gender_b=='M'):
    print(1)

else :
    print(0)