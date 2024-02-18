# tesis-project

## Backend Endpoints
| **ENDPOINT**| **METODO**| **DESCRIPCION**|**RESPUESTA**|
|------------ |-----------|----------------|----------|
| `/tag/`|POST|Utiliza el modelo creado previamente para predecir familias de polen en la imagen enviada y las señala en la misma|Devuelve la imagen señalando los diferentes tipos de polen|
| `/tag/health_check`|GET|Verifica que el endpoint se encuentre funcionando|Devuelve un mensaje indicando que la ruta funciona|
|`/email/`|POST|Envia un correo electronico como forma de contacto|Devuelve los datos que se usaron para el correo y un mensaje indicando que el correo fue enviado|
| `/email/health_check`|GET|Verifica que el endpoint se encuentre funcionando|Devuelve un mensaje indicando que la ruta funciona|
| `/health_check`|GET|Verifica que el backend se encuentre funcionando|Devuelve un mensaje indicando que el backend funciona|
