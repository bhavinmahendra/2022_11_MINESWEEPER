'''
Bhavin Mahendra Gulab
Projeto - Minas
'''

########################################### TAD gerador ###########################################

# Contrutores

def cria_gerador(b, s):
    ''' 
    int x int -> gerador
    cria um gerador, utilizando o número de bits do gerador (b) e o estado inicial (s)
    devolve o gerador
    '''
    if type(b) == int and b in (32, 64) and type(s) == int and s > 0 and s <= 2**b:
        return [b, s]
    else:
        raise ValueError('cria_gerador: argumentos invalidos')

def cria_copia_gerador(g):
    ''' 
    gerador -> gerador
    devolve a copia do gerador g
    '''
    return [g[0], g[1]]

# Seletor

def obtem_estado(g):
    ''' 
    gerador -> int
    obtem o estado do gerador g
    devolve o estado
    '''
    return g[1]

# Modificadores

def define_estado(g, s):
    ''' 
    gerador x int -> int
    altera o estado do gerador g
    devolve esse estado
    '''
    g[1] = s
    return s

def atualiza_estado(g):
    ''' 
    gerador -> int
    altera o estado do gerador utilizando o xorshift de geracao de numeros pseudoaleatorios
    devolve esse estado
    '''
    if g[0] == 32: 
        g[1] ^= ( g[1] << 13 ) & 0xFFFFFFFF
        g[1] ^= ( g[1] >> 17 ) & 0xFFFFFFFF
        g[1] ^= ( g[1] << 5 ) & 0xFFFFFFFF
    else: 
        g[1] ^= ( g[1] << 13 ) & 0xFFFFFFFFFFFFFFFF
        g[1] ^= ( g[1] >> 7 ) & 0xFFFFFFFFFFFFFFFF        
        g[1] ^= ( g[1] << 17 ) & 0xFFFFFFFFFFFFFFFF
    return g[1]

# Reconhecedor

def eh_gerador(arg):
    '''
    universal -> booleano
    verifica se arg se trata de um gerador
    se arg for um gerador, devolve True, se nao, devolve False
    '''
    if type(arg) == list and len(arg) == 2:
        if type(arg[0]) == int and arg[0] in (32, 64) and \
           arg[1] > 0 and type(arg[1]) == int and arg[1] <= 2**arg[0]:
            return True
    return False

# Teste

def geradores_iguais(g1, g2):
    ''' 
    gerador x gerador -> booleano
    verifica se g1 e g2 são geradores iguais, caso ambos sejam geradores
    se sim , devolve True, se nao, devolve False
    '''
    if eh_gerador(g1) and eh_gerador(g2):
            return g1 == g2

# Tranformador

def gerador_para_str(g):
    ''' 
    gerador -> str
    devolve uma cadeia de caracteres contendo o tamanho e o estado do gerador g
    '''
    return 'xorshift' + str(g[0]) + '(s=' + str(g[1]) + ')'

# Funcoes de alto nivel

def gera_numero_aleatorio(g, n):
    ''' 
    gerador x int -> int
    atualiza o estado do gerador utilizando o algoritmo xorshift
    devolve um numero aleatorio entre 1 e n utilizando n e o estado do gerador
    '''
    if eh_gerador(g) and n > 0 and type(n) == int:
        s = atualiza_estado(g)
        return 1 + (s % n)

def gera_carater_aleatorio(g, c):
    ''' 
    gerador x str -> str
    atualiza o estado do gerador utilizando o algoritmo xorshift
    devolve um caracter aleatorio entre 'A' e 'Z' utilizando c e o estado do gerador
    '''
    colunas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if eh_gerador(g) and type(c) == str and c in colunas:
        s = atualiza_estado(g)
        cadeia = ''
        x = ord(c) + 1
        for i in range(ord('A'), x):
            cadeia += chr(i)
        l = len(cadeia)
        return cadeia[s % l]

######################################### TAD coordenada ##########################################

# Contrutor

def cria_coordenada(col, lin):
    ''' 
    str x int -> coordenada
    recebe uma letra maiuscula e um numero entre 1 e 99
    devolve a coordenada correspondente a essa letra e esse numero
    '''
    colunas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if type(col) == str and col in colunas and type(lin) == int and lin in range(1, 100):
        return (col, lin)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')

# Seletores

def obtem_coluna(c):
    ''' 
    coordenada -> str
    devolve a coluna da coordenada c
    '''
    return c[0]

