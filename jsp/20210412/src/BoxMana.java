
public class BoxMana {
	BoxMana(){
		//자료형을 정함
		Box<Apple> abox = new Box<Apple>(new Apple());
		Box<Orange> bbox= new Box<Orange>(new Orange());
		
		Apple a= abox.getObj();
		Orange b= bbox.getObj();
		
//		Apple aa= bbox.getObj(); error 오류를 바로 확인 가능해진다.
		
		System.out.println(a);
		System.out.println(b);
		
	}
	public static void main(String[] args) {
		new BoxMana();
	}

}
