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
		height : 500px;
		margin : 0 auto;
		background-color: #c8c8c8;
		padding: 150px 100px;
		box-sizing: border-box;
	}
</style>
<script type="text/javascript">
	window.onload=function(){
		document.getElementById('customer').onclick=function(){
			location.href='customer.jsp';
		}
		document.getElementById('pharmacy').onclick=function(){
			location.href='pharmacy.jsp';
		}
	}
</script>

</head>
<body>
	<div class="container">
		<table>
			<tr>
				<td>고객용</td><br>
				<td><input type="button" value="고객용" id="customer"></td>
				<td>약국용</td><br>
				<td><input type="button" value="약국용" id="pharmacy"></td>
			</tr>
		</table>
	</div>
</body>
</html>
