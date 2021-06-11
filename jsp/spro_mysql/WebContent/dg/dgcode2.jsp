<%@page import="sproj.com.org.dg.SPRO_DaeGUManager"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
	SPRO_DaeGUManager sdgm = new SPRO_DaeGUManager();
	String ret = sdgm.selectStr();
	//System.out.println(ret);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="/spro/css/mycss.css"/>
<script src="https://d3js.org/d3.v6.min.js"></script>
<style type="text/css">
	rect{
		stroke : rgb(100,0,0);
		stroke-width : 1px;
		fill : rgb(124,235,100);
	}
</style>
</head>
<body>
<div class="jumbotron">
	<h1>MY STUDY</h1>
	<p>
		code2 분류별 데이터 <br/>
		현재 코드2 분류시 최소 상권 분석 상위 5개<br/>
		유료회원시 모든 데이터 볼 수 있음.
	</p>
	<svg id="myGraph" width="430" height="300">
<!--         <rect x="10" y="30" width="100" height="80"/> -->
    </svg>
<!--     <script src="../js/sample.js"></script> -->
</div>
</body>
</html>
<script src="../js/sample07.js"></script>
<script type="text/javascript">
	doGra(<%=ret%>);
</script>
