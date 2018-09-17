import re
from typing import List, Tuple
from appPharma.pkg import ureg, Q_
from appPharma.wrapper import formater

UNITS = re.compile(r"(\d+[,|.]*\d+\s*[a-zA-Z]*%*/*[\d+[,|.]*[a-zA-Z]*%*/*[\d+[,|.]*[a-zA-Z]*%*)")
SPLIT = re.compile(r"(\d+[.|,]*\d+)(?:\s*)(%*[a-zA-Z]*/*[a-zA-Z]*(?:/*)[a-zA-Z]*)")
SPLIT_UNIT = re.compile(r"([a-zA-Z%]+)(/*)")
REPLACE = [(",", "."), ("%", "pct"), ("h", "hour")]

infos = List[str]
splited_infos = List[List[str]]
pinted = List[ureg]

def extract_infos(texte : str) -> infos :
    """find all unit given in the test
    Parameters
    --------------------
    texte : str
        texte to extract unit from
     Return
     ------------
     infos : List[str]
         list woth all elements that match unit regex definition
     Exemple
     --------------
     >>> extract_infos("bla bla bla 12mg, bla bla. Bla bla 2.5 mmol/L")
     ["12mg", "2.5 mmol/L"]
    """
    return UNITS.findall(texte)

def split_infos(infos) -> splited_infos:
    """split value and their unit foud with extract infos
   Parameters
    --------------------
    infos : List[str]
        info find in texte with extract_infos
     Return
     ------------
     split_infos : List[List[str]]
         return for given units, value and unut splited
    Exemple
    --------------
    >>> split_infos(["12mg", "2.5 mmol/L"])
    [["12", "mg"], ["2.5", "mmol/L"]]    
    """
    return list(map(SPLIT.findall, infos))

def pintify(infos) -> pinted:
    """return pint quantity from each unit in infos
    Parameters
    -------------------
    infos : List[str]
        info find in texte with extract_infos
     Return
     ------------
     pinted : List[ureg]
         list with all element as pint object
     Exemple
     --------------
    >>> printify(["12mg", "2.5 mmol/L"])
    [<Quantity(12, 'milligram')>,
    <Quantity(2.5, 'millimol/liter')>]
    
    """
    return list(map(ureg, map(replace_unreadable, infos)))

     
def replace_unreadable(info : str) -> str:
    """replece element that can't be read and transform by pint
    Parameters
    -------------------
    info : str
        string to evaluate
     Return
     -----------
     modify_info : str
         info is modify according definition
     Exemple
     --------------
     >>>replace_unreadable("12,5 mg/ml")
     12.5 mg/ml    
    """
    for repl in REPLACE:
        info = info.replace(*repl)
    return info
                    
        
  
 
 