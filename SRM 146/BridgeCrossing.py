# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

def caminanrapidos(lado1, lado2, tiempo):
    lado1 = sorted(lado1)
    tiempo1 = tiempo + lado1[1]
    lado2.append(lado1[0])
    lado2.append(lado1[1])
    del lado1[0]
    del lado1[0]
    return (lado1, lado2, tiempo1)

def caminanlentos(lado1, lado2, tiempo1):
    lado1 = sorted(lado1)
    tiempo1 = tiempo1 + lado1[-1]
    lado2.append(lado1[-1])
    lado2.append(lado1[-2])
    del lado1[-2]
    del lado1[-1]
    return (lado1, lado2, tiempo1)


def caminanextremos(lado3, lado4, tiempo):
    lado3 = sorted(lado3)
    tiempo2 = tiempo + lado3[-1]
    lado4.append(lado3[0])
    lado4.append(lado3[-1])
    del lado3[0]
    del lado3[-1]
    return (lado3, lado4, tiempo2)

def regreso(lado1, lado2, tiempo1):
    lado2 = sorted(lado2)
    tiempo1 = tiempo1 + lado2[0]
    lado1.append(lado2[0])
    del lado2[0]
    return (lado1, lado2, tiempo1)


def viaje(lado1, lado2, tiempo):
    """ The solution to this problem is more easy, simply compute all this
    situation using recursion. Two cicle for consider all posibilities of go to
    other side of the bridging. During the writing code, i omitted read the
    contraints, because of that. do not consider this solution."""
    lado3 = []
    lado4 = []
    for i in lado1:
        lado3.append(i)
    for i in lado2:
        lado4.append(i)
    if len(lado1) < 3:
        lado1 = sorted(lado1)
        return tiempo + lado1[len(lado1) - 1]
    if len(lado1) == 3:
        lado1 = sorted(lado1)
        return tiempo + lado1[1] + lado1[0] + lado1[2]
    if len(lado1) > 3:
        # My answer
        lado1, lado2, tiempo1 = caminanrapidos(lado1, lado2, tiempo)
        lado1, lado2, tiempo1 = regreso(lado1, lado2, tiempo1)
        lado1, lado2, tiempo1 = caminanlentos(lado1, lado2, tiempo1)
        lado1, lado2, tiempo1 = regreso(lado1, lado2, tiempo1)
        tiempo1 = viaje(lado1, lado2, tiempo1)
        # What I never thought, i check the editorial.
        lado3, lado4, tiempo2 = caminanextremos(lado3, lado4, tiempo)
        lado3, lado4, tiempo2 = regreso(lado3, lado4, tiempo2)
        tiempo2 = viaje(lado3, lado4, tiempo2)
        tiempo = tiempo1
        if tiempo > tiempo2:
           tiempo = tiempo2

    return tiempo


class BridgeCrossing:
    def minTime(self, times):
        lado1 = []
        lado2 = []
        tiempo = 0

        for time in times:
            lado1.append(time)
        
        tiempo = viaje(lado1, lado2, tiempo)

        return tiempo

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

def do_test(times, __expected):
    startTime = time.time()
    instance = BridgeCrossing()
    exception = None
    try:
        __result = instance.minTime(times);
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
    sys.stdout.write("BridgeCrossing (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BridgeCrossing.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            times = []
            for i in range(0, int(f.readline())):
                times.append(int(f.readline().rstrip()))
            times = tuple(times)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(times, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1442930910
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
