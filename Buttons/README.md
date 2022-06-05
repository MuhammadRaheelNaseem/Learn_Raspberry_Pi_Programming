<h1 class='jumbotron alert-info'>2.) Buttons Codes</h1>

# `Circuit Diagram`

![image](https://user-images.githubusercontent.com/63813881/172048874-8674a6d7-4cca-4548-840e-87ead438b082.png)

# `Code: 1`
## Check if a Button `.is_pressed:`
<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Button</span>

<span class="n">button</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">button</span><span class="o">.</span><span class="n">is_pressed</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Button is pressed"</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Button is not pressed"</span><span class="p">)</span>
</pre>


# `Code: 2`
## Wait for a button to be pressed before continuing: -> `.wait_for_press()`
<div class="highlight-python3 notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Button</span>

<span class="n">button</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="n">button</span><span class="o">.</span><span class="n">wait_for_press</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"You have press the button"</span><span class="p">)</span>

</pre></div>
</div>

# `Code: 3`
## Wait for a button to be pressed before continuing: -> `.wait_for_release()`
<div class="highlight-python3 notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Button</span>

<span class="n">button</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="n">button</span><span class="o">.</span><span class="n">wait_for_press</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"You have press the button"</span><span class="p">)</span>

<span class="n">button</span><span class="o">.</span><span class="n">wait_for_release</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"you have release the Button"</span><span class="p">)</span>

</pre></div>
</div>

# `Code: 4`
## Run a function every time the button is pressed: -> `.when_pressed`
<div class="highlight-python3 notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Button</span>
<span class="kn">from</span> <span class="nn">signal</span> <span class="kn">import</span> <span class="n">pause</span>

<span class="k">def</span> <span class="nf">say_hello</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Hello!"</span><span class="p">)</span>

<span class="n">button</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="hll"><span class="n">button</span><span class="o">.</span><span class="n">when_pressed</span> <span class="o">=</span> <span class="n">say_hello</span>
</span>


<span class="n">pause</span><span class="p">()</span>
</pre></div>
</div>

# `Code: 5`
## Run a function every time the button is pressed: -> `.when_released`
<div class="highlight-python3 notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Button</span>
<span class="kn">from</span> <span class="nn">signal</span> <span class="kn">import</span> <span class="n">pause</span>

<span class="k">def</span> <span class="nf">say_hello</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Hello!"</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">say_goodbye</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Goodbye RaspberryPi!"</span><span class="p">)</span>


<span class="n">button</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="hll"><span class="n">button</span><span class="o">.</span><span class="n">when_pressed</span> <span class="o">=</span> <span class="n">say_hello</span>
</span>
<span class="hll"><span class="n">button</span><span class="o">.</span><span class="n">when_released</span> <span class="o">=</span> <span class="n">say_goodbye</span>
</span>

<span class="n">pause</span><span class="p">()</span>
</pre></div>
</div>

# `Code: 6`

<div>
<pre data-trimmed="true" class="rainbow-show"><code data-language="python" class="rainbow rainbow-show"><span class="keyword">import</span> time
<span class="keyword">import</span> RPi.GPIO <span class="keyword">as</span> GPIO

<span class="comment"># Pins definitions</span>
btn_pin <span class="keyword operator">=</span> <span class="constant numeric">4</span>


<span class="comment"># Set up pins</span>
GPIO.<span class="function call">setmode</span>(GPIO.BCM)
GPIO.<span class="function call">setup</span>(btn_pin, GPIO.IN)

