# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class BearDartsDiv2:
    def count(self, w):
        N = len(w)
        producto2sum = collections.OrderedDict()
        for i in range(1, N - 2):
            for j in range(0, i):
                producto = w[i] * w[j]
                if not producto in producto2sum:
                    producto2sum[producto] = collections.OrderedDict()
                    producto2sum[producto][i] = 0
                if not i in producto2sum[producto]:
                    ultimoelemento = producto2sum[producto].keys()[-1]
                    producto2sum[producto][i] = producto2sum[producto][ultimoelemento]
                producto2sum[producto][i] += 1
        resultado = 0
        for i in range(3, N):
            for j in range(2, i):
                if w[i] % w[j] != 0:
                    continue
                cociente = w[i] / w[j]
                if not cociente in producto2sum:
                    continue
                k = j -1
                while not k in producto2sum[cociente]:
                    k -= 1
                    if k == 0:
                        break
                if k == 0:
                    continue
                resultado += producto2sum[cociente][k]
        return resultado




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

def do_test(w, __expected):
    startTime = time.time()
    instance = BearDartsDiv2()
    exception = None
    try:
        __result = instance.count(w);
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
    sys.stdout.write("BearDartsDiv2 (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BearDartsDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            w = []
            for i in range(0, int(f.readline())):
                w.append(int(f.readline().rstrip()))
            w = tuple(w)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(w, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1444967094
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
