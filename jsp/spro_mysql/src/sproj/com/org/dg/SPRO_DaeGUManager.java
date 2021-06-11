package sproj.com.org.dg;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import sproj.com.org.DBInfo;
import sproj.com.org.SPRO_MEMBER;

public class SPRO_DaeGUManager {
	
	public String selectcode4() {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String ret = "[";
		try{
			Class.forName(DBInfo.mysql_class);
			conn = DriverManager.getConnection(DBInfo.mysql_url, DBInfo.mysql_id, DBInfo.mysql_pw);
			// 블럭 지정 후 ctrl+ shift + x 대문자 지정
			// 블럭 지정 후 ctrl+ shift + y 소문자 지정
			pstmt = conn.prepareStatement(
					" select code4, count(*) as cnt from daegu " + 
					" group by code4 " + 
					" having cnt> 30 " + 
					" order by cnt asc limit 0,100");
			rs = pstmt.executeQuery();
			while(rs.next()){
				if(rs.isLast())
					ret += rs.getInt("cnt");
				else
					ret += rs.getInt("cnt")+",";
			}
			ret +="]";
			System.out.println("ret= "+ ret);
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
		return ret;
	}
	
	/*
	 * json
	 * [
	 *  { name:'상권1', cnt: 20},
	 *  { name:'상권2', cnt: 30},
	 *  { name:'상권3', cnt: 40},
	 * ]
	 */
	public String selectcode4name() {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String ret = "[";
		try{
			Class.forName(DBInfo.mysql_class);
			conn = DriverManager.getConnection(DBInfo.mysql_url, DBInfo.mysql_id, DBInfo.mysql_pw);
			// 블럭 지정 후 ctrl+ shift + x 대문자 지정
			// 블럭 지정 후 ctrl+ shift + y 소문자 지정
			pstmt = conn.prepareStatement(
					" select code4, count(*) as cnt from daegu " + 
					" group by code4 " + 
					" having cnt> 30 " + 
					" order by cnt asc limit 0,100");
			rs = pstmt.executeQuery();
			while(rs.next()){
				if(rs.isLast())//마지막 결과 값이면 true 아니면 false
					ret += "'"+rs.getString("code4")+"'";//마지막 결과 구문
				else
					ret += "'"+rs.getString("code4")+"',";// 마지막이 아닐때 결과 구문
			}
			ret +="]";
			System.out.println("ret= "+ ret);
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
		return ret;
	}
	
	public String selectStr() {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		String ret = "[";
		try{
			Class.forName(DBInfo.mysql_class);
			conn = DriverManager.getConnection(DBInfo.mysql_url, DBInfo.mysql_id, DBInfo.mysql_pw);
			// 블럭 지정 후 ctrl+ shift + x 대문자 지정
			// 블럭 지정 후 ctrl+ shift + y 소문자 지정
			pstmt = conn.prepareStatement(
					" select code2_name as name, count(*) as cnt from daegu " +
					" group by code2_name " +
					" order by cnt asc " +
					" limit 0,10");
			rs = pstmt.executeQuery();
			while(rs.next()){
				if(rs.isLast())
					ret += rs.getInt("cnt");
				else
					ret += rs.getInt("cnt")+",";
			}
			ret +="]";
			System.out.println("ret= "+ ret);
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
		return ret;
	}

	public List<SPRO_DaeGU> select(int pageNum) {
		List<SPRO_DaeGU> list = new ArrayList<SPRO_DaeGU>();
		pageNum=0;
		Connection conn = null; //DB 연결객체
		PreparedStatement pstmt= null;
		ResultSet rs =null;
		try {
			Class.forName(DBInfo.mysql_class);
			conn= DriverManager.getConnection(DBInfo.mysql_url, DBInfo.mysql_id, DBInfo.mysql_pw);
			pstmt= conn.prepareStatement("SELECT * FROM daegu limit "+ pageNum +", 10");
			rs= pstmt.executeQuery();
			
			while(rs.next()) {
				SPRO_DaeGU sd= new SPRO_DaeGU();
				
				sd.setIdx(rs.getInt("idx"));
				sd.setName(rs.getString("name"));
				sd.setCode1(rs.getString("code1"));
				sd.setCode1_name(rs.getString("code1_name"));
				sd.setCode2(rs.getString("code2"));
				sd.setCode2_name(rs.getString("code2_name"));
				sd.setCode4(rs.getString("code4"));
				sd.setCode4_name(rs.getString("code4_name"));
				sd.setDoro_addr(rs.getString("doro_addr"));
				list.add(sd);
				
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
		}return list;
	}

	public int pageCount() {
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try{
			Class.forName(DBInfo.mysql_class);
			conn = DriverManager.getConnection(DBInfo.mysql_url, DBInfo.mysql_id, DBInfo.mysql_pw);
			// 블럭 지정 후 ctrl+ shift + x 대문자 지정
			// 블럭 지정 후 ctrl+ shift + y 소문자 지정
			pstmt = conn.prepareStatement(" select count(*) from daegu ");
			rs = pstmt.executeQuery();
			while(rs.next()){
				int rowcnt= rs.getInt(1);
				System.out.println("rowcnt= "+rowcnt);
				int pagecnt=rowcnt/10;
				if(rowcnt%10>0)
					pagecnt++;
				System.out.println("현재페이지 갯수pagecnt= "+pagecnt);
				return pagecnt;
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
		}return 0;
	}
}

