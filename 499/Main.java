import java.util.*;
class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		while (in.hasNextLine()) {
			HashMap<Character,Integer> line=new HashMap<Character,Integer>();
			String s = in.nextLine().trim().replaceAll("[\\W+]","").replaceAll("\\d+","");
			for (int i = 0; i<s.length();i++) {
				char temp = s.charAt(i);
				if (line.containsKey(temp))
					line.put(temp, line.get(temp)+1);
				else 
					line.put(temp,1);
			}
			int maxVal = 0;
			Iterator<Character> keySetIterator = line.keySet().iterator();
			while (keySetIterator.hasNext()) {
				int cur = line.get(keySetIterator.next());
				if (cur > maxVal)
					maxVal = cur;
			}
			String str = "";
			Iterator<Character> keySetIterator2 = line.keySet().iterator();	
			while (keySetIterator2.hasNext()) {
				Character key = keySetIterator2.next();
				if (line.get(key).equals(maxVal))
					str += key;
			}
			char[] c  = str.toCharArray();
			Arrays.sort(c);
			for(int i = 0; i<c.length;i++) {
				System.out.print(c[i]);
			}
			System.out.println(" "+maxVal);			
		}
	}
}
