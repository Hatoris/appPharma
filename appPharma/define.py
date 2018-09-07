# module to in help use of function 

# list of function and there call

funcDic = {
	            'clairanceC' :    
	"""this function Calcul clairance of patient require parameters :  
	  |      - age : integer (58)     
	  |     - weight : string ('75kg') 
        - creatine serique : string ('140umol/l')
        optional parameters :
        - F : boolean (F = True) [F = False] *specify sex
        - min : boolean (min = True) [min = False] *specify if you want results in minute
        - size : string (size = '180cm') [size = False] *specify size if patient is above 80 year or bmi > 30"""
	            } 




def define(func):
    """ this function return a docstring of others function"""
    return funcDic[func]