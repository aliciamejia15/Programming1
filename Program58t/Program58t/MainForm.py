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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
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
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 328)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(113, 34)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(157, 328)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(113, 34)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(310, 328)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(113, 34)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.LightCoral
		self._label1.Location = System.Drawing.Point(13, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(175, 34)
		self._label1.TabIndex = 3
		self._label1.Text = "Amount of the Purchase"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.LightCoral
		self._label2.Location = System.Drawing.Point(210, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(200, 34)
		self._label2.TabIndex = 4
		self._label2.Text = "Amount Received from the customer"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(30, 46)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(158, 24)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(230, 46)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(161, 24)
		self._textBox2.TabIndex = 6
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.LightCoral
		self._label3.Location = System.Drawing.Point(-18, 85)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(218, 34)
		self._label3.TabIndex = 7
		self._label3.Text = "Change Due"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.LightCoral
		self._label4.Location = System.Drawing.Point(-18, 122)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(218, 34)
		self._label4.TabIndex = 8
		self._label4.Text = "Dollars"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.LightCoral
		self._label5.Location = System.Drawing.Point(-18, 160)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(218, 34)
		self._label5.TabIndex = 9
		self._label5.Text = "Quarters"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.LightCoral
		self._label6.Location = System.Drawing.Point(-18, 200)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(218, 34)
		self._label6.TabIndex = 10
		self._label6.Text = "Dimes"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.LightCoral
		self._label7.Location = System.Drawing.Point(-19, 238)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(218, 34)
		self._label7.TabIndex = 11
		self._label7.Text = "Nickels"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label8.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(158, 238)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(234, 34)
		self._label8.TabIndex = 16
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label9.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(159, 200)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(234, 34)
		self._label9.TabIndex = 15
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label10.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(159, 160)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(234, 34)
		self._label10.TabIndex = 14
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label11.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(159, 122)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(234, 34)
		self._label11.TabIndex = 13
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label12.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(158, 85)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(235, 34)
		self._label12.TabIndex = 12
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label13.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(158, 278)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(234, 34)
		self._label13.TabIndex = 18
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label14
		# 
		self._label14.Font = System.Drawing.Font("Modern No. 20", 11.249999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.Color.LightCoral
		self._label14.Location = System.Drawing.Point(-18, 278)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(218, 34)
		self._label14.TabIndex = 17
		self._label14.Text = "Pennies"
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(438, 381)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.ForeColor = System.Drawing.Color.LightCoral
		self.Name = "MainForm"
		self.Text = "Program58t"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		
		Price = float(self._textBox1.Text)
		Money = float(self._textBox2.Text)
		
		changet = Money-Price
		
		self._label12.Text=" " + str(changet)
		
		dollars = changet//1
		
		self._label11.Text=" " + str(dollars)
		
		quaters1 = changet-dollars
		
		quaters= quaters1//.25
		
		quatert = quaters*0.25
		
		self._label10.Text=" " + str(quaters)
		
		dimes1 = changet-(dollars+quatert)
		
		dimes = dimes1//.10
		
		dimest = dimes*0.10
		
		self._label9.Text=" " + str(dimes)
		
		nickels1 = changet-(dollars+quatert+dimest)
		
		nickels = nickels1//.05
		
		nickelst = nickels*.05
		
		self._label8.Text=" " + str(nickels)
		
		pennies1 = changet-(dollars+quatert+dimest+nickelst)
		
		pennies = pennies1//.01
		
		penniest = pennies*.01
		
		self._label13.Text=" " + str(pennies)
		
		

	def Button2Click(self, sender, e):
		self._label12.Text=" " 
		
		self._label11.Text=" " 
		
		self._label10.Text=" " 
		
		self._label9.Text=" " 
		
		self._label8.Text=" " 
		
		self._label13.Text=" " 
		
		self._textBox1.Text=" " 
		
		self._textBox2.Text=" " 

	def Button3Click(self, sender, e):
		Application.Exit()
		