
//getting the DOM

// let commentBtn = document.getElementById('comment')
// let commentSection = document.getElementById('commentSec')

// commentBtn.onclick = ()=>{
//     commentSection.style.display = 'block'
//     commentSection.classList.toggle('displayComments')
// }

$(()=>{
  $('#comment').click(()=>{
    $('#commentSec').fadeToggle(500)
  })
})