import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(251, 209)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(134, 38)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(251, 253)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(134, 37)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CornflowerBlue
		self._label1.Font = System.Drawing.Font("Monotype Corsiva", 21.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(39, 60)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(279, 100)
		self._label1.TabIndex = 2
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.CornflowerBlue
		self.ClientSize = System.Drawing.Size(410, 314)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "FavoriteQoute"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text="If I'm going to die, I'd like to actually live first."

	def Button2Click(self, sender, e):
		self._label1.Text=" "