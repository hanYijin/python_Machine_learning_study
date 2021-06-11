package sproj.com.org;

public class SPRO_MEMBER {
	private String id;
	private String pw;
	private String name;
	private String phone;
	//alt + shift +s -> r :getter, setter
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPw() {
		return pw;
	}
	public void setPw(String pw) {
		this.pw = pw;
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
	//alt + shift + s -> s : 오버라이딩
	@Override
	public String toString() {
		return "SPRO_MEMBER [id=" + id + ", pw=" + pw + ", name=" + name + ", phone=" + phone + "]";
	}
	

}
