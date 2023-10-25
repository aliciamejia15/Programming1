import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._label17 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label18 = System.Windows.Forms.Label()
		self._label19 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSkyBlue
		self._label1.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(142, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter KWH used"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Azure
		self._textBox1.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(146, 10)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 23)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSkyBlue
		self._label2.Font = System.Drawing.Font("Verdana", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(56, 51)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(201, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "C O M P S C I  Electric"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSkyBlue
		self._label3.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(13, 83)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(286, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSkyBlue
		self._label4.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(13, 102)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(129, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "Kilowatts Used"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSkyBlue
		self._label5.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(199, 102)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 5
		self._label5.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightSkyBlue
		self._label6.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 153)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(113, 23)
		self._label6.TabIndex = 6
		self._label6.Text = "Base Rate"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightSkyBlue
		self._label7.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(13, 117)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(286, 23)
		self._label7.TabIndex = 7
		self._label7.Text = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.LightSkyBlue
		self._label8.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(12, 180)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 8
		self._label8.Text = "Surcharge"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.LightSkyBlue
		self._label9.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(13, 203)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 9
		self._label9.Text = "Citytax"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.LightSkyBlue
		self._label10.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(13, 254)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(129, 23)
		self._label10.TabIndex = 10
		self._label10.Text = "Pay this amount"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.LightSkyBlue
		self._label11.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(12, 287)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(153, 23)
		self._label11.TabIndex = 11
		self._label11.Text = "After May 20th Pay"
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.LightSkyBlue
		self._label12.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(199, 153)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 12
		self._label12.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.LightSkyBlue
		self._label13.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(199, 176)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 13
		self._label13.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.LightSkyBlue
		self._label14.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(199, 199)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 14
		self._label14.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.LightSkyBlue
		self._label15.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(199, 254)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(100, 23)
		self._label15.TabIndex = 15
		self._label15.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.LightSkyBlue
		self._label16.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(199, 287)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(100, 23)
		self._label16.TabIndex = 16
		self._label16.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label17
		# 
		self._label17.BackColor = System.Drawing.Color.LightSkyBlue
		self._label17.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label17.Location = System.Drawing.Point(203, 213)
		self._label17.Name = "label17"
		self._label17.Size = System.Drawing.Size(100, 23)
		self._label17.TabIndex = 17
		self._label17.Text = "_________"
		self._label17.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold)
		self._button1.Location = System.Drawing.Point(5, 326)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(95, 24)
		self._button1.TabIndex = 18
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold)
		self._button2.Location = System.Drawing.Point(117, 326)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(81, 24)
		self._button2.TabIndex = 19
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Verdana", 9.75, System.Drawing.FontStyle.Bold)
		self._button3.Location = System.Drawing.Point(218, 326)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(81, 24)
		self._button3.TabIndex = 20
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label18
		# 
		self._label18.BackColor = System.Drawing.Color.LightSkyBlue
		self._label18.Font = System.Drawing.Font("Verdana", 9, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label18.Location = System.Drawing.Point(146, 153)
		self._label18.Name = "label18"
		self._label18.Size = System.Drawing.Size(82, 23)
		self._label18.TabIndex = 21
		self._label18.Text = "@ $ 0.0475"
		# 
		# label19
		# 
		self._label19.BackColor = System.Drawing.Color.LightSkyBlue
		self._label19.Font = System.Drawing.Font("Verdana", 9, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label19.Location = System.Drawing.Point(92, 151)
		self._label19.Name = "label19"
		self._label19.Size = System.Drawing.Size(51, 23)
		self._label19.TabIndex = 22
		self._label19.TextAlign = System.Drawing.ContentAlignment.TopRight
		self._label19.Click += self.Label19Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSkyBlue
		self.ClientSize = System.Drawing.Size(311, 362)
		self.Controls.Add(self._label19)
		self.Controls.Add(self._label18)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label17)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pro93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		
		Used = float(self._textBox1.Text)
		
		self._label19.Text=" " + str(Used)
		self._label5.Text=" " + str(Used)
		
		Bs = Used * 0.0475
		Bs = round(Bs,2)
		self._label12.Text=" $ " + str(Bs)
		
		
		Sur = (Bs * 10)/100
		Sur = round(Sur,2)
		self._label13.Text=" $ " + str(Sur)
		
		Ct = (Bs * 3)/100
		Ct = round(Ct,2)
		self._label14.Text=" $ " + str(Ct)
		
		Pay = Bs + Sur + Ct
		Pay = round(Pay,2)
		self._label15.Text=" $ " + str(Pay)
		
		Lt = (Pay * 4) / 100
		
		Late = Pay + Lt
		Late = round(Late,2)
		self._label16.Text=" $ " + str(Late)
		
	def Label19Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._label19.Text=" " 
		self._label5.Text=" "
		self._label12.Text=" $ " 
		self._label13.Text=" $ " 
		self._label14.Text=" $ " 
		self._label15.Text=" $ "
		self._label16.Text=" $ " 

	def Button3Click(self, sender, e):
		Application.Exit()