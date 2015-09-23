import java.io.*;
import java.util.*;

public class PowerOutage {
	public int estimateTimeOut(int[] fromJunction, int[] toJunction, int[] ductLength) {
		return 0;
	}

// CUT begin
	public static void main(String[] args){
		System.err.println("PowerOutage (1100 Points)");
		System.err.println();
		HashSet<Integer> cases = new HashSet<Integer>();
        for (int i = 0; i < args.length; ++i) cases.add(Integer.parseInt(args[i]));
        runTest(cases);
	}

	static void runTest(HashSet<Integer> caseSet) {
	    int cases = 0, passed = 0;
	    while (true) {
	    	String label = Reader.nextLine();
	    	if (label == null || !label.startsWith("--"))
	    		break;

            int[] fromJunction = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < fromJunction.length; ++i)
                fromJunction[i] = Integer.parseInt(Reader.nextLine());
            int[] toJunction = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < toJunction.length; ++i)
                toJunction[i] = Integer.parseInt(Reader.nextLine());
            int[] ductLength = new int[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < ductLength.length; ++i)
                ductLength[i] = Integer.parseInt(Reader.nextLine());
            Reader.nextLine();
            int __answer = Integer.parseInt(Reader.nextLine());

            cases++;
            if (caseSet.size() > 0 && !caseSet.contains(cases - 1))
                continue;
    		System.err.print(String.format("  Testcase #%d ... ", cases - 1));

            if (doTest(fromJunction, toJunction, ductLength, __answer))
                passed++;
	    }
	    if (caseSet.size() > 0) cases = caseSet.size();
        System.err.println(String.format("%nPassed : %d/%d cases", passed, cases));

        int T = (int)(System.currentTimeMillis() / 1000) - 1442956621;
        double PT = T / 60.0, TT = 75.0;
        System.err.println(String.format("Time   : %d minutes %d secs%nScore  : %.2f points", T / 60, T % 60, 1100 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))));
	}

	static boolean doTest(int[] fromJunction, int[] toJunction, int[] ductLength, int __expected) {
		long startTime = System.currentTimeMillis();
		Throwable exception = null;
		PowerOutage instance = new PowerOutage();
		int __result = 0;
		try {
			__result = instance.estimateTimeOut(fromJunction, toJunction, ductLength);
		}
		catch (Throwable e) { exception = e; }
		double elapsed = (System.currentTimeMillis() - startTime) / 1000.0;

		if (exception != null) {
			System.err.println("RUNTIME ERROR!");
			exception.printStackTrace();
			return false;
		}
		else if (__result == __expected) {
			System.err.println("PASSED! " + String.format("(%.2f seconds)", elapsed));
			return true;
		}
		else {
			System.err.println("FAILED! " + String.format("(%.2f seconds)", elapsed));
			System.err.println("           Expected: " + __expected);
			System.err.println("           Received: " + __result);
			return false;
		}
	}

	static class Reader {
        private static final String dataFileName = "PowerOutage.sample";
	    private static BufferedReader reader;

	    public static String nextLine() {
	        try {
                if (reader == null) {
                    reader = new BufferedReader(new InputStreamReader(new FileInputStream(dataFileName)));
                }
                return reader.readLine();
	        }
	        catch (IOException e) {
	            System.err.println("FATAL!! IOException");
	            e.printStackTrace();
	            System.exit(1);
	        }
	        return "";
	    }
	}
// CUT end
}
