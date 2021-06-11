package sproj.com.org;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class Default implements DBInfo {
	public void copy() {
SPRO_MEMBER member =null;
		
		Connection conn = null; //DB ¿¬°á°´Ã¼
		PreparedStatement pstmt= null;
		ResultSet rs =null;
		try {
			Class.forName(DBInfo.mysql_class);
			conn= DriverManager.getConnection(DBInfo.mysql_url, DBInfo.mysql_id, DBInfo.mysql_pw);
			pstmt= conn.prepareStatement("SELECT * FROM MEMBER " + 
					"WHERE ID=? AND PW=? ");
			rs= pstmt.executeQuery();
			
			if(rs.next()) {
				 
			}
		
			
		}catch(Exception e) {
			e.printStackTrace();
		
		}
		finally {
			try {
				if(rs!=null)rs.close();
				if(pstmt!= null)pstmt.close();
				if(conn!= null)conn.close();
			}catch(Exception c) {
				
			}			
		}
	}
}


