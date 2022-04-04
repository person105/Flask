$(function(){

    var hint_btn = document.querySelector('.hint-btn');
    var count = 1;

    hint_btn.addEventListener("click" , () =>{
        for (let i = 0; i < count; i++) {
            if (count > 3){
                for (let j=1; j<4; j++){
                    document.getElementById('hint-'+j).style.display = 'none';
                }
                count = 1;
            }
            else {
                document.getElementById('hint-'+count).style.display = 'flex';
                count++;
                break;
            }
        }
    });


});