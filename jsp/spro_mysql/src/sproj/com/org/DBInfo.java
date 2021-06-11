package sproj.com.org;

public interface DBInfo {
	String ora_class = "oracle.jdbc.driver.OracleDriver";
	String mysql_class="com.mysql.cj.jdbc.Driver";
	String ora_url = "jdbc:oracle:thin:@192.168.0.111:1521:xe";
	String mysql_url = "jdbc:mysql://localhost:3306/spro?useUnicode=true&characterEncoding=utf8"; 
	String mysql_id = "root";
	String mysql_pw = "1234";

}
