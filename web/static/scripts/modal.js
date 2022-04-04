$(function(){
    var modal_btns = document.querySelectorAll('.modal-open');
    var opened = false;

    modal_btns.forEach(function(btn){
        btn.onclick = function() {
            if(!opened) {
                var modal = btn.getAttribute('data-modal');
                document.getElementById(modal).style.display ='flex';
                opened = true;
            }
        };
    });

    var close_btns = document.querySelectorAll('.modal-close');

    close_btns.forEach(function(btn){
        btn.onclick = function() {
            if (opened) {
                var modal = btn.closest('.modal-bg').style.display ='none';
                opened = false;
            }
        };
    });

    window.onclick = function(e) {
        if (e.target.className === 'modal-bg'){
        if (opened) {
                e.target.style.display = 'none';
                opened = false;
        }
        }

    };

});