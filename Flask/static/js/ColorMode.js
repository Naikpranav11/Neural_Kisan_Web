

const ColorModeIcon=document.getElementById('ColorMode');

function ColorMode(){
    if(ColorModeIcon.textContent=='dark_mode'){
      ColorModeIcon.textContent='light_mode'
        document.body.classList.add('dark')  
    }else{
        ColorModeIcon.textContent='dark_mode'
        document.body.classList.remove('dark')  
    }
    
}

ColorMode();
ColorMode();

