
 $(document).ready(function () {
    $('input').addClass('input100');
    $("#id_password2").attr('placeholder', "Confirm Password")
    $("#id_password1").attr('placeholder', 'Password')
    $("#id_email").attr('placeholder', 'Email')
    $("#id_new_password1").attr('placeholder', 'New Password')
    $("#id_new_password2").attr('placeholder', 'Confirm Password')
    
    $('.input100').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })

    var input = $('.validate-input .input100');

    $('#login-btn').on('click',function(event){
        event.preventDefault()
        var check = true;
        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }
        if(check) {
            var username = $("#username").val()
            var password = $("#password").val()
            $("#login-btn").text("Wait..")
            var csrf = $("#csrf").val()
            $.ajax({
                url: "/accounts/login/",
                type: "POST",
                data: {
                    csrfmiddlewaretoken: csrf,
                    username: username,
                    password: password
                },
                success: function(response) {
                    if(response.success) {
                        $("#login-btn").text("Success")
                        window.location.href = "/blogs/";
                    } else {
                        $("#message").text(response.message)
                        $("#login-btn").text("Login")
                    }
                },
                failure: function() {
                }
            })
        } else{
            return check;
        }
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).removeClass('alert-validate');
    }


    $('#signup-btn').on('click',function(event){
        event.preventDefault()
        var formsub = $('#signupform').serializeArray();
        formsub.push({
            csrfmiddlewaretoken: '{{ csrf_token }}'
        })
        $.ajax({
            url: "/accounts/signup/",
            type: "POST",
            data: formsub,
            dataType: "json",
            success: function(response) {
                if(response.success) {
                    window.location.replace('/accounts/signup/success/');
                } else {
                    errors = JSON.parse(response.errors)
                    if(errors.hasOwnProperty('username')){
                        $(".m-b-0").attr('data-validate', errors["username"][0]["message"])
                        $(".m-b-0").addClass('alert-validate');
                    }
                    if(errors.hasOwnProperty('first_name')){
                        $(".m-b-01").attr('data-validate', errors["first_name"][0]["message"])
                        $(".m-b-01").addClass('alert-validate');
                    }
                    if(errors.hasOwnProperty('last_name')){
                        $(".m-b-1").attr('data-validate', errors["last_name"][0]["message"])
                        $(".m-b-1").addClass('alert-validate');
                    }
                    if(errors.hasOwnProperty('email')){
                        $(".m-b-2").attr('data-validate', errors["email"][0]["message"])
                        $(".m-b-2").addClass('alert-validate');
                    }
                    if(errors.hasOwnProperty('password1')){
                        $(".m-b-3").attr('data-validate', errors["password1"][0]["message"])
                        $(".m-b-3").addClass('alert-validate');
                    }
                    if(errors.hasOwnProperty('password2')){
                        $(".m-b-4").attr('data-validate', errors["password2"][0]["message"])
                        $(".m-b-4").addClass('alert-validate');
                    }
                }
            },
            failure: function() {
            }
        })
    });
});