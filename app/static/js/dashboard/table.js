async function carregarDados() {
    const response = await fetch('/api/comparar-quantidade');
    const data = await response.json();

    // Inicializa o DataTables se ainda não foi inicializado
    if (!$.fn.DataTable.isDataTable('#tabela-pecas')) {
        const table = $('#tabela-pecas').DataTable({
            data: data,
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
            order: [[6, 'desc']]
        });

        // Adicionar filtro personalizado para Almoxarifado
        $('#filtro-almoxarifado').on('keyup', function () {
            table.column(0).search(this.value).draw(); // Filtra na coluna de índice 0 (Almoxarifado)
        });
    } else {
        const table = $('#tabela-pecas').DataTable();
        table.clear();
        table.rows.add(data);
        table.draw();
    }
}

carregarDados();