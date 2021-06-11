<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Bootstrap Example</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script	src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="/sproj/css/mycss.css"/>
<script type="text/javascript">
//jQuery 문법
	$('document').ready(function(){
		//css 
		/* 1) #id-> id 선택자
			2) .class -> class 선택자
			3) tage 명 -> tage 선택자
			$('#id명')
			$('.class명')
			$('h1')
			<p><h1>제목</h1><strong>진하게</strong><h2>h2h2</h2></p>
			p > h1 {}	부모 태그 > 자식 태그 	
			p > h2 {}
			$('p > h2').attr('class','class명')
			*/
		$('button').on('click',function(obj){
			$('button').attr('class','btn btn-primary w80'); 
			//해당 버튼만 빨간색으로 표시
			$(this).attr('class','btn btn-danger w80');
			//this: click한 button
			//class와 tag는 중복이 가능, id는 오직 하나
		
			//alert('$(this).html()= '+$(this).html())
			//alert('$(this).text()= '+$(this).text())
//text() 태그사이에 글자만 가져오기
//html() 태그사이에 html 태그 포함해서 글자 가져오기
//val() input 태그에 있는 value 값 가져오기
		});
		$('#confirm').on('click',function(){
			var seat='';
			
			$('button').each(function(index,obj){

				console.log("$(this).attr('class')= "+$(this).attr('class'));
				if($(this).attr('class')== 'btn btn-danger w80'){
//					console.log("$(this).attr('class')= "+$(this).attr('class'));
//					console.log("$(this).text()= "+$(this).text());
					seat= $(this).text();
				}
			})
			location.href="seatsave.jsp?seat="+seat;
		})
	})
</script>
</head>
<body>
	<div class="jumbotron">
		<h1>My Study</h1>
		<p>Select your seat!</p>
		<div class="row text-center">
			<div class="col-sm-2"><button class="btn btn-primary w80"> 1 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 2 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 3 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 4 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 5 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 6 </button></div>
		</div>
		<div class="row text-center mt-2">
			<div class="col-sm-2"><button class="btn btn-primary w80"> 7 </button></div>
			<div class="col-sm-8"></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 8 </button></div>
		</div>
		<div class="row text-center mt-2">
			<div class="col-sm-2"><button class="btn btn-primary w80"> 9 </button></div>
			<div class="col-sm-1"></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 10 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 11 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 12 </button></div>
			<div class="col-sm-1"></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 13 </button></div>
		</div>
		<div class="row text-center mt-2">
			<div class="col-sm-2"><button class="btn btn-primary w80"> 14 </button></div>
			<div class="col-sm-1"></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 15 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 16 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 17 </button></div>
			<div class="col-sm-1"></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 18 </button></div>
		</div>
		<div class="row text-center mt-2">
			<div class="col-sm-2"><button class="btn btn-primary w80"> 19 </button></div>
			<div class="col-sm-8"></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 20 </button></div>
			<div class="col-sm-1"></div>
		</div>
		<div class="row text-center mt-2">
			<div class="col-sm-2"><button class="btn btn-primary w80"> 21 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 22 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 23 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 24 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 25 </button></div>
			<div class="col-sm-2"><button class="btn btn-primary w80"> 26 </button></div>
		</div>
		<div class="row text-center mt-2">
			<div class="col-sm-2"></div>
			<div class="col-sm-2"></div>
			<div class="col-sm-2">
				<input type="button" id="cencel" class="btn btn-warning w80" value="cencel"/>
			</div>
			<div class="col-sm-2">
				<input type="button" id="confirm" class="btn btn-warning w80" value="confirm"/> 
			</div>
			<div class="col-sm-2"></div>
			<div class="col-sm-2"></div>
		</div>
		
	</div>
</body>
</html>