def obtem_linha(c):
    ''' 
    coordenada -> str
    devolve a linha da coordenada c
    '''
    return c[1]

# Reconhecedor

def eh_coordenada(arg):
    ''' 
    universal -> booleano
    devolve a coluna da coordenada c
    verifica se arg se trata de uma coordenada
    se arg for uma coordenada, devolve True, se nao, devolve False
    '''
    colunas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if type(arg) == tuple and len(arg) == 2:
        if type(arg[0]) == str and arg[0] in colunas and \
           type(arg[1]) == int and arg[1] in range(1, 100):
            return True
    return False

# Teste

def coordenadas_iguais(c1, c2):
    ''' 
    coordenada x coordenada -> booleano
    verifica se c1 e c2 são coordenadas iguais, caso ambas sejam coordenadas
    se sim, devolve True, se nao, devolve False
    '''
    if eh_coordenada(c1) and eh_coordenada(c2):
        return c1 == c2

# Tranformadores

def coordenada_para_str(c):
    ''' 
    coordenada -> str
    devolve a cadeia de caracteres correspondente a coordenada c
    '''
    if eh_coordenada(c):
        return obtem_coluna(c) + str(f'{obtem_linha(c):02d}')

def str_para_coordenada(s):
    ''' 
    str -> coordenada
    devolve a coordenada correspondente a cadeia de caracteres s
    '''
    colunas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    linhas = '0123456789'

    if len(s) != 3 or s[1] not in linhas or s[2] not in linhas:
        return (None, None)
    
    col = s[0]
    lin = int(s[1:])
    if type(col) == str and col in colunas and type(lin) == int and lin in range(1, 100):
        return (col, lin)

# Funcoes de alto nivel

def obtem_coordenadas_vizinhas(c):
    ''' 
    coordenada -> tuplo
    devolve um tuplo com as coordenadas vizinhas a c
    '''
    if eh_coordenada(c):
        x = obtem_coluna(c)
        y = obtem_linha(c)
        x1, y1 = chr(ord(x) - 1), y - 1 
        x2, y2 = x, y - 1
        x3, y3 = chr(ord(x) + 1), y - 1 
        x4, y4 = chr(ord(x) + 1), y 
        x5, y5 = chr(ord(x) + 1), y + 1 
        x6, y6 = x, y + 1 
        x7, y7 = chr(ord(x) - 1), y + 1 
        x8, y8 = chr(ord(x) - 1), y
        vis = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8)]
        visinh = ()
        for i in vis: 
            if eh_coordenada(i):
                visinh += (i,)
        return visinh

def obtem_coordenada_aleatoria(c, g):
    ''' 
    coordenada x gerador -> coordenada
    devolve uma coordenada aleatoria utilizando o gerador g
    '''
    x = gera_carater_aleatorio(g, obtem_coluna(c))
    y = gera_numero_aleatorio(g, obtem_linha(c))
    return (x, y)

########################################### TAD parcela ###########################################

# Construtores

def cria_parcela():
    '''
    {} -> parcela
    devolve uma parcela tapada e sem mina
    '''
    return ['tapada', 'sem mina']

def cria_copia_parcela(p):
    '''
    parcela -> parcela
    devolve a copia da parcela p
    '''
    return [p[0], p[1]]

# Modificadores

def limpa_parcela(p):
    '''
    parcela -> parcela
    muda o estado da parcela p para limpa
    devolve p
    '''
    p[0] = 'limpa'
    return p
    
def marca_parcela(p):
    '''
    parcela -> parcela
    muda o estado da parcela p para marcada
    devolve p
    '''
    p[0] = 'marcada'
    return p

def desmarca_parcela(p):
    '''
    parcela -> parcela
    muda o estado da parcela p para tapada
    devolve p
    '''
    p[0] = 'tapada'
    return p
    
def esconde_mina(p):
    '''
    parcela -> parcela
    esconde uma mina na parcela p
    devolve p
    '''
    p[1] = 'com mina'
    return p

# Reconhecedores

def eh_parcela(arg):
    '''
    universal -> booleano
    verifica se arg se trata de um parcela
    se arg for uma parcela, devolve True, se nao, devolve False
    '''
    if type(arg) == list and len(arg) == 2:
        if arg[0] in ('tapada', 'limpa', 'marcada') and arg[1] in ('sem mina', 'com mina'):
            return True
    return False

