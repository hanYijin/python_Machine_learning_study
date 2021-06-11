function doGra(dataSet){
//	alert(dataset);
	d3.select("#myGraph")				    // SVG 요소 지정
	.selectAll("rect")					// SVG로 사각형을 표시할 요소를 지정
	.data(dataSet)						// 데이터 설정
	.enter()							// 데이터 수에 따라 rect 요소 생성
	.append("rect")						// SVG 사각형 생성
	.attr("x", 0)							// 가로형 막대그래프이므로 X좌표를 0으로 함
	.attr("y", function(d,i){			// Y 좌표를 배열의 순서에 따라 계산
		return i * 25;					// 막대그래프의 높이를 25px 단위로 계산
    })
    .attr("height", "20px")			    // 막대그래프의 높이를 20px로 지정
	.attr("width", "0px")
    .transition()
    .delay(function(d,i){
        return i*500;
    })
    .duration(function(d,i){
        return 2500;
    })
    .attr("width", function(d,i){
        return d+"px";
    })
    
    var xScale = d3.scaleLinear()  // 선형 스케일 설정
        .domain([0, 500])   // 원래 데이터 범위
        .range([0, 500])  // 실제 출력 크기
    // 눈금을 설정하고 표시
    d3.select("#myGraph")
	    .append("g")
	    .attr("transform", "translate(0,250)")      // This controls the vertical position of the Axis
	    .call(d3.axisBottom(xScale));
}
