
<%@page import="java.util.ArrayList"%>
<%@page import="sproj.com.org.SPRO_SeatDBManager"%>
<%@page import="sproj.com.org.SPRO_seatUse"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%
	SPRO_SeatDBManager ssdm= new SPRO_SeatDBManager();
	ArrayList<SPRO_seatUse> list= ssdm.select();
	out.print("list.size()= "+list.size());
	
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
.mybgwh{
	/* r g b 255 255 255 */
	background-color:#555;
	color: white;
	
}
</style>
</head>
<body>
	<div class="container mybgwh">
		관리자 화면 입니다.
		<table class ="table table-dark table-hover">
			<thead>
				<tr>
					<td>좌석</td><td>이름</td><td>연락처</td><td>충전시간</td>
				</tr>
			</thead>
			<tbody>
			<% for(int i=0; i<list.size();i++){ 
				SPRO_seatUse ssu= list.get(i);
			%>
				<tr>
					<td><%out.print(ssu.getNum()); %></td>
					<td><%out.print(ssu.getName()); %></td>
					<td><%out.print(ssu.getPhone()); %></td>
					<td><%out.print(ssu.getM_time()); %></td>
				</tr>
			<% } %>
			</tbody>
		</table>
	</div>
<!--	<div class="container bg-dark text-white">
		관리자 화면 입니다.
	</div>-->
</body>
</html>