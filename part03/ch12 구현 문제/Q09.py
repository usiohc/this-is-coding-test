# 문자열 압축 - 프로그래머스 (https://school.programmers.co.kr/learn/courses/30/lessons/60057)

def solution1(s):
    answer = len(s)
    
    if answer == 1:
        return answer 
    
    for l in range(1, len(s)+1):
        lst = [s[i:i+l] for i in range(0, len(s), l)]
        dic = {sl:[1] for sl in set(lst)}
        leng = len(s)
        
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                leng -= l
                dic[lst[i]][-1] += 1
            else:
                if dic[lst[i]][-1] > 1:
                    dic[lst[i]].append(1)
                    
        for v_lst in dic.values():
            for v in v_lst:
                if v > 1:
                    leng += len(str(v))
        answer = min(answer, leng)
        
    return answer

def solution2(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        ss = s[:i]
        cnt = 1
        zip_str = ''
        for j in range(i, len(s)+i, i):
            if ss == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    zip_str += str(cnt)+ss
                else:
                    zip_str += ss
                    
                ss = s[j:j+i]
                cnt = 1

        answer = min(answer, len(zip_str))
            
    return answer