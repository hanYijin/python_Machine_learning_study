package sproj.com.org;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

/*
 * mysql 데이터베이스와 연결해서
 * seatuse
 * select insert update delete 함수 구현
 */
public class SPRO_SeatDBManager implements DBInfo {
	
	public ArrayList<SPRO_seatUse> select() {
		Connection conn = null; //DB 연결 객체 변수
		PreparedStatement pstmt=null; // SQL 만드는 객체 변수
		ResultSet rs =null; //sql문 실행하고 반환값 담는 객체 변수
		ArrayList<SPRO_seatUse> list = new ArrayList<SPRO_seatUse>();
		
		try {
			Class.forName(DBInfo.mysql_class);
			conn=DriverManager.getConnection(DBInfo.mysql_url,DBInfo.mysql_id,DBInfo.mysql_pw);
			pstmt=conn.prepareStatement("Select*from seat_use");
			rs=pstmt.executeQuery();
			
			while(rs.next()) {
				SPRO_seatUse ssu = new SPRO_seatUse();
				ssu.setM_time(rs.getInt("m_time"));
				ssu.setName(rs.getString("name"));
				ssu.setPhone(rs.getString("phone"));
				ssu.setNum(rs.getInt("num"));
				list.add(ssu);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(rs!=null)rs.close();
				if(pstmt!= null)pstmt.close();
				if(conn!= null)conn.close();
			}catch(Exception c) {
				
			}			
		}return list;
	}

}
