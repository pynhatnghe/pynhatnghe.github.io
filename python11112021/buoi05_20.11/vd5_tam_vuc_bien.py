'''Tầm vực biến: global (toàn cục), local (cục bộ)'''

x = "Global"


def process_x(param):
    # x = "PROCESS X"
    global x
    x = param
    print("Inside process_x x=", x)


process_x("PYTHON")
print("Outside process_x x=", x)
