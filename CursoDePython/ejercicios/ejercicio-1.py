
#promedio de duracion
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
este_curso=1.5



diferencia_con_min = 100-((este_curso/otros_cursos_min)*100)
diferencia_con_max = 100-((este_curso*1000//otros_cursos_max)/10)
diferencia_con_promedio = 100-((este_curso/otros_cursos_promedio)*100)


print(f"El curso este dura un {diferencia_con_min}% menos que el curso mas rapido")
print(f"El curso este dura un {diferencia_con_max}% menos que el curso mas lento")
print(f"El curso este dura un {diferencia_con_promedio}% menos que los cursos en promedio")

 

