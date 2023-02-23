# 자물쇠와 열쇠

def unlocking(ul, key, i, j):
    for ki in range(kn):
        for kj in range(kn):
            ul[i+ki][j+kj] += key[ki][kj]

    if chk_unlock(ul):
        result = True
    else:
        result = False
        
    for ki in range(kn):
        for kj in range(kn):
            ul[i+ki][j+kj] -= key[ki][kj]
            
    return result

def chk_unlock(ul):
    for i in range(ln, ln*2):
        for j in range(ln, ln*2):
            if ul[i][j] != 1:
                return False
    return True

def solution(key, lock):
    global kn, ln
    answer = False
    kn, ln = len(key), len(lock)
    unlock = [[0]*(ln*3) for _ in range(ln*3)]
    for i in range(ln):
        for j in range(ln):
            unlock[i+ln][j+ln] = lock[i][j]
    
    keys = []
    for _ in range(4):
        key = list(zip(*key[::-1]))
        keys.append(key)
    
    for i in range(ln*2):
        for j in range(ln*2):
            for key in keys:
                if unlocking(unlock, key, i, j):
                    return True

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))