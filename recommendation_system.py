calificaciones = {
	"Ana": {
		"Matrix": 5,
		"Titanic": 2,
		"Toy Story": 4,
	},
	"Bruno": {
		"Matrix": 5,
		"Titanic": 1,
		"Toy Story": 4,
		"Inception": 5,
		"Interstellar": 4,
	},
	"Carla": {
		"Matrix": 3,
		"Titanic": 5,
		"Toy Story": 4,
		"Coco": 5,
	},
	"Diego": {
		"Matrix": 4,
		"Titanic": 2,
		"Toy Story": 5,
		"Inception": 4,
		"Coco": 3,
	},
}


def calcular_similitud(primer_usuario, segundo_usuario):
	peliculas_en_comun = set(primer_usuario) & set(segundo_usuario)

	if not peliculas_en_comun:
		return 0

	diferencia = sum(
		abs(primer_usuario[pelicula] - segundo_usuario[pelicula])
		for pelicula in peliculas_en_comun
	) / len(peliculas_en_comun)

	return 1 - diferencia / 4


def recomendar_peliculas(nombre_usuario, cantidad_recomendaciones=3):
	if nombre_usuario not in calificaciones:
		return []

	calificaciones_usuario = calificaciones[nombre_usuario]
	puntuaciones_ponderadas = {}
	totales_similitud = {}

	for otro_nombre, otras_calificaciones in calificaciones.items():
		if otro_nombre == nombre_usuario:
			continue

		similitud = calcular_similitud(calificaciones_usuario, otras_calificaciones)

		for pelicula, calificacion in otras_calificaciones.items():
			if pelicula not in calificaciones_usuario and similitud > 0:
				puntuaciones_ponderadas[pelicula] = puntuaciones_ponderadas.get(pelicula, 0) + calificacion * similitud
				totales_similitud[pelicula] = totales_similitud.get(pelicula, 0) + similitud

	recomendaciones = [
		(pelicula, puntuaciones_ponderadas[pelicula] / totales_similitud[pelicula])
		for pelicula in puntuaciones_ponderadas
	]
	recomendaciones.sort(key=lambda elemento: elemento[1], reverse=True)

	return recomendaciones[:cantidad_recomendaciones]


if __name__ == "__main__":
	nombre_usuario = "Ana"
	recomendaciones = recomendar_peliculas(nombre_usuario)

	print(f"Recomendaciones para {nombre_usuario}:")

	if recomendaciones:
		for pelicula, puntuacion in recomendaciones:
			print(f"- {pelicula} (puntuación estimada: {puntuacion:.1f}/5)")
	else:
		print("No hay recomendaciones disponibles.")
