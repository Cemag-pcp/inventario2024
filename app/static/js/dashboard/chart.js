async function loadChartData() {
    try {
        const response = await fetch('/api/dashboard'); // Chama a rota Flask
        const data = await response.json(); // Converte a resposta para JSON
        
        // Cria uma coluna para cada almoxarifado
        data.forEach(almoxarifado => {
            const colDiv = document.createElement('div');
            colDiv.classList.add('col-sm-6');
            colDiv.classList.add('mb-4');

            // Adiciona o título para cada almoxarifado
            const title = document.createElement('p');
            title.classList.add('fw-medium');
            title.style.color = '#6e6e77';
            title.textContent = `Almoxarifado: ${almoxarifado.almoxarifado}`;
            colDiv.appendChild(title);

            // Cria o contêiner para o gráfico
            const chartContainer = document.createElement('div');
            chartContainer.style.width = '100%';
            chartContainer.style.maxWidth = '650px';
            chartContainer.style.margin = 'auto';
            colDiv.appendChild(chartContainer);

            // Cria o canvas para o gráfico
            const canvas = document.createElement('canvas');
            chartContainer.appendChild(canvas);

            // Configuração dos dados do gráfico
            const chartData = {
                labels: [`Não contadas (${almoxarifado.nao_contadas}%)`, `Contadas (${almoxarifado.contadas}%)`],
                datasets: [{
                    data: [almoxarifado.nao_contadas, almoxarifado.contadas],
                    backgroundColor: ['#FF6384', 'rgb(75, 192, 192)'],
                }]
            };

            // Configuração do gráfico de doughnut
            const ctx = canvas.getContext('2d');
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

            // Cria o gráfico de doughnut
            new Chart(ctx, config);

            // Adiciona a coluna com o gráfico na página
            document.querySelector('.row').appendChild(colDiv);
        });

    } catch (error) {
        console.error("Erro ao carregar os dados do gráfico:", error);
    }
}

// Chama a função para carregar e renderizar os dados
loadChartData();
