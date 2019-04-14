import os
import pickle
import datetime

class DirectoryToProcess:
    def __init__(self, id, name, parentID, parent, path):
        self._id = id
        self._name = name
        self._parentID = parentID
        self._parent = parent
        self._path = path[0:len(path)-1]
        self._results = LineCounts()

    def setTotalLineCount(self, count):
        self._results._totalLines = count
        
    def addToTotalLineCount(self, count):
        self._results._totalLines += count
    
    def getTotalLines(self):
        return self._results._totalLines
    
    def countProjectLines(self):
        for root, dirs, files in os.walk(self._path):
            for fileName in files:
                ext = os.path.splitext(fileName)[1]
                if isProgramFile(ext) != 0 and fileName != "sqlite3.c" and fileName != "sqlite3.h":
                    linesInFile = countLinesInFile(root, fileName)
    #                print "   " + fileName + " - ", res._totalLines
                    self.addToTotalLineCount(linesInFile) 

        print "Directory:" + self._path + " - ", self._results._totalLines
    
        return 0
      
class LineCounts:
    def __init__(self):
        self._totalLines = 0
        self._totalCommentLines = 0
        self._cppLines = 0
        self._cLines = 0
        self._hLines = 0
        self._csLines = 0
        self._xamlLines = 0
                    
def isProgramFile(ext):
    if ext == ".cpp" or ext == ".h" or ext == ".cs" or ext == ".c" or ext == ".xaml":
        return 1

    return 0
        
def countLinesInFile(dirPath, fileName):
    file = open(dirPath + "\\" + fileName, 'r')
    
    count = 0
    while file.readline() != "":
        count = count + 1
    
    return count

def loadData():
    fileState = open("state.dat", 'r')
    savedData = pickle.load(fileState)
    fileState.close()
    return savedData

def saveData(savedData):
    fileState = open("state.dat", 'w')
    pickle.dump(savedData, fileState)
    fileState.close()

def findProject(listProjRes, projID):
    for p in listProjRes:
        if p._id == projID:
            return p
        
    return None

def processListOfProjects(fileName):
    listProjectRes = []

    fileInputDir = open(fileName)
    listInputDirLines = fileInputDir.readlines()

    for inputDir in listInputDirLines:
        params = inputDir.split(' ', 3)
    
        id = params[0]
        name = params[1]
        parentID = params[2]
        parent = findProject(listProjectRes, parentID)
        path = params[3]
        
        dirToProcess = DirectoryToProcess(id, name, parentID, parent, path)
    
        dirToProcess.setTotalLineCount(0)
    
        listProjectRes.append(dirToProcess)

        if dirToProcess._parentID != "-1":
            dirToProcess.countProjectLines()
        
            for proj in listProjectRes:
                if proj._id == dirToProcess._parentID:
                    # zbrojiti na taj projekt
                    proj._results._totalLines += dirToProcess._results._totalLines

    return listProjectRes

def compareProjects(dirToProcess):
    return dirToProcess._results._totalLines

def printData(listProjectRes):
    print "TOP PROJECTS:" 
    sumTotal = 0       
    for proj in listProjectRes:
        if proj._parentID == "-1":
            print proj._name, " - ", proj._results._totalLines

            sumTotal += proj._results._totalLines
        
            listSub = []
            for subproj in listProjectRes:
                if subproj._parentID == proj._id:
                    listSub.append(subproj)
        
            listSub.sort(key=compareProjects, reverse=True)
        
            for subp in listSub:
                print "   {0:35} - ".format(subp._name),"{0:>6}".format(subp._results._totalLines)

    print "TOTAL LINES - ", sumTotal

def countTotalLine(listProjectRes):
    sumTotal = 0       
    for proj in listProjectRes:
        if proj._parentID == "-1":
            sumTotal += proj._results._totalLines
    
    return sumTotal

# Funkcionalnost iz glavnog programa
def analyze():
    listProjectRes = processListOfProjects('topXviewInputDirs.txt')
    printData(listProjectRes)

    currTime = datetime.datetime.now()

    savedData[currTime] = listProjectRes

    saveData(savedData)

def compareTime(projectTupleData):
    return projectTupleData[0]

def prepare_statistic():
    tmpList = []
    
    for s in list(savedData.keys()):
        pList = savedData[s]    
        totalLines = countTotalLine(pList)
        newTuple = (s, totalLines, pList)
        tmpList.append(newTuple)

    tmpList.sort(key = compareTime)
    
    return tmpList

    
def print_statistic():
    tmpList = prepare_statistic()
    
    for i in range ( len(tmpList) ):
        if i==0:
            print tmpList[i][0], tmpList[i][1]
        else:
            print tmpList[i][0], tmpList[i][1], tmpList[i][1] - tmpList[i-1][1]

def getChangesList(listProj1, listProj2):
    tmpList = []

    for proj1 in listProj1:
#        if proj1._parentID == "-1":
            projName = proj1._name
            
            for proj2 in listProj2:
                if proj1._id == proj2._id:
                    if proj1.getTotalLines() != proj2.getTotalLines():
                        newTuple = (projName, proj1._parentID, proj1.getTotalLines(), proj2.getTotalLines(), proj2.getTotalLines() - proj1.getTotalLines())
                        tmpList.append(newTuple)
        
    return tmpList

def show_changes():
    tmpList = prepare_statistic()

    for i in range ( len(tmpList) ):
        print
        print tmpList[i][0], tmpList[i][1]
        if i>0:
            listProj1 = tmpList[i-1][2]
            listProj2 = tmpList[i][2]
            
            listChanges = getChangesList(listProj1, listProj2)
    
            for diffTuple in listChanges:
                if diffTuple[1] == "-1":
                    print "    {0:25}". format(diffTuple[0]), " - {:>6}".format(diffTuple[4])
                else:
                    print "         {0:20}". format(diffTuple[0]), " - {:>6}".format(diffTuple[4])
                
 
 
# GLAVNI PROGRAM
savedData = loadData()

choice = -1

while choice != 0:
    print "Main menu:"
    print "1 - Print stat"
    print "2 - Analyze"
    print "3 - Show changes"
    print "4 - Save"
    print "0 - Quit"

    choice = input();

    if choice == 1:
        print_statistic()
    elif choice == 2:
        analyze()
    elif choice == 3:
        show_changes()
    elif choice == 4:
        saveData(savedData)

