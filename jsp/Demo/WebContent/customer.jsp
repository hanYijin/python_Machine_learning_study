<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
	.container{
		width : 800px;
		height: 500px;
		margin: 0 auto;
		background-color: #C9D9D2;
		padding: 200px 160px;
		box-sizing: border-box;
		}
	#tab{
		mrgin-top: 100px;
	}
</style>
<script type="text/javascript">
	window.onload=function(){
		document.getElementById('login').onclick=function(){
			
			location.href='order.jsp';
		}
	}
</script>
</head>
<body>
<%
	String id=request.getParameter("id");
	String pw=request.getParameter("pw");
%>
<div class="container">
	<table>
		<tr>
			<td>로그인</td>
		</tr>
		<tr>
			<td><input type="text" name="Id" id="id"/></td>
			<td><input type="text" name="pw" id="pw"/></td>
			<td><input type="button" value="로그인" id="login"></td>
		</tr>
		</tr>
	</table>
	<div id="tab"></div>
	<table>
		<tr>
			<td>신규 고객</td>
			<td><input type="button" value="회원가입" id="signin"></td>
		</tr>
	</table>
	
</div>

</body>
</html>