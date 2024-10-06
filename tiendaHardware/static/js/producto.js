const agregarCarrito = (id)=>{
    let carrito = JSON.parse(localStorage.getItem('carrito')) || []
    console.log(localStorage.getItem('carrito'))
    carrito.push(2)
    carrito.push(3)
    carrito.push(4)
    carrito = carrito.filter(producto => producto != 2)
    localStorage.setItem('carrito', JSON.stringify(carrito));
    console.log(localStorage.getItem('carrito'))
}

let precio = document.getElementById("precio_contado")
console.log(precio)

