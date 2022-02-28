jQuery.validator.addMethod("noSpace", function(value, element) { 
    return value == '' || value.trim().length != 0;  
}, "Fields cannot be empty.");

// jQuery.validator.addMethod("customEmail", function(value, element) { 
//   return this.optional( element ) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test( value ); 
// }, "Please enter valid email address!");

$.validator.addMethod( "alphanumeric", function( value, element ) {
return this.optional( element ) || /^\w+$/i.test( value );
}, "Only letter, numbers, and underscores are allowed." );


$(function(){
    
    var $loginForm = $('#login');
    if($loginForm.length){
    $loginForm.validate({
        rules:{
            //username is the name of the textbox
            user_name: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                // alphanumeric: true
            },
            password: {
                required: true
            },
            
        },
        messages:{
            user_name: {
                //error message for the required field
                required: '\nPlease enter username!'
            },
            
            password: {
                required: '\nPlease enter password!'
            },
            
        },
        
    });
    }

    var $signUpForm = $('#signup');
    if($signUpForm.length){
    $signUpForm.validate({
        rules:{
            //username is the name of the textbox
            user_name: {
                required: true,
                //alphanumeric is the custom method, we defined in the above
                // alphanumeric: true
            },
            password: {
                required: true
            },
            
        },
        messages:{
            user_name: {
                //error message for the required field
                required: '\nPlease enter username!'
            },
            
            password: {
                required: '\nPlease enter password!'
            },
            
        },
        
    });
    }

    // var hideError = function () {
    //     $(".error").hide();
    // };

    // $loginForm.submit(function () {
    //     setTimeout(hideError, 5000);
    // });

    // $signUpForm.submit(function () {
    //     setTimeout(hideError, 5000);
    // });
})


