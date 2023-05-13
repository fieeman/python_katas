'''
Eres un compositor que acaba de escribir una pieza musical impresionante. Ahora es el momento de presentarla a una banda que interpretará tu pieza, ¡pero hay un problema! El rango vocal de los cantantes no se extiende como requiere tu pieza, y tienes que transponer toda la pieza.

Su tarea
Dada una lista de notas (representadas como cuerdas) y un intervalo, produzca una lista de notas transpuestas en notación sostenida.

Las notas de entrada pueden representarse tanto en bemol como en sostenido (más información a continuación).

Para esta kata, supongamos que la entrada es siempre válida y que la canción dura al menos 1 nota.

Supongamos que el intervalo es un número entero entre -12 y 12.

Breve introducción a la notación musical
Transponer una nota significa desplazar su valor un intervalo determinado.

Las notas son las siguientes:

A, A#, B, C, C#, D, D#, E, F, F#, G, G#.
Se utiliza la notación sostenida, en la que "#" después de una nota significa que es un paso más alta que la nota. Así, A# es un paso más alto que A.

Una alternativa a la notación aguda es la notación llana:

A, Bb, B, C, Db, D, Eb, E, F, Gb, G, Ab.
La "b" después de una nota significa que es un paso más grave que la nota.
'''

def transpose(song, interval):
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    rotate_notes = notes[interval:] + notes[:interval]
    relation = {
        "Bb" : "A#",
        "Db" : "C#",
        "Eb" : "D#",
        "Gb" : "F#",
        "Ab" : "G#"
    }
    new_notes = []
    
    for s in song:
        
        if ("b" in s):
            s = relation[s]
        ref = notes.index(s)
        note = rotate_notes[ref]
        new_notes.append(note)
        
    return new_notes