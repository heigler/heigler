$(function(){
   var en_button = $('.flags a.en');
   var br_button = $('.flags a.br');
   
   var change_lang = function(lang_code){       
        $.ajax({
            url: '/i18n/setlang/',
            type: 'POST', 
            data: {language: lang_code},
				
            success: function(result){
                //window.location.reload();
            }
        });       
   }   
   
   en_button.click(function(evt){
        evt.preventDefault();
        change_lang('en-us');
    });
    
   br_button.click(function(evt){
        evt.preventDefault();
        change_lang('pt_BR');
    });
   
       
});
