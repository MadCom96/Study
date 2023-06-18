# cache가 가득찼을때
# cache hit 인가?
#     맞다면 : 시간만 갱신
#     아니라면 : 시간갱신, 현재 있는 cache중에서 가장 빨리 들어온거 빠지기, 새로 넣기

def solution(cacheSize, cities):
    cache = []
    time = 0 
    for city in cities:
        city = city.lower()

        cache.append(city)
        idx = cache.index(city)
        if idx != len(cache)-1: # 안에 있을때
            time += 1
            cache.pop(idx)
        else: # 안에 없을 때
            time += 5
            if len(cache) > cacheSize:
                cache.pop(0)
    return time


if __name__ == "__main__":
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution(cacheSize, cities))

    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
    print(solution(cacheSize, cities))

    cacheSize = 2
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	
    print(solution(cacheSize, cities))

    cacheSize = 5
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	
    print(solution(cacheSize, cities))

    cacheSize = 2
    cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
    print(solution(cacheSize, cities))

    cacheSize = 0
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution(cacheSize, cities))