document.getElementById("downloadExcel").addEventListener("click", function () {
    // URL da API com o parâmetro para exportar em Excel
    const url = "/api/comparar-quantidade?export=excel";

    // Criação de um link temporário para iniciar o download
    const link = document.createElement("a");
    link.href = url;
    link.download = "comparacoes.xlsx"; // Nome sugerido para o arquivo
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
});