<%@page import="Studycafe.com.org.DBmanager"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%
	DBmanager dbm= new DBmanager();
	String id= (String)request.getParameter("id");
	String pw= (String)request.getParameter("pw");
	String name= (String)request.getParameter("name");
	String phone= (String)request.getParameter("phone");
	
	String sucValue="";
	request.setCharacterEncoding("utf-8");
	dbm.signInsert(id, pw, name, phone);
	sucValue="<a href='index.jsp' class='btn btn-primary'>로그인 창 </a>";
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