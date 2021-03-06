# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
""" As the idea is to go is to check all joints, the following occurs not all 
nodes are interconnected, and sometimes you have to go back, three situations
can happen, the first all nodes are connected in series, if a route Driving
first past one by one one at a time is enough to check them all. The other case
is that neither a node ARE connected to each other, with the exception that all
are connected to only root node, in this case will be necessary to always
return to the root node, in this case, the node is allowed to this farther from
the root node, to avoid having to return.
The other is the intermediate case, that at least one node is not connected to
the root, and also at least two nodes are not connected. I mean node, as a
node is not the root node Third case, this situation presents junctions
interconnected, and not interconnected. To save effort of the engineer,
we proceed to calculate the distance the each junction to root, and choice the
junction with the major distance to visit at the end."""
class PowerOutage:
    def estimateTimeOut(self, fromJunction, toJunction, ductLength):
        n = len(fromJunction)
        sumadistancia1 = 0
        for i in range(n):
            sumadistancia1 += ductLength[i]
        nodos = []
        for i in range(n):
            if not toJunction[i] in nodos:
               nodos += toJunction[i],
            if not fromJunction[i] in nodos:
               nodos += fromJunction[i],
        m = len(nodos)
        nodos = sorted(nodos)
        distanciahastanodo = {}
        distanciamaslarga = 0
        for j in range(m):
            distanciahastanodo[nodos[j]] = 0
        for nodo in nodos:
            for j in range(n):
                if nodo == toJunction[j]:
                    distanciahastanodo[nodo] = distanciahastanodo[fromJunction[j]] + ductLength[j]
                    break
            distanciamaslarga = max(distanciamaslarga, distanciahastanodo[nodo])
        return sumadistancia1 * 2 - distanciamaslarga


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
