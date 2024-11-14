document.getElementById("openModalButton").addEventListener("click", function() {
    // Seleciona o formulário
    const form = document.getElementById("foraDaListaForm");

    // Define todos os campos de input e select como vazios
    form.querySelectorAll("input").forEach(input => {
        if (input.id !== "localNome") { // Condição para não limpar o campo localNome
            input.value = "";
        }
    });
    form.querySelectorAll("select").forEach(select => select.selectedIndex = 0); // Reseta o select para o primeiro índice
});