import re
from typing import List

units = re.compile(r"(\d+[,|.]*\d+\s*[a-zA-Z]*%*/*[\d+[,|.]*[a-zA-Z]*%*/*[\d+[,|.]*[a-zA-Z]*%*)")

def extract_infos(texte : str) -> List[str]:
    return units.findall(texte)

