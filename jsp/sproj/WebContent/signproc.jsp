<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.DriverManager"%>
<%@ page import="java.sql.PreparedStatement"%>
<%@ page import="java.sql.Connection"%>
<%
	String p_id = (String)request.getParameter("id");
	String p_pw = (String)request.getParameter("pw");
	String p_name = (String)request.getParameter("name");
	String p_phone = (String)request.getParameter("phone");

	String sucValue=null;

// 	out.println("<br>");
// 	out.println("p_id = "+ p_id);
// 	out.println("<br>");
// 	out.println("p_pw = "+ p_pw);
// 	out.println("<br>");
// 	out.println("p_name = "+ p_name);
// 	out.println("<br>");
// 	out.println("p_phone = "+ p_phone);
// 	out.println("<br>");
	
	Connection conn = null;
	PreparedStatement pstmt = null;
	try{
		// ojdbc jar 추가 확인
		Class.forName("oracle.jdbc.driver.OracleDriver");

		conn = 
		DriverManager.getConnection
		("jdbc:oracle:thin:@localhost:1521:xe", "AI", "1234");
		
		// 블럭 지정 후 ctrl+ shift + x 대문자 지정
		// 블럭 지정 후 ctrl+ shift + y 소문자 지정
		pstmt = conn.prepareStatement(
				"INSERT INTO "+ 
				"SPRO_MEMBER "+
				"VALUES "+
				"(SPROMEMBER.NEXTVAL,?,?,?,?)");
		
		pstmt.setString(1, p_id);//1번째 ?
		pstmt.setString(2, p_pw);//2번째 ?
		pstmt.setString(3, p_name);//3번째 ?
		pstmt.setString(4, p_phone);//4번째 ?
				
		int ret = pstmt.executeUpdate();
		if(ret > 0 ){
			System.out.println("정상적으로 insert 되었습니다.");
			sucValue="<a class='btn btn-primary' href='Index.jsp'>로그인 페이지 이동</a>";
			
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
		<%out.print(sucValue); %>
	</div>
</body>
</html>












