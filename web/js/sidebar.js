const sidebar = document.querySelector(".sidebar"),
    closeBtn = document.querySelector("#btn"),
    searchBtn = document.querySelector(".bx-search"),
    searchInput = document.querySelector("#search-input")

const listItems = document.querySelectorAll(".list-item")

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();//calling the function(optional)
});

searchBtn.addEventListener("click", () => { // Sidebar open when you click on the search icon
    sidebar.classList.toggle("open");
    menuBtnChange(); //calling the function(optional)
});

searchInput.addEventListener("input", () => {
    const searchedText = searchInput.value.trim().toLowerCase()

    if (searchedText !== "") {
        listItems.forEach((e) => {
            const itemText = e.querySelector("span").innerText.toLowerCase()

            if (itemText.indexOf(searchedText) == -1) e.classList.add("ocult")
            else e.classList.remove("ocult")
        });
    }else {
        listItems.forEach((e)=>{
            e.classList.remove("ocult")
        })
    }
});

// following are the code to change sidebar button(optional)
function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
    } else {
        closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");//replacing the iocns class
    }
}