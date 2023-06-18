Soongsil, Korea, Hanyang = map(int, input().split())
if Soongsil + Korea + Hanyang >= 100:
    print('OK')
else:
    if Soongsil < Korea:
        if Hanyang < Soongsil:
            print('Hanyang')
        else:
            print('Soongsil')
    else:
        if Hanyang < Korea:
            print('Hanyang')
        else:
            print('Korea')