<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

<script type="text/javascript">
	window.onload = function() {
		document.getElementById('idsearch').onclick = function() {
			location.href = 'idsearch.jsp'; //idsearch.jsp 페이지로 이동
		}
		document.getElementById('login').onclick = function() {
			var id = document.getElementById('id');//입력받은 아이디 변수 저장
			var pw = document.getElementById('pw');//입력받은 비밀번호 변수 저장
			location.href = 'login.jsp?id=' + id.value + '&pw=' + pw.value;
			//		location.href='login.jsp'; //login.jsp 페이지로 이동

		}
		document.getElementById('signin').onclick = function() {
			location.href = 'signin.jsp'; //signin.jsp 페이지로 이동
		}
		document.getElementById('outroom').onclick = function() {
			location.href = 'outroom.jsp'; //outroom.jsp 페이지로 이동
		}
	}
</script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script	src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="/sproj/css/mycss.css"/>
<script type="text/javascript">
	$('document').ready(function(){
		$('#seatsel').on('click',function(){ 
			location.href='seatsel.jsp';
		} ) //익명함수
		$('#loginout').on('click',function(){
			location.href='logout.jsp';
		})
		$('#chart').on('click',function(){
			location.href='dg/dgmain.jsp';
		})
	})
</script>
<body>
	<div class="jumbotron text-center">
  <h1>My First Bootstrap Page</h1>
		<div class="row">
			<input class="btn btn-primary ml-3 mb-2" type="button" id="chart" value="차트"/>
		</div>
		<h1>My Study</h1>
		<p>공부하자!</p>
		<%  
			Object name=session.getAttribute("name");
			if(name!=null){ 
		%>
			안녕하세요.<% out.println((String)name); %>님 :)
		<% }else{ %>
		<div class="form-group">
			<label for="id">Id:</label> 
			<input type="text" class="form-control"	id="id">
		</div>
		<div class="form-group">
			<label for="pw">Password:</label> 
			<input type="password" class="form-control" id="pw">
		</div>
		<% } %>
		<div class="row">
			<input type="button" value="ID찾기" id="idsearch" class="btn btn-primary ml-2 mr-2"> 
			<%
				if(name!=null){ 
			%>
			<input type="button" value="로그아웃" id="loginout" class="btn btn-primary mr-2">
			<% }else{ %>
			<input type="button" value="로그인" id="login" class="btn btn-primary mr-2">
			<%} %>
			<input type="button" value="회원가입" id="signin" class="btn btn-primary mr-2">
			<input type="button" value="좌석선택" id="seatsel" class="btn btn-primary mr-2">
			<input type="button" value="시간충전" id="timecharge" class="btn btn-primary mr-2">
			<input type="button" value="퇴실" id="outroom" class="btn btn-primary mr-2">
		</div>
	</div>

	<div class="container">
		<div class="row">
			<div class="col-sm-4">
				<h3>Column 1</h3>
				<p>첫번째 컬럼.</p>
				<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
			</div>
			<div class="col-sm-4">
				<h3>Column 2</h3>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
				<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
			</div>
			<div class="col-sm-4">
				<h3>Column 3</h3>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
				<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
			</div>
		</div>
	</div>

</body>
</html>