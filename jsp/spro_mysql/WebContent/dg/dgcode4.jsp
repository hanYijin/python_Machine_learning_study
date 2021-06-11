<%@page import="sproj.com.org.dg.SPRO_DaeGUManager"%>
<%@page import="sproj.com.org.dg.SPRO_DaeGU"%>

<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>

<%
	SPRO_DaeGUManager sdgm = new SPRO_DaeGUManager();
	String str= sdgm.selectcode4();
	String strname = sdgm.selectcode4name();
	
%>
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
	.rectColor{
		stroke : rgb(255,0,0);
		stroke-width: 1px;
		fill : rgb(0,255,0);	
	}
</style>
</head>
<body>
	<div class="jumbotron">
		<h1>My Study</h1>
		<p>code4</p>
		<svg id="myGraph" width="300" height="2550">
		</svg>
	</div>
</body>
</html>
<script type="text/javascript">
	var dataSet=<%out.print(str);%>
	var dataSets=<%=strname%>
	for(i=0; i<dataSet.length; i++){
		d3.select("#myGraph")
			.append("rect")
			.attr("class","rectColor")
			.attr("x",0)
			.attr("y",(i+1)*25)
			.attr("width",dataSet[i])
			.attr("height",20)
			
		d3.select("#myGraph")
			.append("text")
			.text(dataSets[i])
			.attr("x",dataSet[i]+100)
			.attr("y",(i+1)*25+15)
			.attr("font-family","sans-serif")
			.attr("font-size","11px")
			.attr("fill","hotpink")
			.attr("text-anchor","middle")
	}
	
</script>