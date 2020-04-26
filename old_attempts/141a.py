def amusing_joke(host, resident, random):
    if host is None or resident is None or random is None:
        return "NO"
    
    sh, sre, sr = list(host), list(resident), sorted(random)
    shsre = sh + sre
    shsre = sorted(shsre)
    
    if (len(shsre)) != len(sr):
        return "NO"
    
    if shsre == sr:
        return "YES"
    else:    
        return "NO"

if __name__ == '__main__':
    host = str(input())
    resident = str(input())
    random = str(input())
    print(amusing_joke(host, resident, random))