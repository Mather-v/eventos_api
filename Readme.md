✨ Buenas practicas API RESTfull ✨


🎭1- PLURALIDAD EN LOS RECURSOS

Siempre usar pluralidad en los endpoints:
✅ `/api/events`
❌ `/api/event`


👁️2- USAR SUSTANTIVOS, NO VERBOS EN LOS ENDPOINTS

El verbo ya lo indica el método HTTP.
✅ `POST /api/events (crear evento)`
❌ `POST /api/createEvent`


♨️3- RESPUESTAS CONSISTENTES EN FORMATO JSON

Todos los errores y datos deben tener el mismo formato.
Ejemplo de error:

{
  `"error": "Evento no encontrado",`
  `"status": 404`
}


🧨4- CODIGOS DE ERROR CORRECTOS

`200 → éxito.`
`201 → creado.`
`400 → error en datos enviados.`
`404 → no encontrado.`
`500 → error interno del servidor.`


⚙️5- VERSIONAR LA API

Cuando sea un proyecto serio, conviene poner la versión:
`/api/v1/events`

Filtrar y paginar:
`/api/events?categoria=conferencia&page=2.`





