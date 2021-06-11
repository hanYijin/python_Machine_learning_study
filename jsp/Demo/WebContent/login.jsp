<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	String id= request.getParameter("id");
	String pw= request.getParameter("pw");
	out.println("id= "+id);
	out.println("pw= "+pw);
	Connection conn =null;
	PreparedStatement pstmt= null;
	try{
		Class.forName("oracle.jdbc.driver.OracleDriver");
		conn= DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe", "AI", "1234");
		pstmt= conn.prepareStatement("select ID,Pw from SPRO_MEMBER where Id= ?, pw=?");
		pstmt.setString(1,id);
		pstmt.setString(2,pw);
		
	}catch(Exception e){
		e.printStackTrace();
	}
%>

</body>
</html>