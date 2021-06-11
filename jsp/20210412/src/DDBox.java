//class DBox<L,R>{
//	private L left;
//	private R right;
//	public void set(L o, R r) {
//		left=o;
//		right=r;
//	}
//	public String toString() {return left+ " & "+ right;}
//}
public class DDBox<U, D> {
	private U u;
	private D d;
	public void set(U u, D d) {
		this.u=u;
		this.d=d;
	}
	public String toString() {return u+"\n"+ d;}
	
	public static void main(String[] args) {
		DBox<String, Integer> box1= new DBox<>();
		box1.set("Apple",25);
		DBox<String, Integer> box2= new DBox<>();
		box2.set("Orange",33);
		
		DBox<DBox<String,Integer>,DBox<String, Integer>> dbox= new DBox<>();
		dbox.set(box1,box2);
		String doublebox= dbox.printBox();
		System.out.println(doublebox);
		
	}
}