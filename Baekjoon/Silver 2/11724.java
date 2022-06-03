import java.io.*;
import java.util.*;
class point{
	int x,y;
	point(int x,int y){
		this.x=x;
		this.y=y;
	}
}
class Main{
	static int a;
	static int[] ch;
	public static int FInd(int k) {
		if(k==ch[k]) return k;
		else return ch[k] =	FInd(ch[k]);
	}
	public static void main(String[]args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer std = new StringTokenizer(br.readLine());
		ArrayList<point> list = new ArrayList<>();
		ArrayList<Integer> lis = new ArrayList<>();
		a = Integer.parseInt(std.nextToken());
		int b = Integer.parseInt(std.nextToken());
		ch = new int[a+1];
		for(int i=1;i<=a;i++) ch[i] = i;
		for(int i=0;i<b;i++) {
			std = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(std.nextToken());
			int y = Integer.parseInt(std.nextToken());
			list.add(new point(x,y));
		}
		for(int i=0;i<list.size();i++) {
			ch[list.get(i).x] = FInd(list.get(i).x);
			ch[list.get(i).y] = FInd(list.get(i).y);
			if(ch[list.get(i).x]!=ch[list.get(i).y]) ch[ch[list.get(i).x]] = ch[list.get(i).y]; 
		}
		for(int i=1;i<=a;i++) {
			if(!lis.contains(FInd(ch[i]))) lis.add(FInd(ch[i]));
		}
		
		System.out.println(lis.size());

		
	}
}
