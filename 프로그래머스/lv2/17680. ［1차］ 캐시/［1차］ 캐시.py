from collections import deque 

def solution(cacheSize, cities):
    answer = 0
    cache_buffer = deque()
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache_buffer:
            answer += 1
            cache_buffer.remove(city)
        else:
            answer += 5
        if len(cache_buffer) >= cacheSize:
            cache_buffer.popleft()
        cache_buffer.append(city)
    return answer