<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>
<%@ page import="sproj.com.org.SPRO_DBManager" %>
<%@ page import="sproj.com.org.SPRO_MEMBER" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script	src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="/sproj/css/mycss.css"/>
</head>
<body>
	<div class="jumbotron">
		<h1>My Study</h1>
		<p>공부하자!</p>
	</div>
</body>
</html>
<%
	String id=request.getParameter("id");//
	String pw=request.getParameter("pw");
	out.println("id= "+id);
	out.println("pw= "+pw);
	
	SPRO_DBManager sdbm = new SPRO_DBManager();
	SPRO_MEMBER ret = sdbm.CKLogin(id,pw);
	if(ret!=null)
	{
		out.println("로그인 성공");
		session.setAttribute("id",id);
		session.setAttribute("pw",pw);
		session.setAttribute("name",ret.getName());
		session.setAttribute("id",ret.getPhone());
	
		//out.println("세션에 저장 성공");
		out.println("<a href='Index.jsp' class='btn btn-primary'>메인페이지</a>");
	}else{
		out.println("로그인 실패");
		out.println("<a href= 'index.jsp' class='btn btn-primary'>로그인 창</a>");
	}
%>
