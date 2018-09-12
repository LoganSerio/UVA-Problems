import java.util.*;
class Main {
    static String row = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./";
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); 
        while (in.hasNextLine()) {
            String text = in.nextLine();
            for (char chr : text.toCharArray()) {
                int index = row.indexOf(chr);
                if (index != -1) {
                    System.out.print(row.charAt(index-1));
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}