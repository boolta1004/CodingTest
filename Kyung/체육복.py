def solution(n, lost, reserve):
    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)
    for k in set_reserve:
            if k-1 in set_lost:
                set_lost.remove(k-1)
            elif k+1 in set_lost:
                set_lost.remove(k+1)
    answer = n-len(set_lost)
    return answer