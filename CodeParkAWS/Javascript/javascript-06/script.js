let titulo = document.createElement("h1");
titulo.id = "titulo";
titulo.innerText = "Titulo do site";

let body = document.querySelector('body');
body.appendChild(titulo);

let preco = 0;
for (let i = 1; i < 5; i++){
    let produto = document.createElement("section");
    preco += 10;
    produto.innerHTML =
    `<h2>Nome do produto ${i}</h2>
    <p>Descrição do produto ${i}</p>
    <p>Preço do produto R$${preco}</p>`
    body.appendChild(produto);
}