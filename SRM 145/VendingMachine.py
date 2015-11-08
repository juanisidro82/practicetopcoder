# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class VendingMachine:
    columnaactual = 0
    contador = 0
    cols = 0

    def rotate(self, newcolumn):
        distancia = math.fabs(newcolumn - self.columnaactual)
        if distancia > (self.cols - distancia):
            distancia = self.cols - distancia
        self.contador +=  distancia
        self.columnaactual = newcolumn

    def findMaxcol(self):
        self.columnamaxima = 0
        preciocolumnamaximo = 0
    # Find the column with highest price
        for j in range(self.cols):
            preciocolumna = 0
            for k in range(self.rows):
                preciocolumna += self.maquina[k][j]
            if preciocolumnamaximo < preciocolumna:
                preciocolumnamaximo = preciocolumna
                self.columnamaxima = j

    def motorUse(self, prices, purchases):
        n = len(purchases)
# Create lists variables shelfs, columns, times.
        shelfs = []
        columns = []
        times = []
        for p in purchases:
            coordenadas = p.split(":")[0]
            times += int(p.split(":")[1]),
            shelfs += int(coordenadas.split(",")[0]),
            columns += int(coordenadas.split(",")[1]),
# Create the representation of the machine
        self.maquina = []
        self.rows = len(prices)
        for i in range(self.rows):
            preciosc = prices[i].split(" ")
            self.cols = len(preciosc)
            self.maquina += [],
            for j in range(self.cols):
                self.maquina[i] += int(preciosc[j]),
# Start the purshases. 
        self.cols= len(self.maquina[0])
        ultimouso = -5
        for i in range(n):
            self.findMaxcol()
    # We are in the time of purchase
            tiempoactual = times[i]
    # In this case in that purchase is invalid, return - 1.
            if self.maquina[shelfs[i]][columns[i]] == 0:
                return -1
    #  Verify that the ultime use was more 5 minutes. In this case, the machine
    # rotate to more expensive column.
    #The distance is calculated as the absolute value of the difference of the position initial
    #to the new position.
            if math.fabs(tiempoactual - ultimouso) >= 5:
                self.rotate(self.columnamaxima)
    # The purchases involves changes in the value of the ultime use and the
    # retired of the buyed articled.
            ultimouso = tiempoactual
            self.maquina[shelfs[i]][columns[i]] = 0
            self.rotate(columns[i])
# At the last, the machine rote to most expensive column.
        self.findMaxcol()
        self.rotate(self.columnamaxima)
        return self.contador

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
