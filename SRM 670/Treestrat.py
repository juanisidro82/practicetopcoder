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


def calcularmovimientos(tree, A, B, turno):
    print resultados
    stringA = []
    stringB = []
    for a in A:
        stringA.append(str(a))
    for b in B:
        stringB.append(str(b))
    stringA = ",".join(stringA)
    stringB = ','.join(stringB)
    if not stringA in resultados[turno]:
        resultados[turno][stringA] = {}
    if stringB in resultados[turno][stringA]:
        return resultados[turno][stringA][stringB]


    if turno == 'A':
        points = obtenerpoints(A, tree)
    elif turno == 'B':
        points = obtenerpoints(B, tree)
    if turno == 'A':
        for i in range(len(points)):
            newpoints = points[i]
            newpoints.append(A[i])
            for b in B:
                if b in newpoints:
                    newpoints.remove(b)
            bestValueA = 0
            for newpoint in newpoints:
                oldvalue = A[i]
                A[i] = newpoint
                newA = sorted(A)
                movimientos = calcularmovimientos(tree, newA, B, 'B')
                A[i] = oldvalue
                if bestValueA < movimientos:
                    bestValueA = movimientos
        resultados[turno][stringA][stringB] = bestValueA
        print "A, B, turno"
        print A
        print B
        print turno
        print "movimientos"
        print bestValueA
        return bestValueA
    elif turno == 'B':
        for i in range(len(points)):
            newpoints = points[i]
            bestValueB = 10000000000000000000000000
            for a in A:
                if a in newpoints:
                    bestValueB = 1
                    break
            if bestValueB == 1:
                newpoints = []
            for newpoint in newpoints:
                oldvalue = B[i]
                B[i] = newpoint
                newB = sorted(B)
                movimientos = calcularmovimientos(tree, A, newB, 'A') + 1
                B[i] = oldvalue
                if bestValueB > movimientos:
                    bestValueB = movimientos
        resultados[turno][stringA][stringB] = bestValueB
        print "A, B, turno"
        print A
        print B
        print turno
        print "movimientos"
        print bestValueB
        return bestValueB


class Treestrat:
    def roundcnt(self, tree, A, B):
        newA = []
        newB = []
        for a in A:
            newA.append(a)
        for b in B:
            newB.append(b)
        global resultados
        resultados = {'A': {}, 'B': {}}
        newA = sorted(newA)
        newB = sorted(newB)
        movimientos = calcularmovimientos(tree, newA, newB, 'A')
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
