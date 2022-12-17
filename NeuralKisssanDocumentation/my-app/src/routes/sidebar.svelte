
<div>
   <h1>Neural Kissan Docs</h1>

    <ul>
       <li><a href="./Intro.svelte">Intro</a></li>
     
       <li>
        <h4>Hardware</h4> 
         <ul>
             <li><a href="">ESP32</a></li>
             <li><a href="">ESP32 CAM</a></li>
         </ul>
        </li>
  
       <li>
       <h4>Software</h4> 
        <ul>
            <li><a href="">Neural Network</a></li>
            <li><a href="">Random Forrest</a></li>
        </ul>
       </li>
    </ul>
    <h5>Version 0.1</h5>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    div{
        
        border-radius: 0 var(--radius) var(--radius) 0;
        box-shadow: 1rem 0rem 2rem .5rem rgba(7, 7, 7, 0.486);
        font-family: 'Montserrat', sans-serif;
        background: #101010;
        height: 100vh;
        width: 17rem;
        display: grid;
        grid-template-rows: 10% 85% 5%;
    }
    div h1{
        display:flex ;
        align-items: center;
        font-size: 1.2rem;
        text-align: left;
    padding-left: 1rem;
        font-weight: 800;
        color: var(--accent)
    }
    li{
        text-indent: 1.8ch;
    }

    h5{
        color: aliceblue;
        text-indent: 2ch;
    }
 
    H4{
        font-weight: 600;
        color: rgb(255, 255, 255);
    }

</style>