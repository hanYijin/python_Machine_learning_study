<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.PreparedStatement"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String p_id=(String)request.getParameter("id");
	String p_pw=(String)request.getParameter("pw");
	String p_name=(String)request.getParameter("name");
	String p_phone=(String)request.getParameter("phone");
	
	out.println("<br>");
	out.println("p_id = "+ p_id);
	out.println("<br>");
	out.println("p_pw = "+ p_pw);
	out.println("<br>");
	out.println("p_name = "+ p_name);
	out.println("<br>");
	out.println("p_phone = "+ p_phone);
	out.println("<br>");
	Connection conn = null;
	PreparedStatement pstmt=null;
	
	try{
			Class.forName("oracle.jdbc.driver.OracleDriver");
			conn= DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe", "AI", "1234");
			pstmt= conn.prepareStatement("INSERT INTO"+" SPRO_MEMEBER"+ "VALUES"+"(SPROMEMBER.NEXTVAL,?,?,?,?)");
			pstmt.setString(1,p_id);
			pstmt.setString(2,p_pw);
			pstmt.setString(3,p_name);
			pstmt.setString(4,p_phone);
			int ret=pstmt.executeUpdate();
			if(ret>0){
				System.out.println("insert 성공");
				out.println("<input type='button' href='Index.jsp' onclick=''/>");
			}
			
		
	}catch(Exception e){
		e.printStackTrace();
	}
	finally{
		try{
			if(pstmt!=null)pstmt.close();
			if(conn!=null)conn.close();
		}catch(Exception ex){
		
		}
	}
	
%>
