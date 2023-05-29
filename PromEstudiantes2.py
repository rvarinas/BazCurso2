import unittest

def calcular_promedio_notas(estudiantes):

    if not estudiantes:
        return None

    #Total Estudiantes
    total_estudiantes = len(estudiantes)

    suma_notas = 0

    for estudiante in estudiantes.values():
        suma_notas += estudiante["nota"]

    promedio = suma_notas/total_estudiantes
    return promedio


def imprimir_result(messages_rep,messages_aprob):
    messages_rep = "Reprobado"
    messages_aprob = "Aprobado"

    if not [estudiantes.value()]:
        return None
    if estudiantes.value('+= 50'):
        return messages_rep
    print('valores',estudiantes,estudiantes.value())
    if estudiantes.value('+= 60'):
        return messages_aprob
    print('valores',estudiantes, estudiantes.value())
class TestPromedio(unittest.TestCase):
    def testPromEstudiantes(self):
        estudiantes = {
            "Carlos": {"nota": 95},
            "Ivan": {"nota": 80},
            "Luis": {"nota": 58},
            "Jakob": {"nota": 92}
        }

        self.assertEqual(calcular_promedio_notas(estudiantes), 81.25)
        self.assertIsNone(calcular_promedio_notas({}))
        self.assertEqual(calcular_promedio_notas({"Juan":{"nota":85}}),85)
        self.assertEqual(imprimir_result("Aprobado","80"))


if __name__ == '__main__':
  unittest.main()
