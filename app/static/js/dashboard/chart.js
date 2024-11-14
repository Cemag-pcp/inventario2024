// Função para carregar os dados da API e renderizar o gráfico
async function loadChartData() {
    try {
        const response = await fetch('/api/dashboard'); // Chama a rota Flask
        const data = await response.json(); // Converte a resposta para JSON
        
        // Configura os dados do gráfico
        const chartData = {
            labels: [`Não contadas (${data.nao_contadas}%)`, `Contadas (${data.contadas}%)`],
            datasets: [{
                data: [data.nao_contadas, data.contadas],
                backgroundColor: ['#FF6384', 'rgb(75, 192, 192)'],
            }]
        };

        console.log(chartData)

        // Configuração do gráfico de pizza
        const config = {
            type: 'doughnut',
            data: chartData,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                    }
                }
            }
        };

        const ctx = document.getElementById('quantidadeChart').getContext('2d');
        new Chart(ctx, config);

    } catch (error) {
        console.error("Erro ao carregar os dados do gráfico:", error);
    }
}

// Chama a função para carregar e renderizar os dados
loadChartData();