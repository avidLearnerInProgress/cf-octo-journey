'''
"Tetrahedron" (without quotes), if the i-th polyhedron in Anton's collection is a tetrahedron.
"Cube" (without quotes), if the i-th polyhedron in Anton's collection is a cube.
"Octahedron" (without quotes), if the i-th polyhedron in Anton's collection is an octahedron.
"Dodecahedron" (without quotes), if the i-th polyhedron in Anton's collection is a dodecahedron.
"Icosahedron" (without quotes), if the i-th polyhedron in Anton's collection is an icosahedron
'''

def faces_total(faces):
    if faces is None:
        return 0
    faces = [face.lower() for face in faces]
    face_list = {'tetrahedron':4, 'cube':6, 'octahedron':8, 'dodecahedron':12, 'icosahedron':20}
    
    total_faces = 0
    for f in faces:
        if f in face_list:
            total_faces += face_list[f]
        else:
            pass
    return total_faces           

if __name__ == '__main__':
    total = int(input())
    faces = []
    for i in range(total):
        faces.append(str(input()))
    print(faces_total(faces))