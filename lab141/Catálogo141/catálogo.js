// Seleciona todos os botões de "Comprar"
const botaoComprar = document.querySelectorAll(".comprar");

// Ao clicar no botão, armazena os dados no Local Storage
botaoComprar.forEach((botao) => {
  botao.addEventListener("click", () => {
    const nome = botao.getAttribute("data-nome");
    const preco = botao.getAttribute("data-preco");

    // Recupera itens armazenados anteriormente ou cria uma nova lista
    let itens = JSON.parse(localStorage.getItem("itensCompra")) || [];
    itens.push({ nome, preco });

    // Salva os dados no Local Storage
    localStorage.setItem("itensCompra", JSON.stringify(itens));
    alert(`O item "${nome}" foi adicionado à planilha!`);
  });
});
