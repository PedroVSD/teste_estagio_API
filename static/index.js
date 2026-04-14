const API_BASE_URL = "http://127.0.0.1:8000";

const form = document.getElementById("cashbackForm");
const resultadoBox = document.getElementById("resultado-box");
const resultadoValor = document.getElementById("resultado-valor");
const historyBody = document.getElementById("historyBody");

//(R$)
const formatarMoeda = (valor) => {
  return new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL",
  }).format(valor);
};

// Buscar o histórico na API
async function carregarHistorico() {
  try {
    const response = await fetch(`${API_BASE_URL}/historico`);
    if (!response.ok) throw new Error("Erro na rede");

    const data = await response.json();
    renderizarTabela(data);
  } catch (error) {
    console.error("Erro ao carregar histórico:", error);
    historyBody.innerHTML = `<tr><td colspan="3" class="empty-state" style="color: red;">Erro ao conectar com a API. Verifique se o FastAPI está rodando.</td></tr>`;
  }
}

//renderizar os dados na tabela
function renderizarTabela(dados) {
  historyBody.innerHTML = "";

  if (!dados || dados.length === 0) {
    historyBody.innerHTML = `<tr><td colspan="3" class="empty-state">Nenhuma consulta registrada para o seu IP.</td></tr>`;
    return;
  }

  dados.forEach((item) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td><span style="font-weight: ${item.cliente === "VIP" ? "bold" : "normal"}">${item.cliente}</span></td>
            <td>${formatarMoeda(item.valor_compra)}</td>
            <td style="color: var(--success); font-weight: bold;">${formatarMoeda(item.cash_back)}</td>
        `;
    historyBody.appendChild(tr);
  });
}

//submissão do formulário
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const cliente = document.getElementById("cliente").value;
  const valor = parseFloat(document.getElementById("valor").value);

  try {
    // Envia os dados para cálculo e salva no banco
    const response = await fetch(`${API_BASE_URL}/calcular`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        cliente: cliente,
        valor_compra: valor,
      }),
    });

    if (!response.ok) throw new Error("Erro ao calcular");

    const data = await response.json();

    // Exibe o resultado na tela
    resultadoBox.style.display = "block";
    resultadoValor.textContent = formatarMoeda(data.cashback);

    // Atualiza o histórico
    carregarHistorico();
  } catch (error) {
    alert("Erro ao enviar dados para a API. Verifique a conexão.");
    console.error(error);
  }
});

document.addEventListener("DOMContentLoaded", carregarHistorico);
