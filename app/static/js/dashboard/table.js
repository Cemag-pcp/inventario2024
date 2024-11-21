async function carregarDados() {
    const response = await fetch('/api/comparar-quantidade');
    const data = await response.json();

    // Inicializa o DataTables se ainda não foi inicializado
    if (!$.fn.DataTable.isDataTable('#tabela-pecas')) {
        $('#tabela-pecas').DataTable({
            data: data, // Passa os dados diretamente para o DataTables
            columns: [
                { data: 'almoxarifado' },
                { data: 'local' },
                { data: 'codigo' },
                { data: 'descricao' },
                { 
                    data: 'peca_fora_lista',
                    render: function (data) {
                        return data === false ? 'Não' : 'Sim';
                    } 
                },
                {
                    data: 'quantidade_sistema',
                    render: function (data) {
                        return data !== null ? data : 'Não registrada';
                    }
                },
                {
                    data: 'quantidade_real',
                    render: function (data) {
                        return data !== null ? data : 'Não registrada';
                    }
                },
                {
                    data: 'diferenca',
                    render: function (data) {
                        return data !== null ? data : 'N/A';
                    }
                }
            ],
            language: {
                url: "https://cdn.datatables.net/plug-ins/1.13.6/i18n/pt-BR.json"
            },
            pageLength: 10,
            lengthChange: false,
            order: [[6, 'desc']] // Ordena pela coluna "Diferença"
        });
    } else {
        // Atualiza os dados se o DataTables já estiver inicializado
        const table = $('#tabela-pecas').DataTable();
        table.clear(); // Limpa os dados existentes
        table.rows.add(data); // Adiciona os novos dados
        table.draw(); // Redesenha a tabela
    }
}

// Chama a função para carregar os dados
carregarDados();
