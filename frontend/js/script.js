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
    } 
});


//---------Index----------




// ----------------------------- registro_usuario---------------------------------
document.addEventListener('DOMContentLoaded', function () {
    // Capturar o botão de pesquisa
    const botaoPesquisar = document.getElementById('pesquisar-btn');

    if (botaoPesquisar) {
        // Definir o evento de clique no botão
        botaoPesquisar.addEventListener('click', function () {
            const numeroIdentificacao = document.getElementById('matricula').value;

            if (!numeroIdentificacao) {
                alert("Por favor, digite um número de matrícula válido!");
                return;
            }

            // Chamar a função para buscar e exibir as doações na tabela
            mostrarTabelaDoacoes(numeroIdentificacao);
        });
    } 
});

// Função para buscar e exibir as doações
function mostrarTabelaDoacoes(numeroIdentificacao) {
    // Fazer a requisição para buscar as doações do usuário
    fetch(`http://127.0.0.1:5000/consultar_doacoes/${numeroIdentificacao}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao buscar as doações do usuário.');
        }
        return response.json();
    })
    .then(data => {
        const tabelaCorpo = document.getElementById('tabela-corpo');
        const tabelaDoacoes = document.getElementById('tabela-doacoes');

        // Limpar a tabela antes de preenchê-la
        tabelaCorpo.innerHTML = '';

        // Verificar se existem doações no retorno
        if (!data.doacoes || data.doacoes.length === 0) {
            alert("Nenhuma doação encontrada para este usuário.");
            tabelaDoacoes.classList.add('d-none'); // Esconder a tabela se não houver doações
            return;
        }

        // Preencher a tabela com os dados recebidos
        data.doacoes.forEach(doacao => {
            const linha = document.createElement('tr');
            linha.innerHTML = `
                <td>${doacao.data_doacao}</td>
                <td>${doacao.categoria}</td>
                <td>${doacao.quantidade}</td>
                <td>${doacao.pontos}</td>
            `;
            tabelaCorpo.appendChild(linha);
        });

        // Exibir a tabela após preenchê-la
        tabelaDoacoes.classList.remove('d-none');
    })
    .catch(error => {
        console.error("Erro ao buscar as doações:", error);
        alert("Ocorreu um erro ao buscar as doações. Verifique o console.");
    });
}

document.addEventListener("DOMContentLoaded", function() {
    // Função para atualizar a barra de progresso com o valor total de doações
    function atualizarProgresso() {
        // Faz uma requisição para o endpoint que retorna o total de doações no backend Flask
        fetch('http://127.0.0.1:5000/total_doacoes')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na requisição: ' + response.status);
                }
                return response.json();
            }) // Converte a resposta para JSON
            .then(data => {
                // Pega o valor total de doações retornado pela API
                let totalDoacoes = data.total_doacoes;

                // Defina uma meta de doações (por exemplo, 100 itens doados)
                let metaDoacoes = 25; // Ajuste a meta conforme necessário

                // Calcula a porcentagem com base na meta
                let progresso = (totalDoacoes / metaDoacoes) * 100;

                // Seleciona a barra de progresso e atualiza os valores
                let progressBar = document.querySelector('.progress-bar');
                progressBar.setAttribute('aria-valuenow', progresso);
                progressBar.style.width = `${progresso}%`;
            })
            .catch(error => {
                console.error('Erro ao buscar o total de doações:', error);
            });
    }

    // Chama a função para atualizar a barra de progresso ao carregar a página
    atualizarProgresso();
});
