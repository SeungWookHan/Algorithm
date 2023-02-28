def solution(elements):
    result = set()
    len_elements = len(elements)
    elements = elements * 2
    
    for i in range(len_elements):
        for j in range(len_elements):
            sum_element = sum(elements[i:i+j+1])
            result.add(sum_element)
    return len(result)