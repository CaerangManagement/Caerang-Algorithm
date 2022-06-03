import java.io.*;
import java.util.*;
class Main{
	static int[] ch;
	static long sum = 0;
	public static long DFS(long k) {
		sum = 0;
		for(int i=0;i<ch.length;i++) {
			if(k-ch[i]<=0) sum+=ch[i]-k;
		}
		return sum;
	}
	public static void main(String[]args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer std = new StringTokenizer(br.readLine());
		int a= Integer.parseInt(std.nextToken());
		int b = Integer.parseInt(std.nextToken());
		ch = new int[a];
		long max =0;
		long min =0;
		std = new StringTokenizer(br.readLine());
		for(int i=0;i<a;i++) {
			ch[i] = Integer.parseInt(std.nextToken());
			max = Math.max(ch[i], max);
		}
		long d = 1;
		long hap = (max+min)/2;
		while(min<=max) {
			d = DFS(hap);
			if(d<b) max = hap-1;
			else if(d>b) min = hap+1;
			else break;
			hap = (max+min)/2;
		}
		System.out.println(hap);
		
	}
	
	
}
