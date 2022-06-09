<div class='jumbotron alert-info'><h1>3.) Buzzer</h1>
    <h2>Using a buzzer</h2>
    <p>There are two main types of buzzer: active and passive.</p>

<p>A passive buzzer emits a tone when a voltage is applied across it. It also requires a specific signal to generate a variety of tones. The active buzzers are a lot simpler to use, so these are covered here.

Connecting a buzzer
An active buzzer can be connected just like an LED, but as they are a little more robust, you won’t be needing a resistor to protect them.</p>

<p>Set up the circuit as shown below:</p>

</div>

## `Circuit Diagram:`
![image](https://user-images.githubusercontent.com/63813881/172768030-2de47528-19eb-43cf-903e-a94824decd8e.png)


# `Code: 1`

<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Buzzer</span>
<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>

<span class="n">buz</span> <span class="o">=</span> <span class="n">Buzzer</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>

<span class="n">buz</span><span class="o">.</span><span class="n">on</span><span class="p">()</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">buz</span><span class="o">.</span><span class="n">off</span><span class="p">()</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>

<!-- <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="n">led</span><span class="o">.</span><span class="n">on</span><span class="p">()</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">led</span><span class="o">.</span><span class="n">off</span><span class="p">()</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> -->
</pre>

# `Code: 2`

<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Buzzer</span>
<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>

<span class="n">buz</span> <span class="o">=</span> <span class="n">Buzzer</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>

<span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="n">buz</span><span class="o">.</span><span class="n">on</span><span class="p">()</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">buz</span><span class="o">.</span><span class="n">off</span><span class="p">()</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</pre>

# `Code: 3`

<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Buzzer</span>
<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>

<span class="n">buz</span> <span class="o">=</span> <span class="n">Buzzer</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>

<code class="language-python"><span class="token keyword">while</span> <span class="token boolean">True</span><span class="token punctuation">:</span>
    buzzer<span class="token punctuation">.</span>beep<span class="token punctuation">(</span><span class="token punctuation">)</span></code></pre>

# `Code: 4`

<pre class="wp-block-preformatted font:courier-new lang:python decode:true">import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER= 23
buzzState = False
GPIO.setup(BUZZER, GPIO.OUT)
while True:
    buzzState = not buzzState
    GPIO.output(BUZZER, buzzState)
    time.sleep(1)</pre>
    
# `Code: 5`
<pre>
#Libraries
import RPi.GPIO as GPIO
from time import sleep
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=23 
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
while True:
    GPIO.output(buzzer,GPIO.HIGH)
    print ("Beep")
    sleep(0.5) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    print ("No Beep")
    sleep(0.5)
</pre>

# `Generating Morse Code Sound`
## `First Create JSON file "codes.json" then copy this and saved!`
<pre> {"a" : "._", "b" : "_...", "c" : "_._.", "d" : "_..", "e" : ".", "f" : ".._.", "g" : "__.", "h" : "....", 
"i" : "..", "j" : ".___", "k" : "_._", "l" : "._..", "m" : "__", "n" : "_.", "o" : "___", "p" : ".__.",
"q" : "__._", "r" : "._.", "s" : "...", "t" : "_", "u" : ".._", "v" : "..._", "w" : ".__", "x" : "_.._",
"y" : "_.__", "z" : "__.."
}
</pre>

# `Code: 6`

<pre>
import RPi.GPIO as GPIO
import time
import json

# default dot and dash times (seconds)
DOTTIME = 0.0375
DASHTIME = 0.1125

# setup GPIO and make GPIO 23 output
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=23
GPIO.setup(buzzer, GPIO.OUT)

def playDotSound():
	"""
	Plays the dot sound according to specified time
	"""
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(DOTTIME)
	GPIO.output(buzzer, GPIO.LOW)
	
def playDashSound():
	"""
	Plays the dash sound accord to specified time
	"""
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(DASHTIME)
	GPIO.output(buzzer, GPIO.LOW)

def waitDot():
	"""
	Waits the specified dot sound time
	"""
	time.sleep(DOTTIME)

def waitDash():
	"""
	Waits the specified dash sound time
	"""
	time.sleep(DASHTIME)

def decodeMorse(file):
	"""
	Decodes the morse json file (eg codes.json)
	"""
	with open(file, 'r') as f:
		morseDict = json.load(f)
	return morseDict

def playMorseLetter(letter):
	"""
	Plays the morse code of a letter
	"""
	codes = list(letter)
	for code in codes:
		if code == '.':
			playDotSound()
		elif code == '_':
			playDashSound()
		waitDash()

def playMorseWord(word):
	"""
	Plays the morse code of a word
	"""
	for letter in word:
		playMorseLetter(letter)
		print(letter + " ")
	waitDash()
	waitDash()
	waitDot()

def transcodeWord(word, morseDict):
	"""
	Converts a alphabetic letter to morse code string value
	"""
	morseList = []
	for letter in word:
		morseLetter = morseDict.get(letter.lower())
		morseList.append(morseLetter)
	return morseList

def playMorseSentence(sentence):
	"""
	Plays an alphabetic sentence in morse code
	"""
	alphabetWords = sentence.split()
	morseDict = decodeMorse('codes.json')
	for word in alphabetWords:
		morseWord = transcodeWord(word, morseDict)	
		playMorseWord(morseWord)

if __name__ == '__main__':
	sentence = str(input("Please type your sentence to be converted to morse code: "))
	print(sentence)
	playMorseSentence(sentence)
	GPIO.cleanup()	
</pre>
