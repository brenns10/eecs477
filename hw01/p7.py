#!/usr/bin/env python3
"""4096 attempts to solve HW01 problem 7."""

from itertools import product
from subprocess import Popen, PIPE
from concurrent.futures import ThreadPoolExecutor


octave = """
c = [%d; %d; %d; %d; %d; %d; 1; 1; 1];
A = [1, 1, 1, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 1, 1, 1, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 1, 1, 1;
     1, 0, 0, 1, 0, 0, 1, 0, 0;
     0, 1, 0, 0, 1, 0, 0, 1, 0;
     0, 0, 1, 0, 0, 1, 0, 0, 1;
     1, 0, 0, 1, 0, 0, 0, 0, 0;
     0, 1, 0, 0, 1, 0, 0, 0, 0;
     0, 0, 1, 0, 0, 1, 0, 0, 0];
b = [2; 1; 3; 2; 2; 2; 1; 1; 1];
lb = [];
ub = [];
ctype = "UUUSSSLLL";
vartype = "CCCCCCCCC";
sense = 1;
[x, f, status, extra] = glpk(c, A, b, lb, ub, ctype, vartype, sense)
"""


def do_tup(tup):
    print(tup)
    script = octave % tup
    proc = Popen('octave-cli', stdin=PIPE, stdout=PIPE)
    proc.stdin.write(script.encode('utf8'))
    proc.stdin.close()
    output = proc.stdout.readlines()
    try:
        [int(x.strip()) for x in output[2:11]]  # raise if not int!
    except:
        print("%r works!")


def main():
    pool = ThreadPoolExecutor(8)
    futures = [pool.submit(do_tup, tup) for tup in product(*([[1,2,3,4]]*6))]
    for future in futures:
        future.result()


if __name__ == '__main__':
    main()
