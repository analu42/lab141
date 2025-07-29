// Recupera os itens do Local Storage
const itens = JSON.parse(localStorage.getItem("itensCompra")) || [];
const tabela = document.querySelector("#planilha tbody");
const totalElement = document.getElementById("total");

let total = 0;

// Adiciona os itens à tabela
itens.forEach((item) => {
  const linha = document.createElement("tr");

  const colunaNome = document.createElement("td");
  colunaNome.textContent = item.nome;

  const colunaPreco = document.createElement("td");
  colunaPreco.textContent = `R$ ${item.preco}`;

  linha.appendChild(colunaNome);
  linha.appendChild(colunaPreco);
  tabela.appendChild(linha);

  total += parseFloat(item.preco);
});

// Exibe o total
totalElement.textContent = `Total: R$ ${total.toFixed(2)}`;
