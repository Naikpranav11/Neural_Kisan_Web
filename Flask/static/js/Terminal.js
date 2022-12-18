const terminal=document.getElementById('TerminalTextBox')
const CodeLine=document.getElementById('TerminalLine')
function createRecord(){ 
    
    fetch('/output')
    .then((response) => response.json())
    .then((data) => {
        highlight=data['option']
        const line = CodeLine.cloneNode(true) 
      line.textContent=(data['message'])+'\n'
      
      line.className=highlight
      
      terminal.appendChild(line)
  
  });




    
}
setInterval(createRecord,1000)



// Plant: [ 'Tray 029','Row 2','Column 6']
// Sensor Data Updated.....
// API Fetched
// Processing Data [##########] 100%
// Summary: OK
// Command: Do Nothing
// <span class="highlight">$ NextPlant</span>
// Plant: [ 'Tray 029','Row 3','Column 1']
// Sensor Data Updated.....
// API Fetched
// Processing Data [##########] 100%
// Summary: Dry
// Command: Add Water
// <span class="highlight">$ NextPlant</span> 