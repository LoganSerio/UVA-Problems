import java.util.Scanner;
import java.math.BigInteger;
class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			int n = in.nextInt();
			BigInteger a = new BigInteger(in.next());
			BigInteger sum = BigInteger.ZERO;
			for (int i = 1;i<=n;i++) {
				BigInteger temp = new BigInteger(Integer.toString(i));
				sum = sum.add((a.pow(i)).multiply(temp));
			}
			System.out.println(sum);
		}	
	}
}
