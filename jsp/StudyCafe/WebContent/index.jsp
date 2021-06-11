<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script	src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="/sproj/css/mycss.css"/>
<script type="text/javascript">
	window.onload=function(){
		document.getElementById('idsearch').onclick=function(){
			location.href='idsearch.jsp';
		}
		document.getElementById('login').onclick=function(){
			location.href='login.jsp';
		}
		document.getElementById('signin').onclick=function(){
			location.href='singin.jsp';
		}
		document.getElementById('outroom').onclick=function(){
			location.href='outroom.jsp';
		}
	}
	$('document').ready(function(){
		$('#seatsel').on('click', function(){
			location.href='seatsel.jsp';
		})
		$('#logout').on('click',function(){
			location.href='logout.jsp';
		})
		$('#chart').on('click', funtction(){
			location.href='view/deaguMain.jsp';
		})
	})
</script>
</head>
<body>
	<div class="jumbotron">
		<div class="row">
			<input class="btn btn-primary ml-3 mb-2" type="button" id="chart" value="차트"/>
		</div>
		<h1>STUDY CAFE</h1>
		<p>열공하자!</p>
		<% 
			Object name=session.getAttribute("name");
			if(name!=null){
		%>
			안녕하세요 <% out.println((String)name); %>님 :)
		<%}else{ %>
		<form action='login.jsp' method='post'>
		<div class="form-group">
			<label for="id">Id:</label>
			<input type="text" class="form-control" name="id">
		</div>
			<div class="form-group">
			<label for="pw">Password:</label> 
			<input type="password" class="form-control" name="pw">
		</div>
		<% } %>
		<div class="row">
			<input type="button" value="ID찾기" id="idsearch" class="btn btn-primary ml-2 mr-2">
		<%
			if(name!=null){
		%>
			<input type= "button" value="로그아웃" id="logout" class="btn btn-primary ml-2 mr-2">
		<%}else{ %>
			<input type="submit" value="로그인" id="login" class="btn btn-primary ml-2 mr-2">
		<% } %>
			<input type="button" value="회원가입" id="signin" class="btn btn-primary mr-2">
			<input type="button" value="좌석선택" id="seatsel" class="btn btn-primary mr-2">
			<input type="button" value="시간충전" id="timecharge" class="btn btn-primary mr-2">
			<input type="button" value="퇴실" id="outroom" class="btn btn-primary mr-2">
		</div>
		</form>
	</div>
</body>
</html>