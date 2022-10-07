import maya.cmds as cmds
import xml.etree.ElementTree as ET


class PremierSequenceXMLToMaya(object):
        
    #constructor
    def __init__(self):
            
        self.window = "PremierSequenceXMLToMaya"
        self.title = "Premiere XML Sequence Importer"
        self.size = (400, 70)
            
        # close old window is open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)
            
        #create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        
        cmds.columnLayout(adjustableColumn = True)
        
        
        self.FilePath = cmds.textFieldGrp(label = 'File Path')
        
        
        self.CameraReference = cmds.textFieldGrp(label='Camere reference')
                
        self.CreateSequence = cmds.button(label = 'Apply', command = self.CreateSequence)

        
        #display new window
        cmds.showWindow()
        


    def CreateSequence(self, *args):
        
        CamRef = cmds.textFieldGrp(self.CameraReference, query = True, text = True)
        name = cmds.textFieldGrp(self.FilePath, query = True, text = True)
        tree = ET.parse(name)
        root = tree.getroot()

        shot = [0]

        s = root[0][4][0][2]
        

        for i in range(len(s) - 2):
            n = [s[i][1].text, s[i][5].text, s[i][6].text]
            if shot == [0]:
                shot = [n]
            else:
                shot.append(n)


        #
        for i in range(len(shot)):
            x = int(shot[i][1]) + 1
            shot[i][1] = int(shot[i][1])
            shot[i][2] = int(shot[i][2])
            shot[i][1] = x

        def Create_Shot(name, start, end, cam):
            cmds.shot(name, st=start, et=end, cc=cam, sst=start, set=end)
            
        #
        for i in range(len(shot)):
            cmds.duplicate(CamRef, name = shot[i][0])
            Create_Shot("shot", shot[i][1], shot[i][2], shot[i][0])
            
        
        

                
Window = PremierSequenceXMLToMaya()


print("PremierSequenceXMLToMaya Imported")