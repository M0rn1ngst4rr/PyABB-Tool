import re
from os import listdir, path, makedirs
from classes import pointClass

def getFiles(file_Path:str):
    mod_Files = []
    files = [f for f in listdir(file_Path) if path.isfile(path.join(file_Path, f))]
    for f in files:
        if f.endswith(".mod"):
            mod_Files.append(f)
    return mod_Files

def readfile(file_path:str):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

def getPoints(lines:list[str]):
    pattern = "Move"
    pattern2 = r"[O][F][F][S]"
    pattern3 = r"pinpos"
    pattern4 = r"pKG"
    pattern5 = r"pSuchPos"
    points = list[str]()
    for line in lines:
        # file deepcode ignore change_to_is: <please specify a reason of ignoring this>
        if re.search(pattern, line, re.IGNORECASE) != None:
            test1 = re.search(pattern2, line, re.IGNORECASE)
            test2 = re.search(pattern3, line, re.IGNORECASE)
            test3 = re.search(pattern4, line, re.IGNORECASE)
            test4 = re.search(pattern5, line, re.IGNORECASE)
            if test1 == None and test2 == None and test3 == None and test4 == None:
                # trim spaces at the start
                line = line.strip()
                # get after space
                splitted = line.split(" ")
                name = splitted[1].split(",")[0]
                if not points.__contains__(name):
                    points.append(name) 
    return points

def getCoordiantes(lines:list[str]):
    pattern = "LOCAL CONST robtarget"
    pattern2 = "LOCAL VAR robtarget"
    pattern3 = r"pKG"
    coordianteslist = list[pointClass]()
    for line in lines:
        if re.search(pattern, line, re.IGNORECASE) != None:
            # trim spaces at the start
            line = line.strip()
            spacesplited = line.split(" ")
            name = spacesplited[3].split(":")[0]
            coords = spacesplited[3].split(":")[1].replace("=","")
            point = pointClass()
            point.name = name
            point.coordinates = coords
            coordianteslist.append(point)
        elif re.search(pattern2, line, re.IGNORECASE) != None:
            # trim spaces at the start
            line = line.strip()
            spacesplited = line.split(" ")
            if re.search(pattern3, line, re.IGNORECASE) != None:
                name = spacesplited[3].split(";")[0]
                coords = ""
                try:
                    if len(spacesplited[3].split(":")) >= 3:
                        coords = spacesplited[3].split(":")[1].replace("=","")
                except:
                    pass
            else:
                name = spacesplited[3].split(":")[0]
                coords = spacesplited[3].split(":")[1]
            point = pointClass()
            point.name = name
            point.coordinates = coords
            point.prename = "LOCAL VAR robtarget"
            coordianteslist.append(point)
    return coordianteslist

def getProcessPoints(lines:list[str]):
    # SM, KE, CZ, KL, KE, RE, SearchLine, Off, pInPos, Move, MS, pKG, pSuchPos
    pattern = r"[N|C|K|S|M][Z|E|M|S][_][P|L][T|I][P|N]"
    pattern2 = r"Move"
    pattern3 = r"[S][e][a][r][c][h][L][I][N][_][M]"
    pattern4 = r"[O][f|F][f|F]"
    pattern5 = r"pInPos"
    pattern6 = r"[K][L][_][P|L][T|I][P|N]"
    pattern7 = r"[R][E][_][P|L][T|I][P|N]"
    pattern8 = r"pKG"
    pattern9= r"pSuchPos"
    points = list[str]()
    for line in lines:
        if re.search(pattern, line, re.IGNORECASE) != None:
            # trim spaces at the start
            line = line.strip()
            # get after space
            splitted = line.split(" ")
            name = splitted[1].split(",")[0].split("\\")[0]
            if not points.__contains__(name):
                    points.append(name)
        elif re.search(pattern2, line, re.IGNORECASE) != None:
            test = re.search(pattern4, line, re.IGNORECASE)
            test2 = re.search(pattern5, line, re.IGNORECASE)
            test3 = re.search(pattern8, line, re.IGNORECASE)
            if test != None:
                # trim spaces at the start
                line = line.strip()
                # get after space
                splitted = line.split(" ")
                name = splitted[1].split(",")[0].split("(")[1].split("\\")[0]
                if not points.__contains__(name):
                    points.append(name) 
            # file deepcode ignore IdenticalBranches: <please specify a reason of ignoring this>
            elif test2 != None:
                # trim spaces at the start
                line = line.strip()
                # get after space
                splitted = line.split(" ")
                name = splitted[1].split(",")[0].split("\\")[0]
                if not points.__contains__(name):
                    points.append(name) 
            elif test3 != None:
                # trim spaces at the start
                line = line.strip()
                # get after space
                splitted = line.split(" ")
                name = splitted[1].split(",")[0].split("\\")[0]
                if not points.__contains__(name):
                    points.append(name) 
        elif re.search(pattern3, line, re.IGNORECASE) != None:
            # trim spaces at the start
            line = line.strip()
            # get after space
            splitted = line.split(" ")
            name = splitted[1].split(",")[0].split("\\")[0]
            if not points.__contains__(name):
                    points.append(name)
        elif re.search(pattern6, line, re.IGNORECASE):
            # trim spaces at the start
            line = line.strip()
            # get after space
            try:
                splitted = line.split(" ")
                test123 = splitted[1]
            except:
                splitted = line.split(",")
            name = splitted[1].split(",")[0].split("\\")[0]
            if not points.__contains__(name):
                    points.append(name)
        elif re.search(pattern7, line, re.IGNORECASE) != None:
            # trim spaces at the start
            line = line.strip()
            # get after space
            splitted = line.split(" ")
            # check if it has \start \end else do normal
            if len(splitted) > 1:
                name = splitted[1].split(",")[0].split("\\")[0]
                if not points.__contains__(name):
                    points.append(name)
            else:
                splitted2 = line.split(",")
                name = splitted2[1]
                if not points.__contains__(name):
                    points.append(name)
        elif re.search(pattern8, line, re.IGNORECASE) != None:
            # trim spaces at the start
            line = line.strip()
            # get after space
            splitted = line.split(" ")
            # check if it has \start \end else do normal
            if len(splitted) > 1:
                name = splitted[1].split(",")[0].split("\\")[0]
                if not points.__contains__(name):
                    points.append(name)
        elif re.search(pattern9, line, re.IGNORECASE) != None:
            # trim spaces at the start
            line = line.strip()
            # get after space
            splitted = line.split(" ")
            # check if it has \start \end else do normal
            if len(splitted) > 1:
                name = splitted[1].split(",")[0].split("\\")[0]
                if not points.__contains__(name):
                    points.append(name)
            else:
                splitted2 = line.split(",")
                name = splitted2[1]
                if not points.__contains__(name):
                    points.append(name)
    return points

