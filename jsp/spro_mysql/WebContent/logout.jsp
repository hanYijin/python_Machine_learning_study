<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%
	//세션 삭제
	session.invalidate();
	//jsp 내장 객체 3가지
	/*
		request: getParameter() 주소의 파라메타 가져오기
		response: sendRedirect() 주소로 이동하기
		session
			setAttribute("이름","값") 세션이름 값 지어
			getAttribute("이름") 세션 이름 가져오기
			invalidate() 세션 내용 삭제
	*/
	//index.jsp로 이동
	response.sendRedirect("Index.jsp");
%>