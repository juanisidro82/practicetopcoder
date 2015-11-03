# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect


def obtenerpoints(C, tree):
    points = []
    for i in range(len(C)):
        points.append([])
        # Primero se determina las jugadas hacia abajo
        if C[i] != 0:
            points[i].append(tree[C[i]-1])
        # Luego las jugadas hacia arriba
        for j in range(len(tree)):
            if tree[j] == C[i]:
                points[i].append(j + 1)
    return points

def vectortoString(A):
    stringA = []
    for a in A:
        stringA.append(str(a))
    stringA = ",".join(stringA)
    return stringA

def calcularmovimientos(tree, CP, NP, turno):
    stringCP = vectortoString(CP)
    stringNP = vectortoString(NP)
    if turno == 'A':
        nuevoturno = 'B'
        resultados[turno][stringCP][stringNP] = -1
    if turno == 'B':
        nuevoturno = 'A'
        resultados[turno][stringCP][stringNP] = 10
    if not stringNP in resultados[nuevoturno]:
        resultados[nuevoturno][stringNP] = {}

    points = obtenerpoints(CP, tree)
    for i in range(len(points)):
        newpoints = points[i]
        if turno == 'A':
            adiccion = 0
            newpoints.append(CP[i])
            for np in NP:
                if np in newpoints:
                    newpoints.remove(np)
        if turno == 'B':
            adiccion = 1
            for np in NP:
                if np in newpoints:
                    resultados[turno][stringCP][stringNP] = 1
                    break
            if resultados[turno][stringCP][stringNP] == 1:
                newpoints = []

        for newpoint in newpoints:
            oldvalue = CP[i]
            CP[i] = newpoint
            newCP = sorted(CP)
            CP[i] = oldvalue
            newstringCP = vectortoString(newCP)
            if newstringCP in resultados[nuevoturno][stringNP]:
                movimientos = resultados[nuevoturno][stringNP][newstringCP]
            else:
                movimientos = calcularmovimientos(tree, NP, newCP, nuevoturno) + adiccion
            if (resultados[turno][stringCP][stringNP] < movimientos) and turno == 'A':
                resultados[turno][stringCP][stringNP] = movimientos
            if (resultados[turno][stringCP][stringNP] > movimientos) and turno == 'B':
                resultados[turno][stringCP][stringNP] = movimientos

    return resultados[turno][stringCP][stringNP]



class Treestrat:
    def roundcnt(self, tree, A, B):
        newA = []
        newB = []
        for a in A:
            newA.append(a)
        for b in B:
            newB.append(b)
        global resultados, analisis
        resultados = {'A': {}, 'B': {}}
        newA = sorted(newA)
        newB = sorted(newB)
        stringA = vectortoString(newA)
        stringB = vectortoString(newB)
        if not stringA in resultados['A']:
            resultados['A'][stringA] = {}
        movimientos = calcularmovimientos(tree, newA, newB, 'A')
        print resultados
        print stringA
        print stringB
        return movimientos

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

def do_test(tree, A, B, __expected):
    startTime = time.time()
    instance = Treestrat()
    exception = None
    try:
        __result = instance.roundcnt(tree, A, B);
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
    sys.stdout.write("Treestrat (1050 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Treestrat.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            tree = []
            for i in range(0, int(f.readline())):
                tree.append(int(f.readline().rstrip()))
            tree = tuple(tree)
            A = []
            for i in range(0, int(f.readline())):
                A.append(int(f.readline().rstrip()))
            A = tuple(A)
            B = []
            for i in range(0, int(f.readline())):
                B.append(int(f.readline().rstrip()))
            B = tuple(B)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(tree, A, B, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1446208785
    PT, TT = (T / 60.0, 75.0)
    points = 1050 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
