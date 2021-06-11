package Studycafe.com.org;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DBmanager {
	String ora_class = "oracle.jdbc.driver.OracleDriver";
	String mysql_class="com.mysql.cj.jdbc.Driver";
	String ora_url = "jdbc:oracle:thin:@192.168.0.111:1521:xe";
	String mysql_url = "jdbc:mysql://localhost:3306/spro?useUnicode=true&characterEncoding=utf8"; 
	String mysql_id = "root";
	String mysql_pw = "1234";
	
	public Member checkLogin(String id, String pw) {
		Member member= null;
		Connection conn=null;
		PreparedStatement pstmt=null;
		ResultSet rs= null;
		try {
			Class.forName(mysql_class);
			conn=DriverManager.getConnection(mysql_url,mysql_id,mysql_pw);
			pstmt=conn.prepareStatement("SELECT * FROM MEMBER " + "WHERE ID=? AND PW=? ");
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
				if(pstmt!= null)pstmt.close();
				if(conn!= null)conn.close();
			}catch(Exception c) {
			
			}			
		}
		return member;
	}
	public int signInsert(String id, String pw, String name, String phone) {
		
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			Class.forName(mysql_class);
			conn=DriverManager.getConnection(mysql_url,mysql_id,mysql_pw);
			pstmt=conn.prepareStatement("INSERT INTO MEMBER (ID,PW,NAME,PHONE) VALUES (?,?,?,?)");
			
			pstmt.setString(1, id);
			pstmt.setString(2, pw);
			pstmt.setString(3, name);
			pstmt.setString(4, phone);
			int ret = pstmt.executeUpdate();
			if(ret>0) {
				System.out.println("정상적으로 insert 되었습니다");
				return ret;
			}
		}catch(Exception e){
			e.printStackTrace();
		}
		finally{
			try{
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch(Exception ex){
				
			}
		}
		return 0;
	}
	public int seatSelect(String seat, String name, String phone, String time) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		try{
			// ojdbc jar 추가 확인
			Class.forName(mysql_class);

			conn = 
			DriverManager.getConnection
			(mysql_url, mysql_id, mysql_pw);
			
			// 블럭 지정 후 ctrl+ shift + x 대문자 지정
			// 블럭 지정 후 ctrl+ shift + y 소문자 지정
			pstmt = conn.prepareStatement(
					"INSERT INTO "+ 
					"SEAT_USE "+
					"(NUM,NAME,PHONE,M_TIME)"+
					"VALUES "+
					"(?,?,?,?)");
			
			pstmt.setString(1, seat);//1번째 ?
			pstmt.setString(2, name);//2번째 ?
			pstmt.setString(3, phone);//3번째 ?
			pstmt.setString(4, time);//4번째 ?
					
			int ret = pstmt.executeUpdate();
			if(ret > 0 ){
				System.out.println("정상적으로 insert 되었습니다.");
				return ret;
				
			}
		}
		catch(Exception e){
			e.printStackTrace();
		}
		finally{
			try{
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch(Exception ex){
				
			}
		}
		return 0;
	}
}
