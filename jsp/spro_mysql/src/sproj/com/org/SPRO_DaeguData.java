package sproj.com.org;

public class SPRO_DaeguData {
	private String idx;
	private String name;
	private String location;
	private String jibon_addr;
	public String getIdx() {
		return idx;
	}
	public void setIdx(String idx) {
		this.idx = idx;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getLocation() {
		return location;
	}
	public void setLocation(String location) {
		this.location = location;
	}
	public String getJibon_addr() {
		return jibon_addr;
	}
	public void setJibon_addr(String jibon_addr) {
		this.jibon_addr = jibon_addr;
	}
	@Override
	public String toString() {
		return "SPRO_DaeguDate [idx=" + idx + ", name=" + name + ", location=" + location + ", jibon_addr=" + jibon_addr
				+ "]";
	}
	
	
}
