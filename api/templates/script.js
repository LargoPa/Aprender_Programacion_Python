document.addEventListener("DOMContentLoaded", init);

const URL_API =  'http://localhost:3000/api/'

var customers = []

function init(){
  search()
}

async function search(){
  var url = URL_API+'customers'
  var response = await fetch(url, {
    "method": 'GET',
    "headers": {
      "Content-Type": 'application/json'
    }
  })
  customers = await response.json();
  var html = ''
  for(customer of customers){
    var row = `
    <tr>
      <td>${customer.firstname}</td>
      <td>${customer.lastname}</td>
      <td>${customer.email}</td>
      <td>${customer.phone}</td>
      <td>${customer.address}</td>
      <td>
          <a href="#" onclick="remove(${customer.id})" class="btnEliminar">Eliminar</a>
          <a href="#" onclick="edit(${customer.id})" class="btnEditar">Editar</a>
      </td>
    </tr>
    `
    html = html+row;
  }


document.querySelector('#customers > tbody').outerHTML = html
}


function edit(id){
  abrirFormulario()
  var customer = customers.find(x => x.id == id)
  document.getElementById('txtId').value = customer.id
  document.getElementById('txtFirstname').value = customer.firstname
  document.getElementById('txtLastname').value = customer.lastname
  document.getElementById('txtPhone').value = customer.phone
  document.getElementById('txtEmail').value = customer.email
  document.getElementById('txtAddress').value = customer.address
}



async function remove(id){
  respuesta = confirm('¿Estas seguro de eliminarlo?')
  if(respuesta){
    var url = URL_API+'customers/'+id
    await fetch(url, {
      "method": 'DELETE',
      "headers": {
        "Content-Type": 'application/json'
      }
    })
    window.location.reload();
  }
}


function clean(){
  document.getElementById('txtId').value = ''
  document.getElementById('txtFirstname').value = ''
  document.getElementById('txtLastname').value = ''
  document.getElementById('txtPhone').value = ''
  document.getElementById('txtEmail').value = ''
  document.getElementById('txtAddress').value = ''
}


async function save(){
  var data = {
    "firstname": document.getElementById('txtFirstname').value,
    "lastname": document.getElementById('txtLastname').value,
    "phone": document.getElementById('txtPhone').value,
    "email": document.getElementById('txtEmail').value,
    "address": document.getElementById('txtAddress').value
  }

  var id = document.getElementById('txtId').value
  var url = URL_API+'customers'
  if (id != ''){
    data.id = id
    url = url+'/'+id
    await fetch(url, {
      "method": 'PUT',
      "body": JSON.stringify(data),
      "headers": {
        "Content-Type": 'application/json'
      }
    })
  }
  else{
    await fetch(url, {
      "method": 'POST',
      "body": JSON.stringify(data),
      "headers": {
        "Content-Type": 'application/json'
      }
    })
  }
  window.location.reload();
}



function updatemenu() {
  if (document.getElementById('responsive-menu').checked == true) {
    document.getElementById('menu').style.borderBottomRightRadius = '0';
    document.getElementById('menu').style.borderBottomLeftRadius = '0';
  }else{
    document.getElementById('menu').style.borderRadius = '10px';
  }
}

function abrirFormulario(){
  htmlModal = document.getElementById("modal");
  htmlModal.setAttribute("class","modale opened");
}


function agregar(){
  clean()
  abrirFormulario()
}


function cerrarModal(){
  htmlModal = document.getElementById("modal");
  htmlModal.setAttribute("class","modale");
}

