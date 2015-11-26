# Program to contain methods for reading and writing to files
# Will be a class that reads all the files when constructed

class FileHandler:
  # Constructor that reads in all the files
  def _init_(self):
    try:
      self.base = open("base.txt", "r")
      self.advanced = open("advanced.txt", "r")
      self.user = open("user.txt", "r")
    except IOError as e:
      print "File not found or given permission to read.", e

    extractFile(self, "base")
    extractFile(self, "advanced")
    exractFile(self, "user")
    
    self.base.close()
    self.advanced.close()
    self.user.close()

  # Method to extract info from file and store in lists
  def extractFile(self, fileType):
    if fileType == "base":
      f = self.base
    elif fileType = "advanced":
      f = self.advanced
    else
      f = self.user
    races = extractSection(self, races, f) 
    professions = extractSection(self, professions, f) 
    if fileType == "base":
      self.baseRaces = races
      self.baseProfessions = professions 
    elif fileType = "advanced":
      self.advancedRaces = races
      self.advancedProfessions = professions 
    else
      self.userRaces = races
      self.userProfessions = professions 
    


  # Method to read one section of a file in
  def extractSection(self, section, f):
    # Get past first line heading
    line = f.readline()
    line = f.readline()
    while line.find(";") == -1:
      line.split(",")
      section.append(line)
      line = f.readline()
    return section
    
    

  

  
      
    
    

  


    
