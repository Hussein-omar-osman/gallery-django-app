const opens = document.querySelectorAll('.open');
const modals = document.querySelectorAll('.modal-bg');
const modalClose = document.querySelectorAll('.modal-close');
const modalClose2 = document.querySelectorAll('.modal-close2');
const overlay = document.getElementById('overlay');

// const btn_copys = document.querySelectorAll('.btn_copy');
// console.log('Connected');
opens.forEach((btn, index) => {
  btn.addEventListener('click', () => {
    // console.log(`${index}: clicked`);
    const modalClicked = modals[index];
    modalClicked.classList.add('bg-active');
  });
});

modalClose.forEach((ele, index) => {
  ele.addEventListener('click', () => {
    const modalClicked = modals[index];
    modalClicked.classList.remove('bg-active');
  });
});
modalClose2.forEach((ele, index) => {
  ele.addEventListener('click', () => {
    const modalClicked = modals[index];
    modalClicked.classList.remove('bg-active');
  });
});

function copyAndClip(id) {
  let copyText = document.getElementById(id);

  let btnCopy = document.getElementById(`${id}b`);
  copyText.select();
  document.execCommand('Copy');
  console.log(copyText.value);
  btnCopy.innerHTML = '<i class="fa-solid fa-check"></i>';
  setTimeout(function () {
    btnCopy.innerHTML = '<i class="fa-solid fa-copy"></i>';
  }, 800);
}
