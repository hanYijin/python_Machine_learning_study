public class Box <T> {

	private T ob;
	
	public void set(T ob){
		this.ob=ob;
	}
	public T get() {
		return ob;
	}
	public static void main(String[] args) {
		Box<Integer> b = new Box<>();
		b.set(125);
		int num= b.get();
		System.out.println(num);
		System.out.println(b.get());
	}
}