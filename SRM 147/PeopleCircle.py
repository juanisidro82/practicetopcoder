# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class PeopleCircle:
    def order(self, numMales, numFemales, K):
        n = numMales + numFemales
        circulo = ["M"] * n
        pos = -1
        """" This work cost algorithm to understand. I consult the editorial.
        The logic, is the next,  a list is created of size numFemales + numMales
        with values M, which M indicates that is man.
        Next, each K is movement , replace M for F, which F indicates that is
        female. If a movement it occupes a position of letter F, does not count
        a movement, because, the logic, the position  be removed before.
        This , in the order in which the letter M is changed by a letter F ,
        will be in the order they were eliminated in the game.
        """
        for i in range(numFemales):
            j = 0
            while j < K:
                pos = (pos + 1) % n
                if circulo[pos] == "M":
                    j += 1
            circulo[pos] = "F"
        return "".join(circulo)

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

def do_test(numMales, numFemales, K, __expected):
    startTime = time.time()
    instance = PeopleCircle()
    exception = None
    try:
        __result = instance.order(numMales, numFemales, K);
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
    sys.stdout.write("PeopleCircle (600 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("PeopleCircle.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            numMales = int(f.readline().rstrip())
            numFemales = int(f.readline().rstrip())
            K = int(f.readline().rstrip())
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(numMales, numFemales, K, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1444403600
    PT, TT = (T / 60.0, 75.0)
    points = 600 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
