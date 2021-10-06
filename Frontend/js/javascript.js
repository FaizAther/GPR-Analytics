$(document).ready(function(){

    var courses = [];
    var count = 0;
    $('.course ul li').each(function(){
        courses.push($(this));
    });

    console.log(localStorage.getItem("selected_course"));

    if(localStorage.getItem("selected_course") != null){
        var courses2 = [];
        $('.course ul li').each(function(){
            courses2.push($(this));
        });
        courses2[localStorage.getItem("selected_course")].addClass('purple');
    }
    


    $(".save").click(function() {
        alert('Save Successfully!');
    }); 


    // $(".class_schedule button a").click(function(){
    //     localStorage.setItem('button', 'clicked');
    // });

    // if(localStorage.getItem('button') === 'clicked'){
    //     var courses = [];
        // $('.course2 ul li').each(function(){
        //     courses.push($(this));
        // });

    //     // for(let i = 0; i < courses.length; i++){
    //     //     console.log(courses[i] == course);
    //     //     if(courses[i] == course){
    //     //         courses[i].addClass('purple');
    //     //     }
    //     // }
    // }



    $(".course li").click(function(){
        console.log(courses.length);
        var text = $(this).text();
        if(text != "Course List"){
            $(".course_title").text(text);
            $('.purple').removeClass('purple');
            $(this).addClass('purple');
            for(let i = 0; i < courses.length; i++){
                if(courses[i].text() == $(this).text()){
                    localStorage.setItem("selected_course", i);
                    break;
                }
            }
        }
    });



});
