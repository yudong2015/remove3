# coding=utf-8
#!/usr/bin/env python
import sys


def getLastOne(n):
    starts = getStartFroms(n)
    print "starts: {}".format(starts)
    positionN1 = 1
    """
    positionN = (3positionN1 + startN - 1 - a) / 2
    
    a = 1 or 2
    the type of positionN is int
    """
    for startN in starts[::-1]:
        result, remainder = divmod(positionN1*3+startN-1, 2)
        """
        a = 1 if remainder else 2
        positionN = divmod(positionN1*3+startN-1-a, 2)
        """
        positionN = result if remainder else result - 1
        positionN1 = positionN
    print "The last one quite is: {}".format(positionN1)


def getStartFroms(n):
    starts = []
    end = 0
    while n > 1:
        starts.append(end+1)
        removedNum, end = divmod(n+end, 3)
        n = n - removedNum
    return starts


if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        sys.exit('Need param N!')
    getLastOne(n)