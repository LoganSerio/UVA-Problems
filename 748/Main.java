import java.util.*;
import java.io.*;
import java.math.BigDecimal;
class Main {
	public static void main(String[] args) throws IOException {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			BigDecimal r = in.nextBigDecimal();
			int n = in.nextInt();
			r = r.pow(n);
			String s = r.stripTrailingZeros().toPlainString();
			if (s.charAt(0)== '0')
				s = s.substring(1);
			System.out.println(s);
		}
	}
}
