package sproj.com.org;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

public class SPRO_DaeguDBManager implements DBInfo {
	
	public ArrayList<SPRO_DaeguData> select(){
		Connection conn= null;
		PreparedStatement pstmt =null;
		ResultSet rs =null;
		ArrayList<SPRO_DaeguData> list = new ArrayList<SPRO_DaeguData>();
		
		try {
			Class.forName(DBInfo.mysql_class);
			conn=DriverManager.getConnection(DBInfo.mysql_url,DBInfo.mysql_id,DBInfo.mysql_pw);
			pstmt=conn.prepareStatement("select * from daegu limit 0, 100");
			rs=pstmt.executeQuery();
			
			while(rs.next()) {
				SPRO_DaeguData dd= new SPRO_DaeguData();
				dd.setIdx(rs.getString("idx"));
				dd.setName(rs.getString("name"));
				dd.setLocation(rs.getString("location"));
				dd.setJibon_addr(rs.getString("jibon_addr"));
				list.add(dd);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(rs!=null)rs.close();
				if(conn!=null)conn.close();
				if(pstmt!=null)pstmt.close();
			}catch(Exception c) {
				
			}
		}return list;
	}
}
