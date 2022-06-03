import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		
		int num = s.nextInt();
		
		int ln, cn, rn, crn, newn;
		int cnt =0;
		newn = num;
		while(true) {
			
			ln = newn / 10;
			rn = newn % 10;
			
			cn = ln + rn;
			crn = cn % 10;
			
			newn = rn*10 + crn;
			
			cnt++;
			if(num == newn) {
				break;
			}
		}
		System.out.println(cnt);
	}
}

