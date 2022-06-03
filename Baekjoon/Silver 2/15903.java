import java.io.*;
import java.util.*;
class Main{
	public static void main(String[]args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer std = new StringTokenizer(br.readLine());
		PriorityQueue<Long> Q = new PriorityQueue<>();
		int a = Integer.parseInt(std.nextToken());
		int b = Integer.parseInt(std.nextToken());
		long[] ch = new long[a];
		std = new StringTokenizer(br.readLine());
		for(int i=0;i<a;i++) {
			ch[i] = Integer.parseInt(std.nextToken());
			Q.offer(ch[i]);
		}
		int cnt=0;
		while(cnt<b) {
			long x = Q.poll();
			long y = Q.poll();
			long hap = x+y;
			Q.offer(hap); Q.offer(hap);
			cnt++;
		}
		long sum=0;
		int len = Q.size();
		for(int i=0;i<len;i++) sum += Q.poll();
		System.out.println(sum);
	}
}
