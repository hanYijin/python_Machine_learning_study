<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
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
	p:hover{
		background-color: rgb(255,0,255)
	}
</style>
</head>
<body>
<div class="jumbotron">
	<p>막대그래프</p>
	<svg id="myGraph" width="430" height="150"></svg>
</div>
</body>
</html>
<!--<script src="../js/sample.js"></script>-->
<script type="text/javascript">
//막대그래프 데이터(데이터 세트)
var dataSet = [300, 130, 5, 60, 240];
// 데이터를 기반으로 그리기
d3.select("#myGraph")
	.append("rect")
	.attr("x", 0)
	.attr("y", 25)
	.attr("width", dataSet[0])
	.attr("height", "20px")
	
d3.select("#myGraph")
	.append("rect")
	.attr("x", 0)
	.attr("y", 50)
	.attr("width", dataSet[1])
	.attr("height", "20px")
	
d3.select("#myGraph")
	.append("rect")
	.attr("x", 0)
	.attr("y", 75)
	.attr("width", dataSet[2])
	.attr("height", "20px")

d3.select("#myGraph")
	.append("rect")
	.attr("x", 0)
	.attr("y", 100)
	.attr("width", dataSet[3])
	.attr("height", "20px")

d3.select("#myGraph")
	.append("rect")
	.attr("x", 0)
	.attr("y", 125)
	.attr("width", dataSet[4])
	.attr("height", "20px")
</script>