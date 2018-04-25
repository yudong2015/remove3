# coding=utf-8
#!/usr/bin/env python
import sys


def run(n, mark, last, positionNum, loopDepth):
    removeCount = 0
    for i in range(n):
        if positionNum == 2:
            removeCount += 1
            positionNum = 0
        else:
            mark[i-removeCount] = mark[i]
            last = mark[i]
            positionNum += 1
    left = n-removeCount
    if left > 1:
        loopDepth += 1
        run(left, mark[:left], last, positionNum, loopDepth)
    else:
        print "last:{}, depth:{}".format(last, loopDepth)


def getLastDiv3(n):
    mark = range(1, n+1)
    last = 1
    positionNum = 0
    loopDepth = 1
    print 'N: {}'.format(n)
    run(n, mark, last, positionNum, loopDepth)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        total = int(sys.argv[1])
    else:
        sys.exit('Need param N!')
    getLastDiv3(total)