<span>GPIO.input(btn_pin)</span>
<span>print("Button is Pressed!)</span>
<span>GPIO.cleanup()</span>

</code></pre></div>

# `Code: 7`


<pre data-trimmed="true" class="rainbow-show"><code data-language="python" class="rainbow rainbow-show"><span class="keyword">import</span> time
<span class="keyword">import</span> RPi.GPIO <span class="keyword">as</span> GPIO

<span class="comment"># Pins definitions</span>
btn_pin <span class="keyword operator">=</span> <span class="constant numeric">4</span>


<span class="comment"># Set up pins</span>
GPIO.<span class="function call">setmode</span>(GPIO.BCM)
GPIO.<span class="function call">setup</span>(btn_pin, GPIO.IN)


<span class="comment"># If button is pushed, msg will print</span>
<span class="keyword">try</span>:
    <span class="keyword">while</span> <span class="constant language">True</span>:
        <span class="keyword">if</span> GPIO.<span class="support function python">input</span>(btn_pin):
            print("Button is pressed!")
        <span class="keyword">else</span>:
            print("Button is not pressed!")

<span class="comment"># When you press ctrl+c, this will be called</span>
<span class="keyword">finally</span>:
    GPIO.<span class="function call">cleanup</span>()
</code></pre>


## `Let's Control LED With Button`
## `Circuit Diagram:`
![image](https://user-images.githubusercontent.com/63813881/172048896-a3258a81-3748-4fa4-bff3-5a82219c3a7e.png)
# `Code: 8`
<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">LED</span><span class="p">,</span> <span class="n">Button</span>
<span class="kn">from</span> <span class="nn">signal</span> <span class="kn">import</span> <span class="n">pause</span>

<span class="n">led</span> <span class="o">=</span> <span class="n">LED</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>
<span class="n">button</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="n">button</span><span class="o">.</span><span class="n">when_pressed</span> <span class="o">=</span> <span class="n">led</span><span class="o">.</span><span class="n">on</span>
<span class="n">button</span><span class="o">.</span><span class="n">when_released</span> <span class="o">=</span> <span class="n">led</span><span class="o">.</span><span class="n">off</span>

<span class="n">pause</span><span class="p">()</span>
</pre>

# `Alternative way:`

# `Code: 9`
<div class="highlight-python3 notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">LED</span><span class="p">,</span> <span class="n">Button</span>
<span class="kn">from</span> <span class="nn">signal</span> <span class="kn">import</span> <span class="n">pause</span>

<span class="n">led</span> <span class="o">=</span> <span class="n">LED</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>
<span class="n">button</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="n">led</span><span class="o">.</span><span class="n">source</span> <span class="o">=</span> <span class="n">button</span>

<span class="n">pause</span><span class="p">()</span>
</pre></div>
</div>

# `Code: 10`
<pre class="language-python" tabindex="0"><code class="language-python"><span class="token keyword">from</span> gpiozero <span class="token keyword">import</span> LED<span class="token punctuation">,</span> Button
<span class="token keyword">from</span> time <span class="token keyword">import</span> sleep

led <span class="token operator">=</span> LED<span class="token punctuation">(</span><span class="token number">17</span><span class="token punctuation">)</span>
button <span class="token operator">=</span> Button<span class="token punctuation">(</span><span class="token number">2</span><span class="token punctuation">)</span>

<span class="token keyword">while</span> <span class="token boolean">True</span><span class="token punctuation">:</span>
    button<span class="token punctuation">.</span>wait_for_press<span class="token punctuation">(</span><span class="token punctuation">)</span>
    led<span class="token punctuation">.</span>toggle<span class="token punctuation">(</span><span class="token punctuation">)</span>
    sleep<span class="token punctuation">(</span><span class="token number">0.5</span><span class="token punctuation">)</span></code><br>
<span># led.toggle() switches the state of the LED from on to off, or off to on. Since this happens in a loop the LED will turn on and off each time the button is pressed.</span></pre>

# `Shutdown with Button`
# `Code: 11`
<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Button</span>
<span class="kn">from</span> <span class="nn">subprocess</span> <span class="kn">import</span> <span class="n">check_call</span>
<span class="kn">from</span> <span class="nn">signal</span> <span class="kn">import</span> <span class="n">pause</span>

<span class="k">def</span> <span class="nf">shutdown</span><span class="p">():</span>
    <span class="n">check_call</span><span class="p">([</span><span class="s1">'sudo'</span><span class="p">,</span> <span class="s1">'poweroff'</span><span class="p">])</span>

<span class="n">shutdown_btn</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">17</span><span class="p">,</span> <span class="n">hold_time</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">shutdown_btn</span><span class="o">.</span><span class="n">when_held</span> <span class="o">=</span> <span class="n">shutdown</span>

<span class="n">pause</span><span class="p">()</span>
</pre>

## `LEDBarGraph:`
## `Circuit Diagram:`
![image](https://user-images.githubusercontent.com/63813881/172048924-944f4d0e-d318-46d8-87e8-8bcb1bfdbbe0.png)
# `Code: 12`
<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">LEDBoard</span>
<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>
<span class="kn">from</span> <span class="nn">signal</span> <span class="kn">import</span> <span class="n">pause</span>

<span class="n">leds</span> <span class="o">=</span> <span class="n">LEDBoard</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">13</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">26</span><span class="p">)</span>

<span class="n">leds</span><span class="o">.</span><span class="n">on</span><span class="p">()</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">leds</span><span class="o">.</span><span class="n">off</span><span class="p">()</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">leds</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">leds</span><span class="o">.</span><span class="n">blink</span><span class="p">()</span>

<span class="n">pause</span><span class="p">()</span>
</pre>

# `Code: 13`
<p>Note values are essentially rounded to account for the fact LEDs can only be on
or off when <code class="docutils literal notranslate"><span class="pre">pwm=False</span></code> (the default).</p>
<p>However, using <code class="xref py py-class docutils literal notranslate"><span class="pre">LEDBarGraph</span></code> with <code class="docutils literal notranslate"><span class="pre">pwm=True</span></code> allows more precise
values using LED brightness:</p>
<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">LEDBarGraph</span>
<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>
<span class="kn">from</span> <span class="nn">__future__</span> <span class="kn">import</span> <span class="n">division</span>  <span class="c1"># required for python 2</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">LEDBarGraph</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">13</span><span class="p">,</span> <span class="mi">19</span><span class="p">,</span> <span class="mi">26</span><span class="p">,</span> <span class="n">pwm</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="n">graph</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="mi">1</span><span class="o">/</span><span class="mi">10</span>  <span class="c1"># (0.5, 0, 0, 0, 0)</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">graph</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="mi">3</span><span class="o">/</span><span class="mi">10</span>  <span class="c1"># (1, 0.5, 0, 0, 0)</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">graph</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="o">-</span><span class="mi">3</span><span class="o">/</span><span class="mi">10</span>  <span class="c1"># (0, 0, 0, 0.5, 1)</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">graph</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="mi">9</span><span class="o">/</span><span class="mi">10</span>  <span class="c1"># (1, 1, 1, 1, 0.5)</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">graph</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="mi">95</span><span class="o">/</span><span class="mi">100</span>  <span class="c1"># (1, 1, 1, 1, 0.75)</span>
<span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</pre>

## `Reaction Game:`
## `Circuit Diagram:`
![image](https://user-images.githubusercontent.com/63813881/172048945-9610c20f-4ade-42b3-9cd0-c6b99bc9bea7.png)
# `Code: 14`
<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">Button</span><span class="p">,</span> <span class="n">LED</span>
<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>
<span class="kn">import</span> <span class="nn">random</span>

<span class="n">led</span> <span class="o">=</span> <span class="n">LED</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>

<span class="n">player_1</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<span class="n">player_2</span> <span class="o">=</span> <span class="n">Button</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>

<span class="n">time</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span>
<span class="n">sleep</span><span class="p">(</span><span class="n">time</span><span class="p">)</span>
<span class="n">led</span><span class="o">.</span><span class="n">on</span><span class="p">()</span>

<span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">player_1</span><span class="o">.</span><span class="n">is_pressed</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Player 1 wins!"</span><span class="p">)</span>
        <span class="k">break</span>
    <span class="k">if</span> <span class="n">player_2</span><span class="o">.</span><span class="n">is_pressed</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Player 2 wins!"</span><span class="p">)</span>
        <span class="k">break</span>

<span class="n">led</span><span class="o">.</span><span class="n">off</span><span class="p">()</span>
</pre>
