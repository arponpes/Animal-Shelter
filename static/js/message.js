$( document ).ready(function() {
    $(".modal").addClass("is-active");  
});

$('.delete').click(function(){
    $('.modal').toggle();
})
