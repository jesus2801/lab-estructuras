const table = document.querySelector(".table");
const rightButton = document.querySelector("#right-button");
const leftButton = document.querySelector("#left-button");
const pageNumber = document.querySelector("#page-number");
const rowsPerPage = 100;

const filter = document.querySelector("#filter");
const field = document.querySelector("#slct");

let matrix = [];

leftButton.addEventListener("click", () => {
  page = parseInt(pageNumber.textContent) - 1;
  if (page === 0) return;

  pageNumber.innerText = page;
  updateTable(rowsPerPage * page - rowsPerPage + 1, rowsPerPage * page);
});

rightButton.addEventListener("click", async () => {
  page = parseInt(pageNumber.textContent) + 1;
  data = await eel.gettable(
    rowsPerPage * page - rowsPerPage + 1,
    rowsPerPage * page
  )();

  if (data.length > 0) {
    pageNumber.innerText = page;
    updateTable(rowsPerPage * page - rowsPerPage + 1, rowsPerPage * page);
  }
});

field.addEventListener("change", filterTable);

function filterTable() {
  let key = field.value;
  if (key === "") {
    printTable(matrix);
    return;
  }

  key = parseInt(key);
  const value = filter.value;

  let filteredMatrix = [matrix[0]];
  for (let i = 1, n = matrix.length; i < n; i++) {
    if (matrix[i][key] == value) filteredMatrix.push(matrix[i]);
  }

  printTable(filteredMatrix);
}

updateTable(1, rowsPerPage);
async function updateTable(start, end) {
  matrix = await eel.gettable(start, end)();
  filterTable();
}

function printTable(matrix) {
  table.innerHTML = "";

  let tableHtml = "<div class='header'>";
  for (let i = 0, n = matrix[0].length; i < n; i++) {
    tableHtml += `<p>${matrix[0][i]}</p>`;
  }
  tableHtml += "</div>";
  table.innerHTML = tableHtml;

  const body = document.createElement("div");
  body.classList.add("body");
  table.appendChild(body);

  for (let i = 1, n = matrix.length; i < n; i++) {
    const element = document.createElement("div");
    element.classList.add("element");
    element.id = "dato" + matrix[i][0];

    for (let j = 0, n = matrix[i].length; j < n; j++) {
      const data = document.createElement("p");
      data.innerText = matrix[i][j];
      element.appendChild(data);
    }
    body.appendChild(element);

    new VanillaContextMenu({
      scope: document.querySelector(`#dato${matrix[i][0]}`),
      menuItems: [
        {
          label: "Delete",
          iconClass: "fa-solid fa-trash",
          callback: () => {
            element.remove();
            eel.deleterecord(matrix[i][0])();
          },
        },
      ],
      theme: "black",
    });
  }
}
