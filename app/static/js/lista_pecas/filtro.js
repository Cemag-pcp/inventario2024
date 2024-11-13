// Função que aplica ambos os filtros
function aplicarFiltros() {
    const filtroPeca = document.getElementById('filtroPeca').value.toLowerCase();
    const filtroEstante = document.getElementById('filtroEstante').value.toLowerCase();
    const linhas = document.querySelectorAll('#tabelaPecas tr');

    linhas.forEach(linha => {
        const peca = linha.cells[1].textContent.toLowerCase();
        const estante = linha.cells[2].textContent.toLowerCase();
        
        // Exibe a linha apenas se ambos os filtros forem atendidos
        const correspondePeca = peca.includes(filtroPeca);
        const correspondeEstante = estante.includes(filtroEstante);

        if (correspondePeca && correspondeEstante) {
            linha.style.display = '';
        } else {
            linha.style.display = 'none';
        }
    });
}

// Eventos para chamar a função de filtro ao modificar um dos campos
document.getElementById('filtroPeca').addEventListener('keyup', aplicarFiltros);
document.getElementById('filtroEstante').addEventListener('keyup', aplicarFiltros);