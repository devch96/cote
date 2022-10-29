from collections import deque
def solution(cacheSize, cities):
    time = 0
    cities = [i.lower() for i in cities]
    cache = deque([])
    if cacheSize == 0:
        return 5 * len(cities)

    for i in cities:
        if i in cache:
            cache.remove(i)
            cache.append(i)
            time += 1
        else:
            if len(cache) > 0 and len(cache) == cacheSize:
                cache.popleft()
            cache.append(i)
            time += 5
    return time

