const nextbtn = document.querySelector('#nextbtn');
const backbtn = document.getElementById("backbtn");
const container = document.querySelector(".gallery")


container.addEventListener("wheel", (e)=>{
    e.preventDefault;
    container.scrollLeft += e.deltaX;
    container.style.scrollBehavior = "auto"

    
});

nextbtn.addEventListener("click", (e)=>{
    container.scrollLeft += container.clientWidth;
    container.style.scrollBehavior = "smooth";

    
})

backbtn.addEventListener('click', ()=>{
    container.scrollLeft -= container.clientWidth;
    container.style.scrollBehavior = "smooth" 
})