#!/usr/bin/env python
import wx
import random

adjectives=[]
locations=[]


class appender(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Theme Wizard', size=(200,300))
        
        self.panel=wx.Panel(self)
        
        
        adjective=wx.Button(self.panel,label='Add Ajective',pos=(10,10),size=(130,60))
        location=wx.Button(self.panel,label='Add Location',pos=(10,100),size=(130,60))
        generate=wx.Button(self.panel,label='Generate Theme',pos=(10,190),size=(130,60))
        
        self.Bind(wx.EVT_BUTTON, self.addajective, adjective)
        self.Bind(wx.EVT_BUTTON, self.addlocation, location)
        self.Bind(wx.EVT_BUTTON, self.generatetheme, generate)
        
        self.Bind(wx.EVT_CLOSE, self.closewindow)
    
    def addajective(self, event):
        box1=wx.TextEntryDialog(None,'Enter adjective')
        if box1.ShowModal()==wx.ID_OK:
            adjectives.append(box1.GetValue())
    
    def addlocation(self, event):
        box2=wx.TextEntryDialog(None, 'Enter location')
        if box2.ShowModal()==wx.ID_OK:
            locations.append(box2.GetValue())
            
    def generatetheme(self, event):
        font=wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD, underline=True, faceName="", encoding=wx.FONTENCODING_DEFAULT)

        yourtheme = random.choice(adjectives) + ' ' + random.choice(locations)
        output=wx.StaticText(self.panel,-1, yourtheme,(10,250),(260,-1),wx.ALIGN_CENTER)
        output.SetFont(font)
    
    
    def closewindow(self, event):
        self.Destroy()

if __name__=='__main__':
    app = wx.App(False)
    frame = appender(parent=None,id=-1)
    frame.Show()
    app.MainLoop()