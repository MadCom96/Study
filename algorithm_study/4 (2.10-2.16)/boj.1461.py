# 도서관
n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

ends = [0]
ans = 0
if books[0] < 0:
    i = 0
    ends.append(abs(books[0]))
    while 0 <= i < len(books) and books[i] < 0:
        ans += 2 * abs(books[i])
        if 0 <= i + m - 1 < len(books) and books[i + m - 1] < 0:
            i += m
        else:
            break

if books[-1] > 0:
    i = -1
    ends.append(books[-1])
    while 0 <= i + len(books) < len(books) and books[i] > 0:
        ans += 2 * abs(books[i])
        if len(books) > len(books) + (i - m + 1) >= 0 and  books[i - m + 1] > 0:
            i -= m
        else:
            break

print(ans - max(ends))