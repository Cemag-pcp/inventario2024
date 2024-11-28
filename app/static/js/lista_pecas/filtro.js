// Função que aplica ambos os filtros
function aplicarFiltros() {
    const filtroPeca = document.getElementById('filtroPeca').value.toLowerCase(); // Pega o valor do select 'filtroPeca'
    const filtroEstante = document.getElementById('filtroEstante').value.toLowerCase(); // Pega o valor do select 'filtroEstante'
    const linhas = document.querySelectorAll('#tabelaPecas tr'); // Pega todas as linhas da tabela

    linhas.forEach(linha => {
        const peca = linha.cells[1].textContent.toLowerCase(); // Obtém a descrição da peça (coluna 2)
        const estante = linha.cells[2].textContent.toLowerCase(); // Obtém a descrição da estante (coluna 3)
        
        // Exibe a linha apenas se ambos os filtros forem atendidos
        const correspondePeca = peca.includes(filtroPeca);
        const correspondeEstante = estante.includes(filtroEstante);

        // Se ambos os filtros corresponderem, a linha será exibida, caso contrário será oculta
        if (correspondePeca && correspondeEstante) {
            linha.style.display = ''; // Exibe a linha
        } else {
            linha.style.display = 'none'; // Oculta a linha
        }
    });
}

// Eventos para chamar a função de filtro ao alterar um dos campos select
document.getElementById('filtroPeca').addEventListener('input', aplicarFiltros); // Para o filtro de peça
document.getElementById('btnFiltrar').addEventListener('click', aplicarFiltros);