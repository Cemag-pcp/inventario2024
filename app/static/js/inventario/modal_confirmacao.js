document.querySelectorAll('.openConfirmation').forEach(button => {
    button.addEventListener('click', (event) => {
        document.getElementById('confirmarInventario').disabled = false;
        document.getElementById('spinner-button').classList.add('d-none');

        const row = event.target.closest('tr');

        // Campos da tabela 
        const idLocalPeca = row.querySelector('.idLocalPeca').innerText;
        const codigoDescricao = row.querySelector('.codigoDescricaoPeca').innerText;
        const estantePeca = row.querySelector('.estantePeca').innerText;
        const quantidadePeca = row.querySelector('.quantidadePeca').value;

        // Input do modal
        document.getElementById('idLocal').value = idLocalPeca;
        document.getElementById('peca').value = codigoDescricao;
        document.getElementById('estante').value = estantePeca;
        document.getElementById('quantidade').value = quantidadePeca; 
    })
})

document.querySelectorAll('.quantidadePeca').forEach(input => {
    input.addEventListener('input', (event) => {
        const row = event.target.closest('tr');
        const button = row.querySelector('.openConfirmation');

        event.target.value ? button.disabled = false : button.disabled = true;
    })
})