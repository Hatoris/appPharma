import re
from typing import List, NewType
from appPharma.pkg import ureg, Q_
from appPharma.wrapper import formater

units = re.compile(r"(\d+[,|.]*\d+\s*[a-zA-Z]*%*/*[\d+[,|.]*[a-zA-Z]*%*/*[\d+[,|.]*[a-zA-Z]*%*)")
split = re.compile(r"(\d+[.|,]*\d+)(?:\s*)(%*[a-zA-Z]*/*[a-zA-Z]*/*[a-zA-Z]*)")
split_unit = re.compile(r"([a-zA-Z]+)*")

infos = List[str]
split_infos = List[List[str]]

def extract_infos(texte : str) -> infos :
    return units.findall(texte)

def split_infos(infos) -> split_infos:
    return list(map(split.findall, infos))

def split_units(split_infos):
    result = []
    for infos in split_infos:
        base = []
        for info in infos:
            base.append([info[0], split_unit.findall(info[0])])
        result.append(base)
    return result


def pintify(infos) -> List[ureg]:
#    result = []
#    for infos in split_infos:
#        for info in infos:
#            element = info[0] + ureg(info[1])
#            result.append(element)
    replace = lambda x: x if "%" not in x else x.replace("%", "pct")        
    return list(map(Q_, map(replace, infos)))
   
  
 
 