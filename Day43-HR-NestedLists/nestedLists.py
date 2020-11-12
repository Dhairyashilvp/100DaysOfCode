if __name__ == '__main__':
    name = []
    score = []
    op_name = []
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
    
    for i in range(score.count(min(score))):
        name.remove(name[score.index(min(score))])
        score.remove(score[score.index(min(score))])

    for i in range(score.count(min(score))):
        op_name.append(name[score.index(min(score))])
        name.remove(name[score.index(min(score))])
        score.remove(score[score.index(min(score))])
    op_name.sort()
    for i in op_name:
        print(i)
