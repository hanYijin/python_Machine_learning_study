package study.com.org;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DBManager {
	public Member CkLogin(String id, String pw) {
		Member member= null;
		Connection conn=null;
		PreparedStatement pstmt = null;
		ResultSet rs =null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe", "AI", "1234");
			pstmt= conn.prepareStatement("SELECT * FROM SPRO_MEMBER " + 
					"WHERE ID=? AND PW=?");
			pstmt.setString(1, id);
			pstmt.setString(2, pw);
			rs=pstmt.executeQuery();
			
			if(rs.next()) {
				member= new Member();
				member.setId(id);
				member.setPw(pw);
				member.setName(rs.getString("name"));
				member.setPhone(rs.getString("phone"));
				
			}
		}catch(Exception e) {
			e.printStackTrace();
			
		}
		finally {
			try {
				if(rs!=null)rs.close();
				if(pstmt!=null)pstmt.close();
				if(conn!=null)conn.close();
			}catch(Exception ex) {
			
			}
		}return member;
	}
}