def eh_parcela_tapada(p):
    '''
    parcela -> booleano
    verifica se a parcela p se trata de um parcela tapada
    se sim, devolve True, se nao, devolve False
    '''
    if type(p) == list and len(p) == 2:
        if p[0] == 'tapada':
            return True
    return False

def eh_parcela_marcada(p):
    '''
    parcela -> booleano
    verifica se a parcela p se trata de um parcela marcada
    se sim, devolve True, se nao, devolve False
    '''
    if type(p) == list and len(p) == 2:
        if p[0] == 'marcada':
            return True
    return False

def eh_parcela_limpa(p):
    '''
    parcela -> booleano
    verifica se a parcela p se trata de um parcela limpa
    se sim, devolve True, se nao, devolve False
    '''
    if type(p) == list and len(p) == 2:
        if p[0] == 'limpa':
            return True
    return False

def eh_parcela_minada(p):
    '''
    parcela -> booleano
    verifica se a parcela p se trata de um parcela que esconde uma mina
    se sim, devolve True, se nao, devolve False
    '''
    if type(p) == list and len(p) == 2:
        if p[1] == 'com mina':
            return True
    return False

# Teste

def parcelas_iguais(p1, p2):
    ''' 
    parcela x parcela -> booleano
    verifica se p1 e p2 são parcelas iguais, caso ambas sejam parcelas
    se sim, devolve True, se nao, devolve False
    '''
    if type(p1) == list and len(p1) == 2 and type(p2) == list and len(p2) == 2:
        if p1[0] in ('tapada', 'limpa', 'marcada') and p2[0] in ('tapada', 'limpa', 'marcada'):
            if p1[1] in ('sem mina', 'com mina') and p2[1] in ('sem mina', 'com mina'):
                return p1 == p2

# Transformador

def parcela_para_str(p):
    '''
    parcela -> str
    devolve a cadeia de caracteres correspondente ao estado da parcela e se contem mina ou nao
    '''
    if p[0] == 'tapada':
        return '#'
    elif p[0] == 'marcada':
        return '@'
    elif p[0] == 'limpa' and p[1] == 'sem mina':
        return '?'
    elif p[0] == 'limpa' and p[1] == 'com mina':
        return 'X'
    
# Funcoes de alto nivel

def alterna_bandeira(p):
    ''' 
    parcela -> booleano
    desmarca a parcela p, caso p seja uma parcela e seja marcada, devolvendo True
    marca a parcela p, caso p seja uma parcela e seja tapada, devolvendo True
    se a parcela nao for marcada nem tapada, devolve False
    '''
    if eh_parcela(p):
        if eh_parcela_marcada(p):
            desmarca_parcela(p)
            return True
        elif eh_parcela_tapada(p):
            marca_parcela(p)
            return True
    return False

############################################ TAD campo ############################################

# Contrutores

def cria_campo(c, l):
    ''' 
    str x int -> campo
    devolve um campo cuja a ultima coluna corresponde a c e a ultima linha corresponde a l
    '''
    colunas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if type(c) == str and len(c) == 1 and c in colunas:
        if type(l) == int and l in range(1, 100):
            campo = []
            for i in range(1, l + 1):
                for j in colunas:
                    campo.append([coordenada_para_str(cria_coordenada(j, i)), cria_parcela()])
                    if c == j:
                        break
            return campo
    raise ValueError('cria_campo: argumentos invalidos')

def cria_copia_campo(m):
    '''
    campo -> campo
    devolve a copia do campo m
    '''
    copia = []
    for i in m:
        copia.append([i[0], cria_copia_parcela(i[1])])
        
    return copia

# Seletores

def obtem_ultima_coluna(m):
    '''
    campo -> str
    devolve a ultima coluna de m
    '''
    colunas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letra = m[-1][0][0]
    if letra in colunas:
        return letra

def obtem_ultima_linha(m):
    '''
    campo -> int
    devolve a ultima linha de m
    '''
    numero = int(m[-1][0][1:])
    if numero in range(1, 100):
        return numero

def obtem_parcela(m, c):
    '''
    campo x coordenada -> parcela
    devolve a parcela com coordenada c do campo m
    '''
    coord = coordenada_para_str(c)
    for i in m:
        if i[0] == coord:
            return i[1]

