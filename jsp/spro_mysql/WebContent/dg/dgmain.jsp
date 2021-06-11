<%@page import="sproj.com.org.dg.SPRO_DaeGU"%>
<%@page import="java.util.List"%>
<%@page import="sproj.com.org.dg.SPRO_DaeGUManager"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
 <%
 	SPRO_DaeGUManager sdbm = new SPRO_DaeGUManager();
 	List<SPRO_DaeGU> list= sdbm.select(0); //List 컬렉션 자료구조 
 	int pagecnt= sdbm.pageCount();
 	out.print(pagecnt);

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
<script type="text/javascript">
	$(document).ready(function(){
		$('#code2').on('click',function(){
			location.href='dgcode2.jsp';
		});
		$('#code4').on('click', function(){
			location.href='dgcode4.jsp';
		});
	})
</script>
</head>
<body>
	<div class="jumbotron">
		<div class="row ml-2 mb-2">
			<input class="btn btn-primary mr-2" type="button" value ="분류2" id="code2"/>
			<input class="btn btn-primary" type="button" value ="분류4" id="code4"/>
		</div>
		<h1>My Study</h1>
		<p>대구 상권</p>
		<table class="table table-dark table-hover">
			<thead>
				<tr>
					<td>순번</td><td>이름</td><td>코드</td>
					<td>코드</td><td>코드</td><td>주소</td>
				</tr>
			</thead>
			<tbody>
				<% for(SPRO_DaeGU sd : list){ %>
				<tr>
					<td><%=sd.getIdx()%></td>
					<td><%=sd.getName()%></td>
					<td><%=sd.getCode1_name()%></td>
					<td><%=sd.getCode2_name()%></td>
					<td><%=sd.getCode4_name()%></td>
					<td><%=sd.getDoro_addr()%></td>
				</tr>
				<% } %>
			</tbody>
		</table>
		<%
			for(int i=1; i<pagecnt; i++){
				out.print(" <a href=\"?pagecnt="+i+"\">["+i+"]</a> ");
			}
		%>
	</div>
</body>
</html>