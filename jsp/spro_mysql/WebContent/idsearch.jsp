<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
	window.onload= function(){
		document.getElmentById('getid').onclick=function(){
			var name= document.getElementById('name');
			var phone= document.getelemntById('phone');
			location.href ='myid.jsp?name='+name.value+'&phone= '+phone.value;
		}
	}
</script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script	src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="/sproj/css/mycss.css"/>
</head>
<body>
	<div class="jumbotron">
		<div class="form-group">
			<label for="name">Name:</label> 
			<input type="text" class="form-control"	id="name">
		</div>
		<div class="form-group">
			<label for="phone">Phone:</label> 
			<input type="text" class="form-control" id="phone">
		</div>
			<input type="button" value="ID찾기" id="getid" class="btn btn-primary ml-2 mr-2">
	</div>

</body>
</html>