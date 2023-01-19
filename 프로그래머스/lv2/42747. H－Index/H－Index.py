def solution(citations):
    citations.sort()
    len_citations = len(citations)
    for idx , citation in enumerate(citations):
        h_index_condition = len_citations - idx
        if citation >= h_index_condition:
            return h_index_condition
    return 0