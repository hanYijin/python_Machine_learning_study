<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ page import="com.mh.Ex01" %>
<%@ page import="com.mh.DDBox" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
안녕하세용 jsp
<%
	Ex01 ex01= new Ex01();
	ex01.doA();
	String re = ex01.reString();
	out.println(re);
	DBox<String, Integer> box1= new DBox<>();
	box1.set("Apple",25);
	DBox<String, Integer> box2= new DBox<>();
	box2.set("Orange",33);
	
	DDBox<DBox<String, Integer>,DBox<String, Integer>> ddbox= new DDBox<>();
	ddbox.set(box1,box2);
	System.out.println(ddbox);
%>
</body>
</html>