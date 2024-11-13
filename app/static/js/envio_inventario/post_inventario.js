document.getElementById('confirmarInventario').addEventListener('click', async function() {
    this.disabled = true;
    // Input do modal
    const idLocalValue = document.getElementById('idLocal').value;
    const pecaValue = document.getElementById('peca').value;
    const estanteValue = document.getElementById('estante').value;
    const quantidadeValue = document.getElementById('quantidade').value;

    try {
        const response = await fetch('/api/inventario', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: idLocalValue,
                peca: pecaValue,
                estante: estanteValue,
                quantidade: quantidadeValue
            })
        });

        // Verifica a resposta do servidor
        if (response.ok) {
            Swal.fire({
                title: "Dados enviados com sucesso!",
                icon: "success",
                showConfirmButton: false,
                allowOutsideClick: false,
                timer: 2000
            });

            // Atualiza a tabela após a resposta
            const tabelaPecas = document.getElementById('tabelaPecas');
            const row = [...tabelaPecas.rows].find(row => {
                return row.querySelector('.idLocalPeca').textContent === idLocalValue &&
                    row.querySelector('.codigoDescricaoPeca').textContent.includes(pecaValue);
            });

            if (row) {
                // Atualiza o valor da quantidade na célula
                const quantidadeCell = row.querySelector('.rowQuantidade');
                quantidadeCell.innerHTML = quantidadeValue; // Adiciona o valor de quantidade

                // Remove o input da célula
                const input = quantidadeCell.querySelector('input');
                if (input) {
                    input.remove(); // Remove o input de quantidade
                }
                const rowButton = row.querySelector('.rowButton');
                rowButton.innerHTML = '<i class="fa fa-check" style="font-size: 20px; color: #a5dc86;"></i>'; // Ícone de check

                const buttonCell = row.querySelector('td button');
                if (buttonCell) {
                    buttonCell.remove();
                }
            }

            // Remover a linha da tabela após a resposta bem-sucedida
            // const linha = document.querySelector(`.idLocalPeca[data-id="${idLocalValue}"]`).closest('tr');
            // if (linha) {
            //     linha.remove();
            // }
        } else {
            let timerInterval;
            const seconds = 4;  // Definindo o tempo em segundos
            const timerInMilliseconds = seconds * 1000;  // Convertendo para milissegundos

            Swal.fire({
                title: "Erro ao enviar os dados!",
                icon: "error",
                html: `Página vai carregar sozinha em <b>${seconds}</b> segundos`,
                timer: timerInMilliseconds,
                timerProgressBar: true,
                allowOutsideClick: false,
                didOpen: () => {
                    Swal.showLoading();
                    const timer = Swal.getPopup().querySelector("b");
                    timerInterval = setInterval(() => {
                        timer.textContent = `${Math.ceil(Swal.getTimerLeft() / 1000)}`;  // Mostra o tempo restante em segundos
                    }, 100);  // Atualiza o tempo a cada 100ms
                },
                willClose: () => {
                    clearInterval(timerInterval);
                }
            }).then((result) => {
                // Trata o fechamento do modal
                if (result.dismiss === Swal.DismissReason.timer) {
                    location.reload()
                }
            });
        }
    } catch (error) {
        let timerInterval;
        const seconds = 4;  // Definindo o tempo em segundos
        const timerInMilliseconds = seconds * 1000;  // Convertendo para milissegundos
        console.error('Erro na requisição:', error);
        Swal.fire({
            title: "Erro ao enviar os dados! - Catch",
            icon: "error",
            html: `Página vai carregar sozinha em <b>${seconds}</b> segundos`,
            timer: timerInMilliseconds,
            timerProgressBar: true,
            allowOutsideClick: false,
            didOpen: () => {
                Swal.showLoading();
                const timer = Swal.getPopup().querySelector("b");
                timerInterval = setInterval(() => {
                    timer.textContent = `${Math.ceil(Swal.getTimerLeft() / 1000)}`;  // Mostra o tempo restante em segundos
                }, 100);  // Atualiza o tempo a cada 100ms
            },
            willClose: () => {
                clearInterval(timerInterval);
            }
        }).then((result) => {
            // Trata o fechamento do modal
            if (result.dismiss === Swal.DismissReason.timer) {
                location.reload()
            }
        });
    } finally {
        const modalElement = document.getElementById('modalConfirmarQuantidade');
        const modalInstance = bootstrap.Modal.getInstance(modalElement); 
        modalInstance.hide();
    }
});
