

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        validateDate: function(inputDate) {
            var dateformat = /^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$/;
              if(inputDate.match(dateformat)){
                    document.getElementById("surname_ac").className= "is-valid form-control"
                }
        }
    }
});

function isDate(validateInput) {
    var regex = /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))$/g;
    var txt = document.getElementById("dob_ac").value;
    var p = document.setElementById("response");
    var test = (regex.test(txt)) ?
        "yes" : "no";
    if (test=="yes"){
            document.getElementById("dob_ac").className = "is-valid form-control";
            }
    if (test=="no"){
            document.getElementById("dob_ac").className = "is-invalid form-control";
    }
}



 if (var_output=='valid'){
                years = Math.floor(moment(new Date()).diff(moment(var_txt,"DD/MM/YYYY"),'years',true)))
                console.log(years)
                document.getElementById("dob_ac").className = "is-valid form-control";
        }

var_output = 'set';
        if (inputValue != null){
            var_test = (regex_date.test(var_txt)) ?
                         var_output='valid' : var_output='not_valid;
        }
    }
