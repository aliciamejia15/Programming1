import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.WhiteSmoke
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(294, 226)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(153, 34)
		self._button1.TabIndex = 0
		self._button1.Text = "Go Cougars!"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Gainsboro
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._label1.Location = System.Drawing.Point(38, 51)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(325, 108)
		self._label1.TabIndex = 1
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.WhiteSmoke
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(294, 266)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(153, 36)
		self._button2.TabIndex = 2
		self._button2.Text = "Craig Rules!"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(476, 343)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "CraigRules"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text="Go Cougars!"

	def Button2Click(self, sender, e):
		self._label1.Text="Craig Rules!"