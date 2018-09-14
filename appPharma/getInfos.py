import re
from typing import List

units = re.compile(r"(\d+[,|.]*\d+\s*[a-zA-Z]*%*/*[\d+[,|.]*[a-zA-Z]*%*/*[\d+[,|.]*[a-zA-Z]*%*)")
split = re.compile(r"(\d+[.|,]*\d+)(?:\s*)(%*[a-zA-Z]*/*[a-zA-Z]*/*[a-zA-Z]*)")

def extract_infos(texte : str) -> List[str]:
    return units.findall(texte)

def split_infos(infos : List[str]) -> List[List[str]]:
    return list(map(split.findall, infos))