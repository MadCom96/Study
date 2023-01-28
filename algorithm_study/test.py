def earlier(m1, d1, m2, d2) -> bool:
    if m1 < m2:
        return True
    elif m1 == m2:
        if d1 <= d2:
            return True
        else:
            return False
    else:
        return False

for sm in range(5):
    for sd in range(5):
        for em in range(5):
            for ed in range(5):
                print(f'{sm}.{sd} ~ {em}.{ed}', earlier(sm, sd, em, ed))