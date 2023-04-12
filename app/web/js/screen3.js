const submitButton = document.getElementById("submit");
const peatonI = document.getElementById("peaton"),
  automovilI = document.getElementById("automovil"),
  campaeroI = document.getElementById("campaero"),
  camionetaI = document.getElementById("camioneta"),
  microI = document.getElementById("micro"),
  busetaI = document.getElementById("buseta"),
  busI = document.getElementById("bus"),
  camionI = document.getElementById("camion"),
  volquetaI = document.getElementById("volqueta"),
  motoI = document.getElementById("moto"),
  bicicletaI = document.getElementById("bicicleta"),
  horarioI = document.getElementById("horario"),
  gravedad = document.getElementById("gravedad"),
  prediccionI = document.getElementById("prediccion"),
  actoresI = document.getElementById("actores"),
  horario_prediccionI = document.getElementById("horario-prediccion");

function isEmpty(values) {
  return values.some((e) => e === "");
}

function unfill(elements) {
  for (let i = 0, n = elements.length; i < n; i++) elements[i].value = 0;
}

submitButton.addEventListener("click", async () => {
  values = [
    peatonI.value.trim(),
    automovilI.value.trim(),
    campaeroI.value.trim(),
    camionetaI.value.trim(),
    microI.value.trim(),
    busetaI.value.trim(),
    busI.value.trim(),
    camionI.value.trim(),
    volquetaI.value.trim(),
    motoI.value.trim(),
    bicicletaI.value.trim(),
    horarioI.value.trim(),
    gravedad.value.trim(),
  ];
  if (isEmpty(values)) {
    Swal.fire("Error", "Rellene todos los campos.", "error");
    return;
  }

  try {
    values.unshift(0);
    await eel.addrecord(values)();
    Swal.fire("¡Listo!", "Registro creado correctamente", "success");
    unfill([
      peatonI,
      automovilI,
      campaeroI,
      camionetaI,
      microI,
      busetaI,
      busI,
      camionI,
      volquetaI,
      motoI,
      bicicletaI,
    ]);
  } catch (e) {
    Swal.fire("Error", "Hubo un error añadiendo el registro", "error");
  }
});

prediccionI.addEventListener('click',async ()=> {
  d = horario_prediccionI.value.trim();
  data = await eel.getPrediction(parseInt(actoresI.value.trim()), d == "Diurno" ? 0 : 1)();
  console.log(data)
})