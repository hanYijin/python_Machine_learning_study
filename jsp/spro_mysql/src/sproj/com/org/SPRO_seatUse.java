package sproj.com.org;
/*
 * 테이블과 1:1 맵핑관계에 해당되는 클래스
 */

public class SPRO_seatUse {
	private int num;
	private String name;
	private String phone;
	private int m_time;
	
	//alt + shift + s -> r getter setter 만들기
 	public int getNum() {
		return num;
	}
	public void setNum(int num) {
		this.num = num;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public int getM_time() {
		return m_time;
	}
	public void setM_time(int m_time) {
		this.m_time = m_time;
	}
	
	//alt + shift + s -> s toString() 
	@Override
	public String toString() {
		return "SPRO_seatUse [num=" + num + ", name=" + name + ", phone=" + phone + ", m_time=" + m_time + "]";
	}
	
	

}
