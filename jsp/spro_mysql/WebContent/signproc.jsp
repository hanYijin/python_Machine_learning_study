<%@page import="sproj.com.org.SPRO_DBManager"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.DriverManager"%>
<%@ page import="java.sql.PreparedStatement"%>
<%@ page import="java.sql.Connection"%>
<%
	SPRO_DBManager sdbm = new SPRO_DBManager();
	String p_id = (String)request.getParameter("id");
	String p_pw = (String)request.getParameter("pw");
	String p_name = (String)request.getParameter("name");
	String p_phone = (String)request.getParameter("phone");

	String sucValue="";
	request.setCharacterEncoding("utf-8");
	int ret=sdbm.signInsert(p_id, p_pw, p_name, p_phone);
	out.println("ret= "+ret);
	sucValue="<a href='Index.jsp' class='btn btn-primary'>로그인 창 </a>";
	
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












