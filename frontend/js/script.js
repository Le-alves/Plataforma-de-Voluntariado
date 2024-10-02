// script.js

// Função para mostrar campos adicionais com base na seleção do usuário
function mostrarCampoAdicional() {
    const categoria = document.getElementById('categoria').value;
    const campoRoupas = document.getElementById('campoRoupas');
    const campoOutros = document.getElementById('campoOutros');

    // Resetar visibilidade dos campos adicionais
    campoRoupas.classList.add('d-none');
    campoOutros.classList.add('d-none');

    // Mostrar o campo correspondente com base na seleção
    if (categoria === 'roupa') {
        campoRoupas.classList.remove('d-none');
    } else if (categoria === 'outros') {
        campoOutros.classList.remove('d-none');
    }
}

// Adicionar um evento para o select de categoria
document.addEventListener('DOMContentLoaded', () => {
    const selectCategoria = document.getElementById('categoria');
    if (selectCategoria) {
        selectCategoria.addEventListener('change', mostrarCampoAdicional);
    }
});



// ----------------------------- registro_doaçoes---------------------------------
// script.js

// Função para exibir a tabela de doações
function mostrarTabelaDoacoes() {

     // Evita o comportamento padrão de enviar o formulário
     event.preventDefault();

    // Selecionar a tabela de doações e o corpo da tabela
    const tabelaDoacoes = document.getElementById('tabela-doacoes');
    const tabelaCorpo = document.getElementById('tabela-corpo');

    // Simulação de dados fictícios de doação
    const doacoes = [
        { data: '01/09/2024', tipo: 'Camiseta', quantidade: '5', pontos: '10' },
        { data: '15/09/2024', tipo: 'Arroz', quantidade: '2 kg', pontos: '20' }
    ];

    // Limpar o corpo da tabela antes de preencher
    tabelaCorpo.innerHTML = '';

    // Preencher a tabela com os dados fictícios
    doacoes.forEach(doacao => {
        const linha = document.createElement('tr');
        linha.innerHTML = `
            <td>${doacao.data}</td>
            <td>${doacao.tipo}</td>
            <td>${doacao.quantidade}</td>
            <td>${doacao.pontos}</td>
        `;
        tabelaCorpo.appendChild(linha);
    });

    // Remover a classe 'd-none' para exibir a tabela
    tabelaDoacoes.classList.remove('d-none');
}


// Adicionar evento ao botão "Pesquisar"
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('pesquisar-btn').addEventListener('click', mostrarTabelaDoacoes);
});

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('pesquisar-btn').addEventListener('click', () => {
        // Exibir o Cartão de Classe com Animação
        const cardClasse = document.getElementById('card-classe');
        cardClasse.classList.add('show');

        // Exibir a Tabela de Doações após um pequeno delay
        setTimeout(() => {
            const tabelaDoacoes = document.getElementById('tabela-doacoes');
            tabelaDoacoes.classList.add('show');
        }, 1000); // Atraso de 1 segundo para exibir a tabela
    });
});


//----------------------------Cards--------------------------

