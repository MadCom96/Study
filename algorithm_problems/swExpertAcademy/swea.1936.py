a, b = map(int, input().split())
winner = ''
if a > b:
    winner = 'A'
if b > a:
    winner = 'B'
print(winner)