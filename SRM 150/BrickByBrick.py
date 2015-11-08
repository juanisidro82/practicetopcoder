# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

def calculateposition(ndir, posicionactual):
    if ndir == 0:
        m = posicionactual[0] / 2
        n = posicionactual[1] / 2
    if ndir == 1:
        m = (posicionactual[0] - 1) / 2
        n = posicionactual[1] / 2
    if ndir == 2:
        m = (posicionactual[0] - 1) / 2
        n = (posicionactual[1] - 1) / 2
    if ndir == 3:
        m = posicionactual[0] / 2
        n = (posicionactual[1] - 1) / 2
    return (m, n)

def getmapa(map):
    mapa = []
    for i in range(len(map)):
        mapa += [],
        for j in range(len(map[i])):
            mapa[i] += map[i][j]
    return mapa

def getnB(map, mapa):
    nB = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if mapa[i][j] == "B":
                nB += 1
    return nB


class BrickByBrick:
    def timeToClear(self, map):
        direcciones = [[1, 1], [-1, 1,], [-1, -1], [1, -1]]
        mapa = getmapa(map)
        nB = getnB(map, mapa)
        ndir = 0
        posicioninicial = [1, 0]
        direccion = direcciones[ndir]
        mmap = len(map[0])
        nmap = len(map)
        time = 0
        ultimorompimiento = [-1, -1]
        while True:
            time = time + 1
            posicionactual = [posicioninicial[0] + direccion[0], posicioninicial[1] + direccion[1]]
            posicioninicial = posicionactual
            if ultimorompimiento == [posicioninicial, ndir]:
                return -1
            if ultimorompimiento == [-1, -1]:
                ultimorompimiento = [posicioninicial, ndir]
            m, n = calculateposition(ndir, posicionactual)
            cuadro = "#"
            if m < mmap and m >= 0 and n < nmap and n >= 0:
                cuadro = mapa[n][m]
            if cuadro != ".":
                if ndir % 2 == posicionactual[0] % 2:
                    ndir += 1
                else:
                    ndir -= 1
                if ndir == 4:
                    ndir = 0
                if ndir == -1:
                    ndir = 3
                direccion = direcciones[ndir]
            if cuadro == "B":
                mapa[n][m] = "."
                ultimorompimiento = [posicioninicial, ndir]
                nB -= 1
                if nB == 0:
                    break
        return time

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

def do_test(map, __expected):
    startTime = time.time()
    instance = BrickByBrick()
    exception = None
    try:
        __result = instance.timeToClear(map);
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
    sys.stdout.write("BrickByBrick (1100 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BrickByBrick.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            map = []
            for i in range(0, int(f.readline())):
                map.append(f.readline().rstrip())
            map = tuple(map)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(map, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1444587043
    PT, TT = (T / 60.0, 75.0)
    points = 1100 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
