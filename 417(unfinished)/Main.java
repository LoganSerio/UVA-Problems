import java.util.Scanner;
class Main {
	public static void main(String[] args) { 
		Scanner in = new Scanner(System.in);
		while (in.hasNextLine()) {
			String word = in.nextLine();
			int sum = 0;
			boolean isWord = true;
			for (int i = 0; i < word.length(); i++) {
				if (sum > (i+1)*((int) word.charAt(i)-96))
					isWord = false;
				else {
					sum += (int) word.charAt(i)-96;
				}
			}
			if (isWord == true)
				System.out.println(sum);
			else
				System.out.println(0);
		}
	}
}
