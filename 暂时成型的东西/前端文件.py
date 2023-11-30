#decoding=gbk
from tkinter import SEL
import wx
import wx.xrc
import socket
import time
def tongxinudpfasong(data):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localaddr = ("127.0.0.1",12345) 
    udp_socket.bind(localaddr)
    sendadd=("127.0.0.1",7788)
    udp_socket.connect(sendadd)
    udp_socket.send(data)
	
        
class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 379,321 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"请输入名称", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )

		mynameChoices = [ u"1", u"2", u"3", u"4", u"5", u"6", wx.EmptyString, wx.EmptyString ]
		self.myname= wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mynameChoices, 0 )
		self.myname.SetSelection( 5 )
		bSizer1.Add( self.myname
		, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"查找内容设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"选好后点击", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button3, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.SetMenuBar( self.m_menubar1 )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def m_button1OnButtonClick( self, event ):
		event.Skip()


	# Virtual event handlers, override them in your derived class
	def m_button1OnButtonClick( self, event ):
		event.Skip()







class mainWin(MyFrame1):
   def fi(self,event):
      neirong=self.m_textCtrl2.GetValue()
      choic=self.myname.GetStringSelection()
      tongxinudpfasong(str(choic+' '+neirong).encode('utf-8'))
       
   def solve1(self):
       self.Bind(wx.EVT_BUTTON,self.fi,self.m_button3)


if __name__ == '__main__':
    app = wx.App()
    main_win = mainWin(None)
    main_win.solve1()
    main_win.Show()
    app.MainLoop()
