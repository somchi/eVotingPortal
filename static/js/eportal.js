function rotate(){
    var current=$("#slide div.current");
    var next = current.next();
    if(next.length==0)
         next=$("#slide div:first");
         current.removeClass("current").addClass("previous");
         next.slideUp().addClass("current").slideDown();
}
$(function(){
    setInterval("rotate()", 2000);
});

/*function rotate(){
	var current=$("#PhotoShow div.current");
	var next= current.next();
	if(next.length==0)
		next=$("#PhotoShow div:first");
		current.removeClass("current").addClass("previous");
		next.slideUp().addClass("current").slideDown();
}*/
$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
});