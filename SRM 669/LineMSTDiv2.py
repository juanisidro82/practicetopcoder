# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class LineMSTDiv2:
    def count(self, N):
        # Is amazing easy the algoritm when understand. Is essential visualize
        # the structure of data, in this case, you should imagine than the SMN
        # is a line path that cross all points, without returning to one, after
        # having gone through.
        #Assume that N = 4 . Then there exists an MTF that follows the path ABCD,
        # with distance 2, 2 , 2, where A, B , C , D are the vertices. There is
        # also an MTF which follows the route ABDC with 2-2-2 away . These two
        # SMN share the same structure , the only thing that varies is the
        # order of the points. If you look , all combinations with 1-1-1 equals
        # the number of combination between two points is calculated as the
        # permutation of 4 points, must be reduced by half because the lines
        # connecting the vertices are unidirectional.
        numerodecombinaciones = math.factorial(N) / 2
        SMNs = list(itertools.product(reversed(range(1, 3)), repeat = (N - 1)))
        waystotal = 0
        for SMN in SMNs:
            waysSMN = 1
            for i in range(N):
                for j in range(i +2, N):
                    ways = 2
                    for k in range(i, j):
                        if SMN[k] == 2:
                            ways = 1
                    waysSMN *=  ways
                    waysSMN %=  1000000007
            waystotal += waysSMN
            waystotal %= 1000000007
        waystotal *= math.factorial(N) / 2
        waystotal %= 1000000007
        return waystotal

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(N, __expected):
    startTime = time.time()
    instance = LineMSTDiv2()
    exception = None
    try:
        __result = instance.count(N);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("LineMSTDiv2 (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("LineMSTDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            N = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(N, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1445574818
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
