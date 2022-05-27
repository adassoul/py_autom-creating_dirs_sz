à partir du fichier api-urlCalls.json (de son architecture spécifique)
accède à la clé "response"
et crée un dir correspondant à sa valeur correspondante

0 : create
1 : delete all files
2 : delte all files then create

if dir exists, doesn't recreate it and continues to check/create subdirs/next dirs 
    [log] prints "existing folder. Didn't override it. Continuing to subfolder/next folder"
if file exists, doesn't overwrite it 
    [log] prints "existing file. Didn't overwrite it"
