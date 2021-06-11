<%@ page language="java" contentType="text/html; charset=EUC-KR" pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
<script type="text/javascript">
	window.onload=function(){
		document.getElementById('idsearch').onclick=function(){
			location.href='Idsearch.jsp';
		}
		document.getElementById('login').onclick=function(){
			var id = document.getElementById('id');
			var pw= document.getElementById('pw');
			location.href='Login.jsp?id='+id.value+'&pw='+pw.value;
		}
		document.getElementById('signin').onclick=function(){
			location.href='Signin.jsp';
		}
		document.getElementById('logout').onclick=function(){
			location.href='Logout.jsp;'
		}
		
	}
</script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script	src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<script type="text/javascript">
	$('document').ready(function(){
		$('#select').on('click', function(){
			location.href='Select.jsp';
		})
	})
</script>
</head>
<body>
	<div class="jumbotron">
		<h1>My Study</h1>
		<p>공부하자!</p>
		<div class="form-group">
			<label for ="id">Id</label>
			<input type="text" class="form-control" id="id">
		</div>
		<div class="form-group">
			<label for="pw">Password</label>
			<input type="password" class="form-control" id="pw">
		</div>
		<div class="row">
			<input type="button" value="ID찾기" id="idsearch" class="btn btn-primary ml-2 mr-2"/>
			<input type="button" value="로그인" id="login" class="btn btn-primary mr-2"/>
			<input type="button" value="회원가입" id="signin" class="btn btn-primary mr-2"/>
			<input type="button" value="좌석선택" id="select" class="btn btn-primary mr-2"/>
			<input type="button" value="시간충전" id="timeplus" class="btn btn-primary mr-2"/>
			<input type="button" value="퇴실" id="logout" class="btn btn-primary mr-2"/>
		</div>
	</div>
</body>
</html>