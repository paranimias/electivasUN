import requests
import json


def retrieve_json_electivas():
    url = (
        "https://bobt42d1b3.execute-api.us-east-1.amazonaws.com/api/v1/buscadorcursos/"
        "busqueda/primernivel2/?nivel=PREGRADO&sede=SEDE+BOGOT%C3%81&facultad=2050+"
        "FACULTAD+DE+CIENCIAS&planEstudio=2933+CIENCIAS+DE+LA+COMPUTACI%C3%93N&page"
        "=1&limit=100&tipologia=L+LIBRE+ELECCI%C3%93N"
    )
    r = requests.get(url)
    r.status_code
    return json.loads(r.text)


def electivas_con_cupo(data):
    result = []
    for electiva in data["data"]:
        dupla = (electiva["NOMBREASIGNATURA"], [])
        for grupo in electiva["DETALLECURSOASIGNATURA"]:
            if (
                grupo["CUPOS_DISPONIBLES"] is not None
                and grupo["CUPOS_DISPONIBLES"] > 0
            ):
                dupla[1].append(grupo)
        if len(dupla[1]) > 0:
            result.append(dupla)
    return result


def print_electivas(grouplist):
    for electiva in grouplist:
        print("------------------------------")
        print(f"[{electiva[0].upper()}]", end="\n")
        for group in electiva[1]:
            print(f"├──[{group["GRUPO"]}]", end="\n")
            print(f"│   ├── {group["CODIGO_ASIGNATURA"]}", end="\n")
            print(f"│   ├── {group["DOCENTE"]}", end="\n")
            for key, value in group.items():
                if key.startswith("HORARIO") and value is not None:
                    print(f"│   ├──{key}: {value}", end="\n")


def retrieve_json(code):
    url = (
        "https://bobt42d1b3.execute-api.us-east-1.amazonaws.com/api/v1"
        "/buscadorcursos/busqueda/primernivel2/?nivel=PREGRADO&sede=SEDE+BOGOT%C3%81&"
        "facultad=2050+FACULTAD+DE+CIENCIAS&planEstudio=2933+CIENCIAS+DE+LA+"
        "COMPUTACI%C3%93N&page=1&limit=100&codigo_asignatura="
    )
    r = requests.get(url + code)
    r.status_code
    return json.loads(r.text)


def grupos_con_cupo(data):
    class_name = data["data"][0]["NOMBREASIGNATURA"]
    group_list = data["data"][0]["DETALLECURSOASIGNATURA"]
    result = []
    for group in group_list:
        if group["CUPOS_DISPONIBLES"] > 0:
            result.append(group)
    return (class_name, result)


def print_results(group_duple):
    print("------------------------------")
    print(f"[{group_duple[0].upper()}]--------", end="\n")
    for group in group_duple[1]:
        print(f"├──[{group["GRUPO"].upper()}]-----", end="\n")
        print(f"│   ├──{group["DOCENTE"]}", end="\n")
        for key, value in group.items():
            if key.startswith("HORARIO") and value is not None:
                print(f"│   ├──{key}: {value}", end="\n")


if __name__ == "__main__":
    option = input("[0] Electivas, [1] Asignaturas CC: ")
    if option == "1":
        codes = input("ingrese códigos de asignatura separados por una coma: ")
        code_list = codes.split(",")
        for code in code_list:
            print_results(grupos_con_cupo(retrieve_json(code)))
    elif option == "0":
        print_electivas(electivas_con_cupo(retrieve_json_electivas()))
    else:
        print("opción no disponible")
