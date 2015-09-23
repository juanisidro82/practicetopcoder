# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class PowerOutage:
    def estimateTimeOut(self, fromJunction, toJunction, ductLength):
        n = len(fromJunction)
        sumadistancia1 = 0
        for i in range(n):
            sumadistancia1 = sumadistancia1 + ductLength[i]
        nodos = []
        for i in range(n):
            if not toJunction[i] in nodos:
               nodos.append(toJunction[i])
            if not fromJunction[i] in nodos:
               nodos.append(fromJunction[i])
        m = len(nodos)
        nodos = sorted(nodos)
        w1 = {}
        m1 = 0
        for j in range(m):
            w1[nodos[j]] = 0
        for nodo in nodos:
            for j in range(n):
                if nodo == toJunction[j]:
                    w1[nodo] = w1[fromJunction[j]] + ductLength[j]
                    break
            print "nodo=" + str(nodo)
            print w1[nodo]
            print m1
            if w1[nodo] > m1:
               m1 = w1[nodo]
        print "sumadisntacia=" + str(sumadistancia1)
        return sumadistancia1 * 2 - m1


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

def do_test(fromJunction, toJunction, ductLength, __expected):
    startTime = time.time()
    instance = PowerOutage()
    exception = None
    try:
        __result = instance.estimateTimeOut(fromJunction, toJunction, ductLength);
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
    sys.stdout.write("PowerOutage (1100 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("PowerOutage.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            fromJunction = []
            for i in range(0, int(f.readline())):
                fromJunction.append(int(f.readline().rstrip()))
            fromJunction = tuple(fromJunction)
            toJunction = []
            for i in range(0, int(f.readline())):
                toJunction.append(int(f.readline().rstrip()))
            toJunction = tuple(toJunction)
            ductLength = []
            for i in range(0, int(f.readline())):
                ductLength.append(int(f.readline().rstrip()))
            ductLength = tuple(ductLength)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(fromJunction, toJunction, ductLength, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1442928201
    PT, TT = (T / 60.0, 75.0)
    points = 1100 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
