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


/* Adicionar evento ao botão "Pesquisar"
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
});*/
// Função para verificar se o usuário existe no banco de dados
function verificarUsuario(numeroIdentificacao) {
    return fetch(`http://127.0.0.1:5000/consultar_usuario/${numeroIdentificacao}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();  // Se o usuário existir, retorna os dados do usuário
        }
        throw new Error('Usuário não encontrado');
    })
    .then(data => {
        console.log("Usuário encontrado: ", data);
        return true;  // Usuário existe
    })
    .catch(error => {
        console.warn('Usuário não encontrado:', error);
        return false;  // Usuário não existe
    });
}

// Função para registrar um novo usuário no backend
function registrar_usuario(numeroIdentificacao, tipoUsuario) {
    const dadosUsuario = {
        numero_identificacao: numeroIdentificacao,
        tipo_usuario: tipoUsuario  // Definir um valor padrão (1 para Estudante)
    };

    return fetch('http://127.0.0.1:5000/registrar_usuario', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dadosUsuario)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao registrar o usuário: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message);  // Mensagem de sucesso ao registrar o usuário
        return true;  // Usuário registrado com sucesso
    })
    .catch(error => {
        console.error('Erro ao registrar o usuário:', error);
        return false;  // Falha ao registrar o usuário
    });
}

// Função para registrar a doação no backend
function registrar_doacao(numeroIdentificacao, categoria, item, quantidade) {
    const dadosDoacao = {
        numero_identificacao: numeroIdentificacao,
        categoria: categoria,
        item: item,
        quantidade: quantidade
    };

    return fetch('http://127.0.0.1:5000/registrar_doacao', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dadosDoacao)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na requisição: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        alert(data.message);  // Mostrar mensagem de sucesso ou erro do backend
    })
    .catch(error => {
        console.error('Erro ao registrar a doação:', error);
        alert("Ocorreu um erro ao registrar a doação. Verifique o console.");
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const botaoEnviar = document.querySelector('button[type="submit"]');

    if (botaoEnviar) {
        botaoEnviar.addEventListener('click', function (event) {
            event.preventDefault();

            // Capturar os valores dos campos do formulário
            const numeroIdentificacao = document.getElementById('matricula').value;
            const tipoUsuarioTexto = document.querySelector('input[name="tipoUsuario"]:checked')?.value;
            const categoria = document.getElementById('categoria').value;
            let item = "";
            if (categoria === "roupa") {
                item = document.getElementById('tipoRoupa').value || "Indefinido";
            } else if (categoria === "outros") {
                item = document.getElementById('descricaoOutros').value || "Indefinido";
            } else {
                item = categoria;  // Usar a própria categoria como item para alimentos ou categorias não especificadas
            }
            const quantidadeTexto = document.getElementById('quantidade').value
            const quantidade = parseInt(quantidadeTexto, 10); 


            // Converter o tipo de usuário de texto para número (1 para Estudante, 2 para Funcionário)
            let tipoUsuario;
            if (tipoUsuarioTexto === "estudante") {
                tipoUsuario = 1;
            } else if (tipoUsuarioTexto === "funcionario") {
                tipoUsuario = 2;
            } else {
                alert("Por favor, selecione o tipo de usuário (Estudante ou Funcionário).");
                return;
            }

            if (!numeroIdentificacao || !categoria || item === "Indefinido") {
                alert("Por favor, preencha todos os campos antes de enviar!");
                return;
            }

            // Verificar se o usuário existe antes de registrar a doação
            verificarUsuario(numeroIdentificacao).then(usuarioExiste => {
                if (usuarioExiste) {
                    console.log("Usuário existente. Registrando a doação...");
                    registrar_doacao(numeroIdentificacao, categoria, item, quantidade);  // Registrar doação com o usuário existente
                } else {
                    console.log("Usuário não encontrado. Criando novo usuário...");

                    // Criar o usuário e, após o sucesso, registrar a doação
                    registrar_usuario(numeroIdentificacao, tipoUsuario).then(usuarioRegistrado => {
                        if (usuarioRegistrado) {
                            console.log("Usuário criado com sucesso. Registrando a doação...");
                            registrar_doacao(numeroIdentificacao, categoria, item, quantidade);  // Registrar doação com o novo usuário
                        } else {
                            alert("Erro ao criar o usuário. Não foi possível registrar a doação.");
                        }
                    });
                }
            });
        });
    } else {
        console.error("Botão de envio de doação não encontrado no HTML.");
    }
});
