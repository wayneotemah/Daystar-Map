// open modal js

//get the nesseccary elemnts 
const openModalButtons = document.querySelectorAll('[data-modal-target]')
const closeModalButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')


//looping through all oelements that can open a modal
// opening the click event on them and calling the opening modal function
openModalButtons.forEach(button => {
  button.addEventListener('click',() => {
    const modal = document.querySelector(button.dataset.modalTarget)
    openModal(modal)
  })
})

//closing the modal by closing in the overlay outside the modal 
overlay.addEventListener('click',()=>{
  const modals = document.querySelectorAll('.modalup.active')
  modals.forEach(modal => {
    closeModal(modal)
  })
})

//looping through all oelements that can class a modal
// creating the click event on them and calling the close modal function
closeModalButtons.forEach(button => {
  button.addEventListener('click',()=>{
    const modal = button.closest('.modalup')
    closeModal(modal)
  })
})


//open modal function
function openModal(modal){
  if (modal == null) return
  modal.classList.add('active')
  overlay.classList.add('active')
}

//closing the modal function
function closeModal(modal){
  if (modal == null) return
  modal.classList.remove('active')
  overlay.classList.remove('active')
}