def obtem_coordenadas(m, s):
    '''
    campo x str -> tuplo
    devolve um tuplo com todas as coordenadas com estado s
    '''
    listas = []
    for i in m:
        coord = str_para_coordenada(i[0])
        if coord not in listas:
            if s == 'tapadas' and eh_parcela_tapada(i[1]):
                listas.append(coord)
            elif s == 'limpas' and eh_parcela_limpa(i[1]):
                listas.append(coord)
            elif s == 'marcadas' and eh_parcela_marcada(i[1]):
                listas.append(coord)
            elif s == 'minadas' and eh_parcela_minada(i[1]):
                listas.append(coord)
    return tuple(listas)

def obtem_numero_minas_vizinhas(m, c):
    '''
    campo x coordenada -> int
    devolve o numero de parcelas vizinhas com minas
    '''
    for i in range(len(m)):
        if c == str_para_coordenada(m[i][0]):
            break
        
    a11 = chr(ord(c[0]) - 1) + str(f'{c[1] - 1:02d}')
    a12 = c[0] + str(f'{c[1] - 1:02d}')
    a13 = chr(ord(c[0]) + 1) + str(f'{c[1] - 1:02d}')
    a21 = chr(ord(c[0]) - 1) + str(f'{c[1]:02d}')
    a23 = chr(ord(c[0]) + 1) + str(f'{c[1]:02d}')
    a31 = chr(ord(c[0]) - 1) + str(f'{c[1] + 1:02d}')
    a32 = c[0] + str(f'{c[1] + 1:02d}')
    a33 = chr(ord(c[0]) + 1) + str(f'{c[1] + 1:02d}')
    cont = 0
    for i in m:
        if i[0] in [a11, a12, a13, a21, a23, a31, a32, a33]:
            if i[1][1] == 'com mina':
                cont += 1
    return cont

# Reconhecedores

def eh_campo(arg):
    '''
    universal -> booleano
    verifica se arg se trata de um campo
    se arg for uma campo, devolve True, se nao, devolve False
    '''
    if type(arg) == list and len(arg) > 0:
        for i in arg:
            if type(i) == list and len(i) == 2:
                if eh_coordenada(str_para_coordenada(i[0])) and eh_parcela(i[1]):
                    return True
                else:
                    return False
            else:
                return False
    return False

def eh_coordenada_do_campo(m, c):
    '''
    campo x coordenada -> booleano
    verifica se a coordenada c pertence ao campo m
    se sim, devolve True, se nao, devolve False
    '''
    for i in m:
        if i[0] == coordenada_para_str(c):
            return True
    return False

# Teste

def campos_iguais(m1, m2):
    '''
    campo x campo -> booleano
    verifica se m1 e m2 são campos iguais, caso ambas sejam campos
    se sim, devolve True, se nao, devolve False
    '''
    if len(m1) != len(m2):
        return False
    for i in range(len(m1)):
        if m1[i][0] != m2[i][0] or m1[i][1] != m2[i][1]:
            return False
    return True

# Tranformador

def campo_para_str(m):
    '''
    campo -> str
    devolve a cadeia de caracteres correspondente ao campo m
    '''
    c = obtem_ultima_coluna(m)
    colunas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cabecalho = '   '
    for i in colunas:
        cabecalho += i
        if i == c:
            break
    separador = '  +' + '-' * (ord(c) - ord('A') + 1) + '+'
    conteudo = ''
    linhas = []
    
    for i in range(len(m)):
        if eh_parcela_limpa(m[i][1]) and not eh_parcela_minada(m[i][1]):
            minas = obtem_numero_minas_vizinhas(m, str_para_coordenada(m[i][0]))
            simbolo = str(minas) if minas > 0 else ' '
        else:
            simbolo = parcela_para_str(m[i][1])
        conteudo += simbolo
        if len(conteudo) == ord(c) - ord('A') + 1:
            num_linha = f'{int(m[i][0][1:]):02d}'
            linhas.append(f'{num_linha}|{conteudo}|')
            conteudo = ''
    
    cadeia = cabecalho + '\n' + separador + '\n'
    for i in linhas:
        cadeia += i + '\n'
    cadeia += separador
    return cadeia

# Funcoes de alto nivel

