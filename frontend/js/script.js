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

