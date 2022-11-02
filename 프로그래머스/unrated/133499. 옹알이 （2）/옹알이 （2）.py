# def solution(babbling):
#     can_speak = ["aya", "ye", "woo", "ma"]
#     for i in range(len(babbling)):
#         for j in range(len(can_speak)):
#             if can_speak[j] + can_speak[j] in babbling[i]:
#                 continue
                
#             if can_speak[j] in babbling[i][:2]:
#                 babbling[i] = babbling[i][2:]
                
#             if can_speak[j] in babbling[i][-2:]:
#                 babbling[i] = babbling[i][0:-2]
                
#             if can_speak[j] in babbling[i][:3]:
#                 babbling[i] = babbling[i][3:]
            
#             if can_speak[j] in babbling[i][-3:]:
#                 babbling[i] = babbling[i][0:-3]
#     print(babbling)
#     return babbling.count("")

def solution(babbling):
    result = 0
    
    for word in babbling:
        stack = ''
        prev = ''
        
        for char in word:
            stack += char
            
            if prev != stack and stack in ["aya", "ye", "woo", "ma"]:
                prev = stack
                stack = ''
        if stack == '':
            result += 1
    return result
