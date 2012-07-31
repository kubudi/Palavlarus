
    $(document).ready(function() {  
  
        $('.button').hover(function(){  
            $(this).css('padding', '5px 15px')  
            .stop()  
            .animate({'paddingLeft'    : '25px',  
                     'paddingRight' : '25px',  
                     'backgroundColor':'rgba(50,0,200,0.8);'},  
                     'fast');  
            },  
        function() {  
            $(this).css('padding', '5px 25px')  
            .stop()  
            .animate({  'paddingLeft'    : '15px',  
                        'paddingRight'      : '15px',  
                        'backgroundColor' :'rgba(0,90,230,0.9);'},  
                        'fast');  
        })
        .mousedown(function() {  
            $(this).stop().animate({'backgroundColor': 'rgba(50,0,200,0.6);'}, 'fast');  
        })
        .mouseup(function() {  
            $(this).stop().animate({'backgroundColor': 'rgba(0,90,230,0.8)'}, 'fast');  
        });  
    });  