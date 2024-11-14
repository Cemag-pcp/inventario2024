document.getElementById('foraDaListaForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Previne o recarregamento da página

    const buttonAddForaLista = document.getElementById("addForaLista");
    buttonAddForaLista.disabled = true;
    document.querySelector(".spinner-button-fora-lista").classList.remove('d-none');

    const form = document.getElementById('foraDaListaForm');
    const localNome = document.getElementById("localNome").value;
    const codigoPecaForaLista = document.getElementById("codigoPecaForaLista").value;
    const descricaoPecaForaLista = document.getElementById("descricaoPecaForaLista").value;
    const estantePecaForaLista = document.getElementById("estantePecaForaLista").value;
    const quantidadePecaForaLista = document.getElementById("quantidadePecaForaLista").value;

    try {
        const response = await fetch("/api/fora-da-lista", {
            method:"POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                localNome:localNome,
                codigoPecaForaLista:codigoPecaForaLista,
                descricaoPecaForaLista:descricaoPecaForaLista,
                estantePecaForaLista:estantePecaForaLista,
                quantidadePecaForaLista:quantidadePecaForaLista
            }),
        });

        const json = await response.json();

        if (response.ok) {
            Swal.fire({
                title: `${json.message}!`,
                icon: "success",
                showConfirmButton: false,
                allowOutsideClick: false,
                timer: 2000
            });

        } else {

            let timerInterval;
            const seconds = 5;  // Definindo o tempo em segundos
            const timerInMilliseconds = seconds * 1000;  // Convertendo para milissegundos

            Swal.fire({
                title: `${json.message}!`,
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
        const seconds = 5;  // Definindo o tempo em segundos
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

        form.querySelectorAll("input").forEach(input => {
            if (input.id !== "localNome") { // Condição para não limpar o campo localNome
                input.value = "";
            }
        });
        form.querySelectorAll("select").forEach(select => select.selectedIndex = 0); // Reseta o select para o primeiro índice

        buttonAddForaLista.disabled = false;
        document.querySelector(".spinner-button-fora-lista").classList.add('d-none');
        const modalElement = document.getElementById('modalPecaForaDaLista');
        const modalInstance = bootstrap.Modal.getInstance(modalElement); 
        modalInstance.hide();
    }
})