import java.util.*;
import java.math.BigInteger;
class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		for (int i = 0; i < n; i++) {
			StringBuilder rev1 = new StringBuilder();
			StringBuilder rev2 = new StringBuilder();
			rev1.append(in.next());
			rev2.append(in.next());
			BigInteger first = new BigInteger(rev1.reverse().toString());
			BigInteger second = new BigInteger(rev2.reverse().toString());
			BigInteger sum = first.add(second);
			StringBuilder sumRev = new StringBuilder();
			sumRev.append(sum.toString());
			sumRev = sumRev.reverse();
			BigInteger result = new BigInteger(sumRev.toString());
			System.out.println(result);
		}
	}
}
