import java.util.Scanner;
import java.io.PrintWriter;
class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		while (in.hasNext()) {
			out.println(in.nextLine());
		}
		out.close();
		in.close();
	}
}