def coloca_minas(m, c, g, n):
    '''
    campo x coordenada x gerador x int -> campo
    coloca n minas no campo m; as coordenadas das minas sao aleatorias (utilizando um gerador) 
    e nao coincidem com a coordenada c devolve o campo modificado
    '''
    proibido = [coordenada_para_str(c)]
    for i in obtem_coordenadas_vizinhas(c):
        if eh_coordenada_do_campo(m, i):
            proibido.append(coordenada_para_str(i))
    minas = []
    dimensoes = cria_coordenada(obtem_ultima_coluna(m), obtem_ultima_linha(m))
    i = 0
    while i < n:
        coord_a = obtem_coordenada_aleatoria(dimensoes, g)
        if coordenada_para_str(coord_a) not in proibido \
           and coordenada_para_str(coord_a) not in minas:
            minas.append(coordenada_para_str(coord_a))
            esconde_mina(obtem_parcela(m, coord_a))
            i += 1
    return m

def limpa_campo(m, c):
    '''
    campo x coordenaada -> campo
    limpa a coordenada c
    se nao houver minas nas parcelas vizinha, limpa-as
    devolve o campo modificado
    '''
    p = obtem_parcela(m, c)
    if eh_parcela_limpa(p):
        return m
    
    limpa_parcela(p)
    if not eh_parcela_minada(p) and obtem_numero_minas_vizinhas(m, c) == 0:
        for j in obtem_coordenadas_vizinhas(c):
            pvizinha = obtem_parcela(m, j)
            if eh_parcela_tapada(pvizinha):
                limpa_campo(m, j)
    return m

####################################### Funcoes Adicionais ########################################

def jogo_ganho(m):
    '''
    campo -> booleano
    caso todas as parcelas sem minas estiverem limpas, devolve True; se nao devolve False
    '''
    for i in m:
        if (not eh_parcela_limpa(i[1]) or eh_parcela_minada(i[1])) and \
           (not eh_parcela_minada(i[1]) or eh_parcela_limpa(i[1])):
            return False
    return True

def turno_jogador(m):
    '''
    campo -> booleano
    altera destrutivamente o campo, atraves de duas acoes, 'Limpar' e 'Marcar', numa coordenada 
    (ambos escolhidos pelo utilizador)
    caso o utilizador tiver escolhido 'Limpar' num parcela minada devolve False
    Caso contrario, se nao devolve True
    '''
    acao = ''
    while acao not in ('L', 'M'):
        acao = input('Escolha uma ação, [L]impar ou [M]arcar:')

    coord = ''
    while not eh_coordenada_do_campo(m, str_para_coordenada(coord)):
        coord = input('Escolha uma coordenada:')
    
    c = str_para_coordenada(coord)
    p = obtem_parcela(m, c)
    
    if acao == 'M':
        alterna_bandeira(p)
        return True
    elif acao == 'L':
        limpa_campo(m, c)
        return not eh_parcela_minada(p)

def minas(c, l, n, d, s):
    '''
    str x int x int x int x int -> booleano
    utiliza-se c e l para criar um campo, n para colocar minas, d e s para um gerador
    c, ultima coluna
    l, ultima linha
    n, numero de minas
    d, tamanho do gerador
    s, estado inicial do gerador
    devolve True se o jogador ganhar; se nao devolve False
    '''

    def printer(campo):
        bandeiras = len(obtem_coordenadas(campo, 'marcadas'))
        print('   [Bandeiras ' + str(bandeiras) + '/' + str(n) + ']')
        print(campo_para_str(campo))

    if type(c) != str or type(l) != int or type(n) != int or type(d) != int or type(s) != int or \
       len(c) != 1 or ord(c) not in range(ord('A'), ord('Z') + 1) or l not in range(1, 100) or \
       n not in range(1, (ord(c) - ord('A') + 1) * l - 9) or d not in (32, 64) or \
       s not in range(1, 2**d + 1):
        raise ValueError('minas: argumentos invalidos')


    gerador = cria_gerador(d, s)
    campo = cria_campo(c, l)
    printer(campo)

    coord = ''
    while not eh_coordenada_do_campo(campo, str_para_coordenada(coord)):
        coord = input('Escolha uma coordenada:')
    coord = str_para_coordenada(coord)
    coloca_minas(campo, coord, gerador, n)
    limpa_campo(campo, coord)

    while not jogo_ganho(campo):
        printer(campo)
        if not turno_jogador(campo):
            printer(campo)
            print('BOOOOOOOM!!!')
            return False
        
    printer(campo)
    print('VITORIA!!!')
    return True
