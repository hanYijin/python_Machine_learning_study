<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%
	/*
	파라메타 전송방법
	1. form 태그로 감싸서 보내는 방식
	2. 주소에 parameterProc.jsp?a=10&b=20
		특징.. 다음 페이지에서 변수로 작동
	
	- 세션으로 전송방법
		특징: 브라우저가 닫기기 전까지 변수로 작동
		sesion 객체를 사용
		setAttribute("이름","값") // 설정함수
		getAttribute("이름") //가져올때 사용하는 함수
		
		세션 값을 지우기 session.invalidate() // 세션에 내용 삭제
	*/
%>
<!-- form 태그로 감싸서 파라메터 보내기 -->
<form action="parameterProc.jsp">
	a=<input type="text" name="a"/>
	b=<input type="text" name="b"/> 
	<input type="submit" value="확인"/>
</form>
<!-- 주소로 파라메터 보내기 (비밀번호 암호화가 되지 않는다)-->
<a href="parameterProc.jsp?a=">a값 보내기 </a>
</body>
</html>