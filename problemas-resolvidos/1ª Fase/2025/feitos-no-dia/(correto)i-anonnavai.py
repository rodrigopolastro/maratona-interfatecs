p = int(input())
for _ in range(p):
    do = int(input())
    da = int(input())
    if do+da > 40:
        if do>da:
            print("DOROTHY DECIDE E A NONNA VAI")
        else:
            print("DAGMAR DECIDE E A NONNA VAI")
    else:
        if do>da:
            print("DOROTHY DECIDE")
        else:
            print("DAGMAR DECIDE")