# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
import fractions

def factorizar(K):
    divisores = []
    k = int(math.ceil(math.sqrt(K)))
    for i in range(1, k+ 1):
        if K%i == 0:
            divisores += i,
            if not K/i in divisores:
                divisores += K/i,
    return sorted(divisores)


class AnArray:
    def solveProblem(self, A, K):
        divisores = factorizar(K)
        matriz = dict()
        divisoresdict = {}
        for i in range(len(divisores)):
            divisoresdict[divisores[i]] = i
        matrizdp = dict()
        for i in range(len(A)+1):
            matrizdp[i] = dict()
            for j in range(len(divisores)):
                matrizdp[i][j] = dict()
                for l in range(4):
                    matrizdp[i][j][l] = 0
        matrizdp[0][0][0] = 1
        for i in range(1, len(A)+ 1):
            for j in range(len(divisores)):
                # Me costo trabaja entender esta parte, de 4, es el numero de
                # factores que quedan 3, 2, 1 y nada
                for l in range(4):
                    # Aca se pone el numero de caso en que no incluye el factor A[i]
                    # en este sera n - 1 caso, sobrara el mismo numero de monedas
                    # y sera el mismo numero que se dividira entre residuos
                    matrizdp[i][j][l] = matrizdp[i-1][j][l]
                    if l == 0:
                        # como ya no queda elementos que eliminar, se salta
                        continue
                    # Ahora se aborda, los casos en que A[n] esta involucrado,
                    # como es el mismo factor, se elimina A[n], obteniendo el GCD
                    # como entre diviores[j] y A[n]
                    g = fractions.gcd(A[i-1], divisores[j])
                    nuevoK = divisoresdict[divisores[j]/g]
                    matrizdp[i][j][l] += matrizdp[i-1][nuevoK][l-1]
        return matrizdp[len(A)][len(divisores) -1][3]

        # Encontrar divisores de K

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

def do_test(A, K, __expected):
    startTime = time.time()
    instance = AnArray()
    exception = None
    try:
        __result = instance.solveProblem(A, K);
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
    sys.stdout.write("AnArray (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("AnArray.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            A = []
            for i in range(0, int(f.readline())):
                A.append(int(f.readline().rstrip()))
            A = tuple(A)
            K = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(A, K, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1444934282
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
