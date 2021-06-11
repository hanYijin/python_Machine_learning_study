<%@page import="sproj.com.org.SPRO_DaeguData"%>
<%@page import="java.util.ArrayList"%>
<%@page import="sproj.com.org.SPRO_DaeguDBManager"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%
	SPRO_DaeguDBManager sddm = new SPRO_DaeguDBManager();
	ArrayList<SPRO_DaeguData> list = sddm.select();
	out.print(list.size());
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
<link rel="stylesheet" href="/sproj/css/mycss.css"/>
<style type="text/css">
 	tr:hover{
 		color: hotpink;
 	}
</style>
</head>
<body>
	<div class="container">
		<h1>대구 상권 데이터 출력</h1>
		<table class="table table-striped">
			<thead>
				<tr>
					<td>상권번호</td><td>상호명</td><td>위치</td><td>주소</td>
				</tr>
			</thead>
			<tbody>
			<%
				for(int i=0; i<list.size();i++){
					SPRO_DaeguData dd= list.get(i);
			%>
				<tr>
					<td><%out.print(dd.getIdx()); %></td>
					<td><%out.print(dd.getName()); %></td>
					<td><%out.print(dd.getLocation());%></td>
					<td><%out.print(dd.getJibon_addr()); %></td>
				</tr>
				<% } %>
			</tbody>
		</table>
	</div>
</body>
</html>