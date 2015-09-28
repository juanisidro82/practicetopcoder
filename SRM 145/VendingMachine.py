# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class VendingMachine:
    def motorUse(self, prices, purchases):
        n = len(purchases)
        tt = 0
        shelfs = []
        columns = []
        times = []
        for p in purchases:
            coordenadas = p.split(":")[0]
            times.append(int(p.split(":")[1]))
            shelfs.append(int(coordenadas.split(",")[0]))
            columns.append(int(coordenadas.split(",")[1]))
        maquina = []
        rows = len(prices)
        for i in range(rows):
            preciosc = prices[i].split(" ")
            cols = len(preciosc)
            maquina.append([])
            for j in range(cols):
                maquina[i].append(int(preciosc[j]))
        contador = 0
        cols= len(maquina[0])
        columnaactual = 0
        ultimouso = -5
        print "columnaactual=" + str(columnaactual)
        for i in range(n):
            columnamaxima = 0
            preciocolumnamaximo = 0
            for j in range(cols):
                preciocolumna = 0
                for k in range(rows):
                    preciocolumna = preciocolumna + maquina[k][j]
                if preciocolumnamaximo < preciocolumna:
                   preciocolumnamaximo = preciocolumna
                   columnamaxima = j
            print "columnamxima=" + str(columnamaxima)
            tiempoactual = times[i]
            if maquina[shelfs[i]][columns[i]] == 0:
                return -1
            if math.fabs(tiempoactual - ultimouso) >= 5:
               distancia = math.fabs(columnamaxima - columnaactual)
               if distancia > (cols - distancia):
                  distancia = cols - distancia
               contador = contador + distancia
               print "contador=" + str(contador)
               columnaactual = columnamaxima
            print "columnaactual=" + str(columnaactual)
            ultimouso = tiempoactual
            maquina[shelfs[i]][columns[i]] = 0
            distancia = math.fabs(columns[i] - columnaactual)
            if distancia > (cols - distancia):
               distancia = cols - distancia
            columnaactual = columns[i]
            contador =  contador + distancia
            print "contador=" + str(contador)
            print "columnaactual=" + str(columnaactual)
            print maquina
            print columns
        columnamaxima = 0
        preciocolumnamaximo = 0
        for j in range(cols):
            preciocolumna = 0
            for k in range(rows):
                preciocolumna = preciocolumna + maquina[k][j]
            if preciocolumnamaximo < preciocolumna:
                preciocolumnamaximo = preciocolumna
                columnamaxima = j
        print "columnamaxima=" + str(columnamaxima)
        distancia = math.fabs(columnamaxima - columnaactual)
        if distancia > (cols - distancia):
            distancia = cols - distancia
        contador = contador + distancia
        return contador

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

def do_test(prices, purchases, __expected):
    startTime = time.time()
    instance = VendingMachine()
    exception = None
    try:
        __result = instance.motorUse(prices, purchases);
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
    sys.stdout.write("VendingMachine (1100 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("VendingMachine.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            prices = []
            for i in range(0, int(f.readline())):
                prices.append(f.readline().rstrip())
            prices = tuple(prices)
            purchases = []
            for i in range(0, int(f.readline())):
                purchases.append(f.readline().rstrip())
            purchases = tuple(purchases)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(prices, purchases, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1442928488
    PT, TT = (T / 60.0, 75.0)
    points = 1100 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end