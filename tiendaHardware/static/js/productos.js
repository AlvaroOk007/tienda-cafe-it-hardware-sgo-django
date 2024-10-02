/* comportamiento de filtros de busqueda */

const btnAplicarFiltro = document.getElementById('btn-aplicar-filtros')
const btnQuitarFiltro = document.getElementById('btn-quitar-filtro')

btnAplicarFiltro.addEventListener('click', ()=>{
    /* 
        Comportamiento: Cuando el usuario de click en "APLICAR FILTROS" js escuchara el click y mandara una peticion a django para obtener los datos de la bd aplicando los filtros correspondientes
    */
    const categoria = document.getElementById('filtro_categoria').value
    const marca = document.getElementById('filtro_marca').value
    const tieneCatergoria = categoria.value === 'Filtrar por Categoria' ? false : true
    const tieneMarca = marca.value === 'Filtrar por Marca' ? false : true 
    const filtros = {
        categoria:categoria,
        marca:marca,
    }
    if (tieneCatergoria || tieneMarca){
        /*Verificamos que tenga categoria o marca */
        enviarFiltros(filtros)
        btnQuitarFiltro.classList.add('mostrar')
    }
})

btnQuitarFiltro.addEventListener('click',()=>{
    const filtros = {
        categoria:'Filtrar por Categoria',
        marca:'Filtrar por Marca',
    }
    enviarFiltros(filtros)
    btnQuitarFiltro.classList.toggle('mostrar')
})
/* */

const enviarFiltros = async (data) => {
    try {
        const response = await fetch("http://localhost:8000/home/productos/api/aplicarFiltros/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams(data),  // Convierte el objeto a formato de formulario
        });

        if (response.ok) {
            const resultados = await response.json();
            const conteiner_productos = document.getElementById('conteiner-productos')
            conteiner_productos.innerHTML = ``
            resultados.forEach(resultado=>{
                conteiner_productos.innerHTML += `
                            <article class="conteiner_card">
                                <div class="header_card">
                                    <img src="/media/${resultado.imagen}" alt="${resultado .nombre}">
                                </div>
                                <div class="footer_card">
                                    <h2 class="card_nombre">${resultado.nombre}</h2>
                                    <h2 class="card_precio">${resultado.precio}</h2>
                                    <div class="card_btns">
                                        <p>¡Hasta 12 cuotas fijas!</p>
                                        <div class="ver_mas" id = ${resultado.id}><span>VER MAS</span></div>
                                    </div>
                                </div>
                            </article>
                    `
            })
        } else {
            console.error("Error en la solicitud:", response.status);
        }
    } catch (error) {
        console.error("Error:", error);
    }
};