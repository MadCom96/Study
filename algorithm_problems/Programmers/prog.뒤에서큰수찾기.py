w2i = [0] * 5
now = [0] * 5
ith = 0
done = False

def dfs(depth):
    global w2i, now, ith, done
    ith -= 1
    for i in range(6):
        ith += 1
        now[depth] = i
        if w2i == now: 
            done = True
            return
        if i != 0 and depth != 4:
            dfs(depth + 1)
            if done:
                return
        now[depth] = 0

def solution(word):
    global w2i
    
    letter2int = {' ': 0, 'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    i = 0
    for letter in word:
        w2i[i] = letter2int[letter]
        i+=1
    
    dfs(0)
    print(ith)

solution(input())