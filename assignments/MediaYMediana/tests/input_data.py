# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    [0],
    ["", "Error"],
    ["Se debe mostrar Error cuando la primer entrada es menor a 1."]
    ),
    # Test case 2
    (
    [7, 5, 8, 20, 9, 33, 42, 2],
    ["", "", "", "", "", "", "", "", "Media: 17.0", "Mediana: 9.0"],
    ["La media o la mediana no tienen el valor correcto."]
    ),
    # Test case 3
    (
    [6, 4, 10, 13, 5, 17, 5],
    ["", "", "", "", "", "", "", "Media: 9.0", "Mediana: 7.5"],
    ["La media o la mediana no tienen el valor correcto."]
    )
]
