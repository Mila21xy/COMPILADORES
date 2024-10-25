import ply.lex as lex
import csv
import re

# ANALIZADOR LEXICO
# Lista de Tokens
tokens = (
    'identificador', 'num', 'bool', 'texto', 'lla_L', 'lla_R', 'pyc',
    'dosp', 'punto', 'coma', 'dif', 'o_Ma', 'o_me', 'o_mayeq', 'o_meneq',
    'Mmin', 'Mmas', 'co_L', 'co_R', 'o_sum', 'o_mul', 'o_and',
    'o_div', 'o_res', 'o_equ', 'o_2eq', 'o_dif', 'par_L', 'par_R', 'while', 'for',
    'if', 'else', 'do', 'break', 'return', 'case', 't_int', 't_double',
    't_char', 't_float', 't_string', 'boool',
    'com_lineal', 'com_mult', 'lit', 'main', 'cout', 'cin', 'endl'
)

# Expresiones regulares para cada token
t_identificador = r'[a-zA-Z][a-zA-Z0-9]*'
t_num = r'\d+'
t_bool = r'[VF]'
t_texto = r'\".*\"'
t_lla_L = r'\{'
t_lla_R = r'\}'
t_pyc = r';'
t_dosp = r':'
t_punto = r'\.'
t_coma = r','
t_dif = r'!='
t_o_Ma = r'>'
t_o_me = r'<'
t_o_mayeq = r'>='
t_o_meneq = r'<='
t_Mmin = r'--'
t_Mmas = r'\+\+'
t_co_L = r'<<'
t_co_R = r'>>'
t_o_sum = r'\+'
t_o_mul = r'\.\.'
t_o_and = r'&&'
t_o_div = r'/'
t_o_res = r'-'
t_o_equ = r'='
t_o_dif = r'!='
t_o_2eq = r'=='
t_par_L = r'\('
t_par_R = r'\)'
t_while = r'WHILE'
t_for = r'FOR'
t_if = r'IF'
t_else = r'ELSE'
t_do = r'DO'
t_break = r'BREAK'
t_return = r'RETURN'
t_case = r'CASE'
t_t_int = r'INT'
t_t_double = r'DOUBLE'
t_t_char = r'CHAR'
t_t_float = r'FLOAT'
t_t_string = r'STRING'
t_boool = r'BOOL'
t_com_lineal = r'//.*'
t_com_mult = r'/\*.*\*/'
t_lit = r'\'[^\']*\''
t_main = r'MAIN'
t_cout = r'COUT'
t_cin = r'CIN'
t_endl = r'ENDL'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

def tokenize_code(input_code):
    # Darle la entrada al lexer
    lexer.input(input_code)

    # Lista para almacenar los tokens como diccionarios
    tokens_list = []

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No hay más entrada
        tokens_list.append({'type': tok.type, 'value': tok.value, 'line': tok.lineno, 'position': tok.lexpos})

    return tokens_list

def write_tokens_to_file(tokens_list):
    # Escribir los tokens en Input.txt para procesamiento adicional si es necesario
    with open("Input.txt", "w") as f:
        for token in tokens_list:
            f.write(f"{token['type']} ")
        f.write("$\n")  # Añadir $ al final después de todos los tokens

    # Escribir los detalles completos de cada token en Detalles.txt
    with open("Detalles.txt", "w") as f:
        for token in tokens_list:
            f.write(f"Type: {token['type']}, Value: {token['value']}, Line: {token['line']}, Position: {token['position']}\n")

def generate_dot_file(tokens_list):
    # Abrir el archivo .dot para escribir el grafo
    with open("graph.dot", "w") as f:
        f.write("digraph G {\n")

        # Escribir los nodos
        for i, token in enumerate(tokens_list):
            f.write(f'  node{i} [label="{token["type"]}: {token["value"]}"];\n')

        # Escribir las aristas
        for i in range(len(tokens_list) - 1):
            f.write(f'  node{i} -> node{i+1};\n')

        f.write("}")

# Leer el contenido del archivo de código fuente
with open('source_code.txt', 'r') as file:
    data = file.read()

# Obtener la lista de tokens
tokens_list = tokenize_code(data)

# Escribir tokens en archivos
write_tokens_to_file(tokens_list)

# Generar archivo .dot
generate_dot_file(tokens_list)