def findUnused(p_points:list[str], r_points:list[str], coords:list[pointClass]):
    unused = list[str]()
    for coord in coords:
        found = False
        for p in p_points:
            if coord.name == p:
                found = True
                break
        for p in r_points:
            if coord.name == p:
                found = True
                break
        if not found:
            unused.append(coord.name)
    return unused

def cleanup(org_file:list[str], unused:list[str]):
    new_file = list[str]()
    for line in org_file:
        found = False
        for p in unused:
            if line.__contains__(p):
                found = True
        if not found:
            new_file.append(line)
    return new_file

def renameRPoints(lines:list[str], r_points:list[str], pre="x", step=10, start=10):
    file1 = lines
    p_number = start
    for point in r_points:
        p_name_new = f'{pre}{p_number}'
        for i, line in enumerate(file1):
            pattern = rf'{point}[:|,]'
            if re.search(pattern, line) != None:
                file1[i] = line.replace(point, p_name_new)
        p_number += step   
    return file1

def sort(file:list[str], p_declare:str, r_declare:str, p_points:list[str], r_points:list[str], coordiantes:list[pointClass]):
    new_file = list[str]()
    start_line = 0
    stop_line = 0
    start_pattern = r'[!][*]'
    stop_pattern = r'[p|!][r|#]'
    f_done = False
    r_done = False
    for i, line in enumerate(file):
        if bool(re.search(start_pattern, line, re.IGNORECASE)):
            if start_line == 0:
                start_line = i
        if bool(re.search(stop_pattern, line, re.IGNORECASE)):
            if stop_line == 0:
                stop_line = i - 1
                break
    for i, line in enumerate(file):
        if i >= start_line and i <= stop_line:
            if f_done == False:
                for l in p_declare:
                    new_file.append(l)
                for p in p_points:
                    for coord in coordiantes:
                        if bool(re.fullmatch(p, coord.name, re.IGNORECASE)):
                            if coord.coordinates != "":
                                new_file.append(f'{coord.spaces}{coord.prename} {coord.name}:={coord.coordinates}\n')
                            else:
                                new_file.append(f'{coord.spaces}{coord.prename} {coord.name};\n')
                            break
                new_file.append("\n")
                f_done = True
            elif r_done == False:
                for l in r_declare:
                    new_file.append(l)
                for r in r_points:
                    for coord in coordiantes:
                        if bool(re.fullmatch(r, coord.name, re.IGNORECASE)):
                            new_file.append(f'{coord.spaces}{coord.prename} {coord.name}:={coord.coordinates}\n')
                            break
                new_file.append("\n")
                r_done = True
        else:
            new_file.append(line)
    return new_file

def writeNewFile(prepath:str, file_name:str, lines:list[str]):
    pre = f"{prepath}/new/"
    try:
        makedirs(pre)
    except:
        pass
    file = path.join(pre, file_name)
    with open(file, 'w') as f:
        f.writelines(lines)