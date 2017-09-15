import os
import sys
import random
import csv

def main(nr,nc,csvfname):
    f = open(csvfname,"w")
    for i in xrange(int(nr)):
        for j in xrange(int(nc)):
            d = random.uniform(-200.0, 200.0)
            f.write(str(d))
            if j < int(nc)-1:
                f.write(", ")
        f.write("\n")
    f.close()
    print "done."

if __name__ == '__main__':
    print "creating csv file ", sys.argv[3], "with ", sys.argv[1], "rows and ", sys.argv[2], "columns of random data."
    main(sys.argv[1],sys.argv[2],sys.argv[3])
