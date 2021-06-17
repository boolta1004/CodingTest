def solution(absolutes, signs):
    answer = 0
    for k in range(len(signs)):
        if signs[k] == False:
            temp = -1*absolutes[k]
        else:
            temp = absolutes[k]
        answer+=temp
    return answer