<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%
	String a= request.getParameter("a");
	String b= request.getParameter("b");
	
	out.println("a= "+a);
	out.println("b= "+b);
	
	String c= request.getParameter("c");
	out.println("c= "+c); 
	
	Integer se_a= (Integer)session.getAttribute("a");
	String se_id= (String)session.getAttribute("id");
	String se_b= (String)session.getAttribute("b");
	
	out.println("se_a= "+ se_a);
	out.println("se_id= "+ se_id);
	out.println("se-b= "+se_b);
%>
</body>
</html>