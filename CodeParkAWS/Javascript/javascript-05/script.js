let h1 = document.getElementById('titulo');
h1.innerText = "Titulo JavaScript"

let ul = document.querySelector('ul');
ul.innerHTML = `
<li>item 01</li>
<li>item 02</li>
<li>item 03</li>
`

let proz = document.querySelector('a');
proz.innerText = 'Link Proz'

let ol = document.getElementById('lista-ordenada');
ol.innerHTML = `
<li><a href="https://www.youtube.com.br" target=_blank>Link Um</a></li>
<li><a href="https://www.google.com.br" target=_blank>Link Dois</a></li>
<li><a href="https://www.naointendo.com.br" target=_blank>Link Três</a></li>
`