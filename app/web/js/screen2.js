const statistics = document.querySelector(".statistics");

const icons = {
  Moda: '<i class="fa-solid fa-ranking-star"></i>',
  Mediana: '<i class="fa-solid fa-chart-area"></i>',
  Media: '<i class="fa-solid fa-chart-pie"></i>',
  máximo: '<i class="fa-solid fa-chart-line"></i>',
  mínimo: '<i class="fa-solid fa-chart-gantt"></i>',
};

async function main() {
  const actores = await eel.actoresViales()();
  config = {
    type: "line",
    data: {
      labels: [...Array(actores.length).keys()],
      datasets: [
        {
          label: "Histórico de actores viales",
          data: actores,
          fill: false,
          borderColor: "rgb(75, 192, 192)",
          tension: 0,
        },
      ],
    },
    options: {
      animation: false,
      elements: {
        point: {
          radius: 0,
        },
      },
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          enabled: false,
        },
      },
      scales: {
        x: {
          display: false,
        },
      },
    },
  };

  new Chart(document.getElementById("chart"), config);

  //estadísticas
  const data = await eel.statisticData()();
  for (column in data) {
    const title = document.createElement("h2");
    title.innerText = column;
    statistics.appendChild(title);

    const cards = document.createElement("div");
    cards.classList.add("cards");
    for (statistic in data[column]) {
      const card = document.createElement("div");
      card.classList.add("card");
      card.innerHTML = `
     <div class="info">
        <p>${statistic}</p>
        <p>${
          data[column][statistic] != "N/A"
            ? typeof data[column][statistic] === "string"
              ? data[column][statistic]
              : parseFloat(data[column][statistic]).toFixed(3)
            : "<span class='red'>N/A</span>"
        }</p>
      </div>
      ${icons[statistic]}`;
      cards.appendChild(card);
    }
    statistics.appendChild(cards);
  }
}

main();
