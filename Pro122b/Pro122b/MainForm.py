import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Perpetua", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 18
		self._listBox1.Location = System.Drawing.Point(2, 0)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(321, 238)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Perpetua", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(3, 265)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 28)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Perpetua", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(114, 265)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 28)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Perpetua", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(223, 265)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 28)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightGray
		self.ClientSize = System.Drawing.Size(328, 306)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Pro122b"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Hours\tPay\t"
		self._listBox1.Items.Add(heading)
		
		for hours in range(1,40+1): 
			
			pay = hours*4.00
			msg = str(hours) +"\t" + str(pay) 
			self._listBox1.Items.Add(msg)
 