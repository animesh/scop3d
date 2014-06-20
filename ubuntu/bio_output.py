__author__ = 'stijn'
import wx
import wx.xrc
import wx.richtext
from Bio import motifs
from bio_retrieve_fasta import output2
from bio_retrieve_fasta import output3
from bio_retrieve_fasta import output4
from bio_blast_pdb_fasta import project_dir
from bio_retrieve_fasta import project_name
from bio_blast_pdb_fasta import spacer
from bio_parse_pdb_fasta import consensus
consensus = consensus
file_info = open(project_dir + spacer + "info.txt", "r")
if output3 == 1:
    file_abundance=open(project_dir + spacer + "myOutfile_abundance.pdb", "r")
    abundance = "Lines of pdb containing C-alpha coordinates and entropy: \n"
    for line in file_abundance:
        if line.startswith("ATOM") and "CA" in line:
            abundance += line

if output4 == 1:
    file_amount=open(project_dir + spacer + "myOutfile_amount.pdb", "r")
    amount = "Lines of pdb containing C-alpha coordinates and number of different AA: \n"
    for line in file_amount:
        if line.startswith("ATOM") and "CA" in line:
            amount += line
info = file_info.read()

from Bio import SeqIO
alignmentid = "record id:"
alignmentseq = "record sequence:"
instances = []
for record in SeqIO.parse(open(project_dir + spacer + "alignments" + spacer +"alignment_" + project_name + ".clw"), "clustal") :
    alignmentid += "\n" + record.id
    alignmentseq += "\n" + record.seq

class Scop3D ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Scop3D - Output", pos = wx.DefaultPosition, size = wx.Size( 569,423 ), style = wx.DEFAULT_FRAME_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.notebook_1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.notebook_1_pane_1 = wx.Panel( self.notebook_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_richText1 = wx.richtext.RichTextCtrl( self.notebook_1_pane_1, wx.ID_ANY, info, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gSizer2.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )


		self.notebook_1_pane_1.SetSizer( gSizer2 )
		self.notebook_1_pane_1.Layout()
		gSizer2.Fit( self.notebook_1_pane_1 )
		self.notebook_1.AddPage( self.notebook_1_pane_1, u"project", True )

		self.notebook_1_pane_2 = wx.Panel( self.notebook_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_richText6 = wx.TextCtrl( self.notebook_1_pane_2, wx.ID_ANY, str(alignmentid) , wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.m_richText6.SetMinSize( wx.Size( 200,-1 ) )
		self.m_richText6.SetMaxSize( wx.Size( 300,-1 ) )

		gbSizer2.Add( self.m_richText6, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_richText71 = wx.TextCtrl( self.notebook_1_pane_2, wx.ID_ANY, "   " + str(alignmentseq) + "   ", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		# self.m_richText71.SetMinSize( wx.Size( 1,-1 ) )
		gbSizer2.Add( self.m_richText71, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		gbSizer2.AddGrowableRow( 0 )
		gbSizer2.AddGrowableCol(1)
		# gbSizer2.AddGrowableRow( 5 )
		self.notebook_1_pane_2.SetSizer( gbSizer2 )
		self.notebook_1_pane_2.Layout()
		gbSizer2.Fit( self.notebook_1_pane_2 )
		self.notebook_1.AddPage( self.notebook_1_pane_2, u"alignment", False )

		if output3 ==1:
		    self.notebook_1_pane_3 = wx.Panel( self.notebook_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		    gSizer4 = wx.GridSizer( 0, 1, 0, 0 )


		    self.m_richText3 = wx.richtext.RichTextCtrl( self.notebook_1_pane_3, wx.ID_ANY, str(abundance), wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		    gSizer4.Add( self.m_richText3, 1, wx.EXPAND |wx.ALL, 5 )


		    self.notebook_1_pane_3.SetSizer( gSizer4 )
		    self.notebook_1_pane_3.Layout()
		    gSizer4.Fit( self.notebook_1_pane_3 )
		    self.notebook_1.AddPage( self.notebook_1_pane_3, u"pdb_procent", False )
		if output4 == 1:
		    self.notebook_1_pane_4 = wx.Panel( self.notebook_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		    gSizer5 = wx.GridSizer( 0, 1, 0, 0 )

		    self.m_richText4 = wx.richtext.RichTextCtrl( self.notebook_1_pane_4, wx.ID_ANY, str(amount), wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		    gSizer5.Add( self.m_richText4, 1, wx.EXPAND |wx.ALL, 5 )


		    self.notebook_1_pane_4.SetSizer( gSizer5 )
		    self.notebook_1_pane_4.Layout()
		    gSizer5.Fit( self.notebook_1_pane_4 )
		    self.notebook_1.AddPage( self.notebook_1_pane_4, u"pdb_amount", False )
		if output2 == 1:
		    self.notebook_1_pane_5 = wx.ScrolledWindow( self.notebook_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		    self.notebook_1_pane_5.SetScrollRate( 5, 5 )
		    gSizer6 = wx.GridSizer(0, 1, 0, 0)

		    self.png = wx.Image(project_dir + spacer + "sequence_logo.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		    self.m_bitmap2 = wx.StaticBitmap(self.notebook_1_pane_5, -1, self.png, (10, 5), (self.png.GetWidth(), self.png.GetHeight()))
		    gSizer6.Add( self.m_bitmap2, 0, wx.ALL, 5 )
		    self.notebook_1_pane_5.SetSizer( gSizer6)
		    self.notebook_1_pane_5.Layout()
		    gSizer6.Fit( self.notebook_1_pane_5)
		    self.notebook_1.AddPage( self.notebook_1_pane_5, u"seq_logo", False )
		# self.notebook_1_pane_6 = wx.Panel( self.notebook_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		# self.notebook_1.AddPage( self.notebook_1_pane_6, u"6", False )
		# self.notebook_1_pane_7 = wx.Panel( self.notebook_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		# self.notebook_1.AddPage( self.notebook_1_pane_7, u"7", False )
		# self.notebook_1_pane_8 = wx.Panel( self.notebook_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		# self.notebook_1.AddPage( self.notebook_1_pane_8, u"8", False )
		# self.notebook_1_pane_9 = wx.Panel( self.notebook_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		# self.notebook_1.AddPage( self.notebook_1_pane_9, u"9", False )

		bSizer1.Add( self.notebook_1, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

	def __del__( self ):
		pass


def main():
    app = wx.App(0)
    MainApp = Scop3D(None)
    MainApp.Show()
    MainApp.Maximize()
    app.MainLoop()

main()