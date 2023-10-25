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
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(4, 71)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(125, 38)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(137, 71)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(125, 38)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(270, 71)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(125, 38)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(187, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Sum of Multiples of 3"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightCyan
		self._label2.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(215, 29)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(120, 23)
		self._label2.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSkyBlue
		self.ClientSize = System.Drawing.Size(395, 121)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pro152a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		pass