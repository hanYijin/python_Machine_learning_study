<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%
	String p_id=(String)request.getParameter("id");
	String p_pw=(String)request.getParameter("pw");
	String p_name=(String)request.getParameter("name");
	String p_phone=(String)request.getParameter("phone");
	String sncValue = null;
	
	Connection conn =null;
	PreparedStatement pstmt=null;
	
	try{
		Class.forName("oracle.jdbc.driver.OracleDriver");
		
		conn=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe", "AI", "1234");
		pstmt=conn.prepareStatement("INSERT INTO SPRO_MEMBER VALUES (SPROMEMBER.NEXTVAL,?,?,?,?)");
		
		pstmt.setString(1,p_id);
		pstmt.setString(2,p_pw);
		pstmt.setString(3, p_name);
		pstmt.setString(4,p_phone);
		
		int ret=pstmt.executeUpdate();
		if(ret>0){
			System.out.println("정상적으로 insert 되었습니다.");
			sncValue="<a class='btn btn-primary' href='Open.jsp'>로그인 페이지로 이동</a>";
		}
	}catch(Exception e){
		e.printStackTrace();
	}
	finally{
		try{
			if(pstmt !=null)pstmt.close();
			if(conn!=null)conn.close();
		}catch(Exception ex){
			
		}
	}
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script	src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
	<div class="jumbotron">
		<h1>My Study</h1>
		<p>공부하자!</p>
		<%out.print(sncValue); %>
	</div>
</body>
</html>