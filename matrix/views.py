from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        def get_value(field_name):
            # If the field is empty or not provided, return 0
            value = request.POST.get(field_name, '')
            return int(value) if value else 0

        # Retrieve matrix A values
        a1 = get_value('a1')
        a2 = get_value('a2')
        a3 = get_value('a3')
        a4 = get_value('a4')
        a5 = get_value('a5')
        a6 = get_value('a6')
        a7 = get_value('a7')
        a8 = get_value('a8')
        a9 = get_value('a9')

        matrix_a = [
            [a1, a2, a3],
            [a4, a5, a6],
            [a7, a8, a9],
        ]

        # Retrieve matrix B values
        b1 = get_value('b1')
        b2 = get_value('b2')
        b3 = get_value('b3')
        b4 = get_value('b4')
        b5 = get_value('b5')
        b6 = get_value('b6')
        b7 = get_value('b7')
        b8 = get_value('b8')
        b9 = get_value('b9')

        matrix_b = [
            [b1, b2, b3],
            [b4, b5, b6],
            [b7, b8, b9],
        ]

        # Retrieve the selected operation and scalar multiplier
        operation = request.POST.get('operation')
        mulnum = request.POST.get('mulnum', 1)

        # Convert mulnum to an integer or float
        mulnum = int(mulnum) if mulnum else 1

        # Perform the selected operation
        result = []
        if operation == 'add':
            result = [
                [matrix_a[i][j] + matrix_b[i][j] for j in range(3)]
                for i in range(3)
            ]
        elif operation == 'sub':
            result = [
                [matrix_a[i][j] - matrix_b[i][j] for j in range(3)]
                for i in range(3)
            ]
        elif operation == 'mul':
            # Matrix multiplication
            result = [
                [
                    sum(matrix_a[i][k] * matrix_b[k][j] for k in range(3))
                    for j in range(3)
                ]
                for i in range(3)
            ]
        elif operation == 'div':
            # Matrix division (handle division by zero)
            result = [
                [
                    matrix_a[i][j] / matrix_b[i][j] if matrix_b[i][j] != 0 else 'Error'
                    for j in range(3)
                ]
                for i in range(3)
            ]
        elif operation == 'transa':
            # Transpose matrix A
            result = [
                [matrix_a[j][i] for j in range(3)]
                for i in range(3)
            ]
        elif operation == 'transb':
            # Transpose matrix B
            result = [
                [matrix_b[j][i] for j in range(3)]
                for i in range(3)
            ]
        elif operation == 'mula':
            # Multiply matrix A by scalar
            result = [
                [matrix_a[i][j] * mulnum for j in range(3)]
                for i in range(3)
            ]
        elif operation == 'mulb':
            # Multiply matrix B by scalar
            result = [
                [matrix_b[i][j] * mulnum for j in range(3)]
                for i in range(3)
            ]

        # Pass the result to the template for display
        return render(request, 'matrix_result.html', {'result': result})

    return render(request, 'index.html')
