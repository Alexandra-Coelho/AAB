# -- coding: utf-8 --
"""
@author: Alexandra,Andreia,Catarina,Daniela
"""

'''@package docstring
Implementação da procura de Motifs biológicos
'''


"""
Class: MySeq
"""

class MySeq:
    '''
    Classe MySeq implementa um conjunto de funções que pemitem, a partir de uma sequência inicial, obter a sequência transcrita, o complemento inverso,
     a tradução, as ORF´s e por fim a maior proteína nas ORF's.
    '''

    def __init__(self, seq : str, tipo: str = "dna"):
        '''
        Construtor, recebe a sequência introduzida e guarda-a para ser utilizada pelos restantes métodos
        
        Parameters
        ----------
        :param seq: Sequência introduzida
        
        '''
        self.seq = seq.upper()
        self.tipo = tipo

    def __len__(self) -> int:
        """
        Define o tamanho da sequência que foi introduzida

        """
        return len(self.seq)
    
    def __getitem__(self, n: int) -> str:
        """
        Função vai buscar o elemento n à sequência

         Parameters
        ----------
        :param n: elemento n 

        """
        return self.seq[n]

    def __getslice__(self, i: int, j: int) -> str:
        """
        Função vai buscar o uma fração da sequência

         Parameters
        ----------
        :param i: elemento i inicial 

        :param j: elemento j final
        """
        return self.seq[i:j]

    def __str__(self) -> str:
        """
        Define o tipo da sequência

        """
        return self.tipo + ":" + self.seq

    def printseq(self) -> str:
        """
        Imprime a sequência

        """
        print(self.seq)
    
    def alfabeto(self) -> str:  
        """
        Define o alfabeto utilizado na sequência

        """
        if (self.tipo=="dna"): return "ACGT"
        elif (self.tipo=="rna"): return "ACGU"
        elif (self.tipo=="protein"): return "ACDEFGHIKLMNPQRSTVWY"
        else: return None
    
    def valida(self) -> str: 
        """
        Valida se a sequência pertence a algum dos alfabetos anteriores

        """
        alf = self.alfabeto()
        res = True
        i = 0
        while i < len(self.seq) and res:
            if self.seq[i] not in alf: 
                res = False
            else: i += 1
        return res 
    
    def validaER(self) -> str: 
        """
        Valida se a sequência pertence a algum dos alfabetos anteriores
        utilizando para isso expressões regulares

        """
        import re
        if (self.tipo=="dna"):
            if re.search("[^ACTGactg]", self.seq) != None: return False
            else: return True 
        elif (self.tipo=="rna"):
            if re.search("[^ACUGacug]", self.seq) != None:  return False
            else: return True
        elif (self.tipo=="protein"):
            if re.search("[^ACDEFGHIKLMNPQRSTVWY_acdefghiklmnpqrstvwy]", self.seq) != None:
                return False
            else: return True
        else: return False    
    
    def transcricao (self) -> str:  #trabceição
        """
        Faz a transcrição da sequência, transformando uma sequência de DNA em RNA,
        substituindo para isso a base timina 'T' por uracilo 'U'

        """        
        if (self.tipo == "dna"):
            return MySeq(self.seq.replace("T","U"), "rna")
        else:
            return None
        
    def compInverso(self) -> str: 
        """
        Faz o complemento inverso da sequência, apenas se a sequência for do tipo DNA

        """
        if (self.tipo != "dna"): return None
        comp = ""
        for c in self.seq:
            if (c == 'A'):
                comp = "T" + comp 
            elif (c == "T"): 
                comp = "A" + comp 
            elif (c == "G"): 
                comp = "C" + comp
            elif (c== "C"): 
                comp = "G" + comp
        return MySeq(comp)

    def traduzSeq (self, iniPos= 0) -> str: 
        """
        Traduz a sequência, se esta for de DNA, em prteína
        
        """
        if (self.tipo != "dna"): return None
        seqM = self.seq
        seqAA = ""
        for pos in range(iniPos,len(seqM)-2,3):
            cod = seqM[pos:pos+3]
            seqAA += self.traduzCodao(cod)
        return MySeq(seqAA, "protein")

    def orfs (self) -> str:  
        """
        Constroí as 6 ORF's, 3 a partir da sequência normal e 3 a partir do complemento inverso
        
        """
        if (self.tipo != "dna"): return None
        res = []
        res.append(self.traduzSeq(0))
        res.append(self.traduzSeq(1))
        res.append(self.traduzSeq(2))
        compinv = self.compInverso()
        res.append(compinv.traduzSeq(0))
        res.append(compinv.traduzSeq(1))
        res.append(compinv.traduzSeq(2))    
        return res

    def traduzCodao (self, cod : str) -> str:
        """
        Utiliza uma biblioteca para fazer corresponder os codões a cada aminiácido, 
        se o codão não estiver  presente no dicionário é marcado com um 'X'
        ----------
        :param cod: codão
        
        """
        tc = {"GCT":"A", "GCC":"A", "GCA":"A", "GCC":"A", "TGT":"C", "TGC":"C",
      "GAT":"D", "GAC":"D","GAA":"E", "GAG":"E", "TTT":"F", "TTC":"F",
      "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G","CAT":"H", "CAC":"H",
      "ATA":"I", "ATT":"I", "ATC":"I",
      "AAA":"K", "AAG":"K",
      "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
      "ATG":"M", "AAT":"N", "AAC":"N",
      "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
      "CAA":"Q", "CAG":"Q",
      "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
      "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
      "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
      "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
      "TGG":"W",
      "TAT":"Y", "TAC":"Y",
      "TAA":"_", "TAG":"_", "TGA":"_"}
        if cod in tc:
            aa = tc[cod]
        else: aa = "X" # errors marked with X
        return aa

    def traduzCodaoER (self, cod : str) -> str:
        """
        Utiliza expressões regulares para fazer corresponder os codões a cada aminiácido
        ----------
        :param cod: codão
        
        """
        import re
        if re.search("GC.", cod): aa = "A"
        elif re.search("TG[TC]", cod): aa = "C" 
        elif re.search("GA[TC]", cod): aa = "D"
        elif re.search("GA[AG]", cod): aa = "E"
        elif re.search("TT[TC]", cod): aa = "F"
        elif re.search("GG.", cod): aa = "G"
        elif re.search("CA[TC]", cod): aa = "H"
        elif re.search("AT[TCA]", cod): aa = "I"
        elif re.search("AA[AG]", cod): aa = "K"
        elif re.search("TT[AG]|CT.", cod): aa = "L"
        elif re.search("ATG", cod): aa = "M"
        elif re.search("AA[TC]", cod): aa = "N"
        elif re.search("CC.", cod): aa = "P"
        elif re.search("CA[AG]", cod): aa = "Q"
        elif re.search("CG.|AG[AG]", cod): aa = "R"
        elif re.search("TC.|AG[TC]", cod): aa = "S"
        elif re.search("AC.", cod): aa = "T"
        elif re.search("GT.", cod): aa = "V"
        elif re.search("TGG", cod): aa = "W"
        elif re.search("TA[TC]", cod): aa = "Y"
        elif re.search("TA[AG]|TGA", cod): aa = "_";
        else: aa = None     
        return aa

    def maiorProteina (self) -> str:
        """
        Função devolve a maior proteina obtida a partir da sequência

        """
        if (self.tipo != "protein"):
            return None
        seqAA = self.seq
        protAtual = ""
        maiorprot = ""
        for aa in seqAA:
            if aa == "_":
                if len(protAtual) > len(maiorprot):
                    maiorprot = protAtual
                protAtual = ""
            else:
                if len(protAtual) > 0 or aa == "M":
                    protAtual += aa
        return MySeq(maiorprot, "protein")        

    def maiorProteinaER (self) -> str:
        """
        Função devolve a maior proteina obtida a partir da sequência, utilizando para isso expressões regulares

        """
        import re
        if (self.tipo != "protein"): return None
        mos = re.finditer("M[^_]*_", self.seq)
        sizem = 0
        lprot = ""
        for x in mos:
            ini = x.span()[0]
            fin = x.span()[1]
            s = fin - ini + 1
            if s > sizem:
                lprot = x.group()
                sizem = s
        return MySeq(lprot, "protein")    
    
    def todasProteinas(self) -> str:
        """
        Construí uma lista com todas as proteínas possíveis de serem obtidas a partir da sequência

        """
        if (self.tipo != "protein"):
            return None
        seqAA = self.seq
        protsAtuais = []
        proteinas = []
        for aa in seqAA:
            if aa == "_":
                if protsAtuais:
                    for p in protsAtuais:
                        proteinas.append(MySeq(p, "protein"))
                    protsAtuais = []
            else:
                if aa == "M":
                    protsAtuais.append("")
                for i in range(len(protsAtuais)):
                    protsAtuais[i] += aa

        return proteinas

    def maiorProteinaORFs (self) -> str:
        """
        Funçâo vai buscar a maior proteina que esteja presente numa das 6 ORF's

        """
        if (self.tipo != "dna"):
            return None
        larg = MySeq("","protein") 
        for orf in self.orfs():
            prot = orf.maiorProteinaER() 
            if len(prot.seq)>len(larg.seq): 
                larg = prot 
        return larg

