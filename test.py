import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask,send_from_directory



app = Flask(__name__)



def start():

        put_html('''<section data-toggle="wy-nav-shift" class="wy-nav-content-wrap">

      
      <nav class="wy-nav-top" aria-label="top navigation">
        
          <i data-toggle="wy-nav-top" class="fa fa-bars"></i>
          <a href="index.html">PyWebIO</a>
        
      </nav>


      <div class="wy-nav-content">
        
        <div class="rst-content">
        
          















<div role="navigation" aria-label="breadcrumbs navigation">

  <ul class="wy-breadcrumbs">
    
      <li><a href="index.html">Docs</a> »</li>
        
      <li><code class="docutils literal notranslate"><span class="pre">pywebio.platform</span></code> — Deploy applications</li>
    
    
      <li class="wy-breadcrumbs-aside">
        
            
            
              <a href="https://github.com/wang0618/PyWebIO/blob/doc/docs/platform.rst" class="fa fa-github"> Edit on GitHub</a>
            
          
        
      </li>
    
  </ul>

  
  <hr>
</div>
          <div role="main" class="document" itemscope="itemscope" itemtype="http://schema.org/Article">
           <div itemprop="articleBody">
            
  <div class="section" id="module-pywebio.platform">
<span id="pywebio-platform-deploy-applications"></span><h1><code class="docutils literal notranslate"><span class="pre">pywebio.platform</span></code> — Deploy applications<a class="headerlink" href="#module-pywebio.platform" title="Permalink to this headline">¶</a></h1>
<p>The <code class="docutils literal notranslate"><span class="pre">platform</span></code> module provides support for deploying PyWebIO applications in different ways.</p>
<div class="contents local topic" id="contents">
<ul class="simple">
<li><p><a class="reference internal" href="#directory-deploy" id="id1">Directory Deploy</a></p></li>
<li><p><a class="reference internal" href="#application-deploy" id="id2">Application Deploy</a></p>
<ul>
<li><p><a class="reference internal" href="#tornado-support" id="id3">Tornado support</a></p>
<ul>
<li><p><a class="reference internal" href="#websocket" id="id4">WebSocket</a></p></li>
<li><p><a class="reference internal" href="#http" id="id5">HTTP</a></p></li>
</ul>
</li>
<li><p><a class="reference internal" href="#flask-support" id="id6">Flask support</a></p></li>
<li><p><a class="reference internal" href="#django-support" id="id7">Django support</a></p></li>
<li><p><a class="reference internal" href="#aiohttp-support" id="id8">aiohttp support</a></p></li>
<li><p><a class="reference internal" href="#fastapi-starlette-support" id="id9">FastAPI/Starlette support</a></p></li>
</ul>
</li>
<li><p><a class="reference internal" href="#other" id="id10">Other</a></p></li>
</ul>
</div>
<div class="admonition seealso">
<p class="admonition-title">See also</p>
<ul class="simple">
<li><p><a class="reference internal" href="guide.html#server-and-script-mode"><span class="std std-ref">Use Guide: Server mode and Script mode</span></a></p></li>
<li><p><a class="reference internal" href="advanced.html#integration-web-framework"><span class="std std-ref">Advanced Topic: Integration with Web Framework</span></a></p></li>
</ul>
</div>
<div class="section" id="directory-deploy">
<span id="dir-deploy"></span><h2><a class="toc-backref" href="#id1">Directory Deploy</a><a class="headerlink" href="#directory-deploy" title="Permalink to this headline">¶</a></h2>
<p>You can use <code class="docutils literal notranslate"><span class="pre">path_deploy()</span></code> or <code class="docutils literal notranslate"><span class="pre">path_deploy_http()</span></code> to deploy the PyWebIO applications from a directory.
The python file under this directory need contain the <code class="docutils literal notranslate"><span class="pre">main</span></code> function to be seen as the PyWebIO application.
You can access the application by using the file path as the URL.</p>
<p>Note that users can’t view and access files or folders whose name begin with the underscore in this directory.</p>
<p>For example, given the following folder structure:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>.
├── A
│   └── a.py
├── B
│   └── b.py
└── c.py
</pre></div>
</div>
<p>All three python files contain <code class="docutils literal notranslate"><span class="pre">main</span></code> PyWebIO application function.</p>
<p>If you use this directory in <a class="reference internal" href="#pywebio.platform.path_deploy" title="pywebio.platform.path_deploy"><code class="xref py py-obj docutils literal notranslate"><span class="pre">path_deploy()</span></code></a>, you can access the PyWebIO application in
<code class="docutils literal notranslate"><span class="pre">b.py</span></code> by using URL <code class="docutils literal notranslate"><span class="pre">http://&lt;host&gt;:&lt;port&gt;/A/b</span></code>. And if the files have been modified after run
<a class="reference internal" href="#pywebio.platform.path_deploy" title="pywebio.platform.path_deploy"><code class="xref py py-obj docutils literal notranslate"><span class="pre">path_deploy()</span></code></a>, you can use <code class="docutils literal notranslate"><span class="pre">reload</span></code> URL parameter to reload application in the file:
<code class="docutils literal notranslate"><span class="pre">http://&lt;host&gt;:&lt;port&gt;/A/b?reload</span></code></p>
<p>You can also use the command <code class="docutils literal notranslate"><span class="pre">pywebio-path-deploy</span></code> to start a server just like using
<a class="reference internal" href="#pywebio.platform.path_deploy" title="pywebio.platform.path_deploy"><code class="xref py py-obj docutils literal notranslate"><span class="pre">path_deploy()</span></code></a>. For more information, refer <code class="docutils literal notranslate"><span class="pre">pywebio-path-deploy</span> <span class="pre">--help</span></code></p>
<dl class="py function">
<dt id="pywebio.platform.path_deploy">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.</span></code><code class="sig-name descname"><span class="pre">path_deploy</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">base</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">port</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">index</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">reconnect_timeout</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">max_payload_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'200M'</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">tornado_app_settings</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/path_deploy.html#path_deploy"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.path_deploy" title="Permalink to this definition">¶</a></dt>
<dd><p>Deploy the PyWebIO applications from a directory.</p>
<p>The server communicates with the browser using WebSocket protocol.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>base</strong> (<em>str</em>) – Base directory to load PyWebIO application.</p></li>
<li><p><strong>port</strong> (<em>int</em>) – The port the server listens on.</p></li>
<li><p><strong>host</strong> (<em>str</em>) – The host the server listens on.</p></li>
<li><p><strong>index</strong> (<em>bool/callable</em>) – </p><p>Whether to provide a default index page when request a directory, default is <code class="docutils literal notranslate"><span class="pre">True</span></code>.
<code class="docutils literal notranslate"><span class="pre">index</span></code> also accepts a function to custom index page, which receives the requested directory path as parameter
and return HTML content in string.</p>
<p>You can override the index page by add a <code class="xref py py-obj docutils literal notranslate"><span class="pre">index.py</span></code> PyWebIO app file to the directory.</p>
<p></p></li>
<li><p><strong>static_dir</strong> (<em>str</em>) – Directory to store the application static files.
The files in this directory can be accessed via <code class="docutils literal notranslate"><span class="pre">http://&lt;host&gt;:&lt;port&gt;/static/files</span></code>.
For example, if there is a <code class="docutils literal notranslate"><span class="pre">A/B.jpg</span></code> file in <code class="docutils literal notranslate"><span class="pre">static_dir</span></code> path,
it can be accessed via <code class="docutils literal notranslate"><span class="pre">http://&lt;host&gt;:&lt;port&gt;/static/A/B.jpg</span></code>.</p></li>
<li><p><strong>reconnect_timeout</strong> (<em>int</em>) – The client can reconnect to server within <code class="docutils literal notranslate"><span class="pre">reconnect_timeout</span></code> seconds after an unexpected disconnection.
If set to 0 (default), once the client disconnects, the server session will be closed.</p></li>
</ul>
</dd>
</dl>
<p>The rest arguments of <code class="docutils literal notranslate"><span class="pre">path_deploy()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.tornado.start_server" title="pywebio.platform.tornado.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.tornado.start_server()</span></code></a></p>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.path_deploy_http">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.</span></code><code class="sig-name descname"><span class="pre">path_deploy_http</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">base</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">port</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">index</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_expire_seconds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_cleanup_interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">max_payload_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'200M'</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">tornado_app_settings</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/path_deploy.html#path_deploy_http"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.path_deploy_http" title="Permalink to this definition">¶</a></dt>
<dd><p>Deploy the PyWebIO applications from a directory.</p>
<p>The server communicates with the browser using HTTP protocol.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">base</span></code>, <code class="docutils literal notranslate"><span class="pre">port</span></code>, <code class="docutils literal notranslate"><span class="pre">host</span></code>, <code class="docutils literal notranslate"><span class="pre">index</span></code>, <code class="docutils literal notranslate"><span class="pre">static_dir</span></code> arguments of <code class="docutils literal notranslate"><span class="pre">path_deploy_http()</span></code>
have the same meaning as for <a class="reference internal" href="#pywebio.platform.path_deploy" title="pywebio.platform.path_deploy"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.path_deploy()</span></code></a></p>
<p>The rest arguments of <code class="docutils literal notranslate"><span class="pre">path_deploy_http()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.tornado_http.start_server" title="pywebio.platform.tornado_http.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.tornado_http.start_server()</span></code></a></p>
</dd></dl>

</div>
<div class="section" id="application-deploy">
<span id="app-deploy"></span><h2><a class="toc-backref" href="#id2">Application Deploy</a><a class="headerlink" href="#application-deploy" title="Permalink to this headline">¶</a></h2>
<p>The <code class="docutils literal notranslate"><span class="pre">start_server()</span></code> functions can start a Python Web server and serve given PyWebIO applications on it.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">webio_handler()</span></code> and <code class="docutils literal notranslate"><span class="pre">webio_view()</span></code> functions can be used to integrate PyWebIO applications into existing Python Web project.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">wsgi_app()</span></code> and <code class="docutils literal notranslate"><span class="pre">asgi_app()</span></code> is used to get the WSGI or ASGI app for running PyWebIO applications.
This is helpful when you don’t want to start server with the Web framework built-in’s.
For example, you want to use other WSGI server, or you are deploying app in a cloud environment.
Note that only Flask, Django and FastApi backend support it.</p>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 1.1: </span>Added the <code class="docutils literal notranslate"><span class="pre">cdn</span></code> parameter in <code class="docutils literal notranslate"><span class="pre">start_server()</span></code>, <code class="docutils literal notranslate"><span class="pre">webio_handler()</span></code> and <code class="docutils literal notranslate"><span class="pre">webio_view()</span></code>.</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 1.2: </span>Added the <code class="docutils literal notranslate"><span class="pre">static_dir</span></code> parameter in <code class="docutils literal notranslate"><span class="pre">start_server()</span></code>.</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 1.3: </span>Added the <code class="docutils literal notranslate"><span class="pre">wsgi_app()</span></code> and <code class="docutils literal notranslate"><span class="pre">asgi_app()</span></code>.</p>
</div>
<div class="section" id="tornado-support">
<h3><a class="toc-backref" href="#id3">Tornado support</a><a class="headerlink" href="#tornado-support" title="Permalink to this headline">¶</a></h3>
<p>There are two protocols (WebSocket and HTTP) can be used to communicates with the browser:</p>
<div class="section" id="websocket">
<h4><a class="toc-backref" href="#id4">WebSocket</a><a class="headerlink" href="#websocket" title="Permalink to this headline">¶</a></h4>
<dl class="py function">
<dt id="pywebio.platform.tornado.start_server">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.tornado.</span></code><code class="sig-name descname"><span class="pre">start_server</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">port</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">remote_access</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">reconnect_timeout</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">auto_open_webbrowser</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">max_payload_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'200M'</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">tornado_app_settings</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/tornado.html#start_server"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.tornado.start_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Start a Tornado server to provide the PyWebIO application as a web service.</p>
<p>The Tornado server communicates with the browser by WebSocket protocol.</p>
<p>Tornado is the default backend server for PyWebIO applications,
and <code class="docutils literal notranslate"><span class="pre">start_server</span></code> can be imported directly using <code class="docutils literal notranslate"><span class="pre">from</span> <span class="pre">pywebio</span> <span class="pre">import</span> <span class="pre">start_server</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>applications</strong> (<em>list/dict/callable</em>) – </p><p>PyWebIO application.
Can be a task function, a list of functions, or a dictionary.
Refer to <a class="reference internal" href="advanced.html#multiple-app"><span class="std std-ref">Advanced topic: Multiple applications in start_server()</span></a> for more information.</p>
<p>When the task function is a coroutine function, use <a class="reference internal" href="advanced.html#coroutine-based-session"><span class="std std-ref">Coroutine-based session</span></a> implementation,
otherwise, use thread-based session implementation.</p>
<p></p></li>
<li><p><strong>port</strong> (<em>int</em>) – The port the server listens on.
When set to <code class="docutils literal notranslate"><span class="pre">0</span></code>, the server will automatically select a available port.</p></li>
<li><p><strong>host</strong> (<em>str</em>) – The host the server listens on. <code class="docutils literal notranslate"><span class="pre">host</span></code> may be either an IP address or hostname.
If it’s a hostname, the server will listen on all IP addresses associated with the name.
<code class="docutils literal notranslate"><span class="pre">host</span></code> may be an empty string or None to listen on all available interfaces.</p></li>
<li><p><strong>debug</strong> (<em>bool</em>) – Tornado Server’s debug mode. If enabled, the server will automatically reload for code changes.
See <a class="reference external" href="https://www.tornadoweb.org/en/stable/guide/running.html#debug-mode">tornado doc</a> for more detail.</p></li>
<li><p><strong>cdn</strong> (<em>bool/str</em>) – Whether to load front-end static resources from CDN, the default is <code class="docutils literal notranslate"><span class="pre">True</span></code>.
Can also use a string to directly set the url of PyWebIO static resources.</p></li>
<li><p><strong>static_dir</strong> (<em>str</em>) – The directory to store the application static files.
The files in this directory can be accessed via <code class="docutils literal notranslate"><span class="pre">http://&lt;host&gt;:&lt;port&gt;/static/files</span></code>.
For example, if there is a <code class="docutils literal notranslate"><span class="pre">A/B.jpg</span></code> file in <code class="docutils literal notranslate"><span class="pre">static_dir</span></code> path,
it can be accessed via <code class="docutils literal notranslate"><span class="pre">http://&lt;host&gt;:&lt;port&gt;/static/A/B.jpg</span></code>.</p></li>
<li><p><strong>remote_access</strong> (<em>bool</em>) – Whether to enable remote access, when enabled,
you can get a temporary public network access address for the current application,
others can access your application via this address.</p></li>
<li><p><strong>auto_open_webbrowser</strong> (<em>bool</em>) – Whether or not auto open web browser when server is started (if the operating system allows it) .</p></li>
<li><p><strong>reconnect_timeout</strong> (<em>int</em>) – The client can reconnect to server within <code class="docutils literal notranslate"><span class="pre">reconnect_timeout</span></code> seconds after an unexpected disconnection.
If set to 0 (default), once the client disconnects, the server session will be closed.</p></li>
<li><p><strong>allowed_origins</strong> (<em>list</em>) – </p><p>The allowed request source list. (The current server host is always allowed)
The source contains the protocol, domain name, and port part.
Can use Unix shell-style wildcards:</p>
<blockquote>
<div><ul>
<li><p><code class="docutils literal notranslate"><span class="pre">*</span></code> matches everything</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">?</span></code> matches any single character</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">[seq]</span></code> matches any character in <em>seq</em></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">[!seq]</span></code> matches any character not in <em>seq</em></p></li>
</ul>
<p>Such as: <code class="docutils literal notranslate"><span class="pre">https://*.example.com</span></code> 、 <code class="docutils literal notranslate"><span class="pre">*://*.example.com</span></code></p>
<p>For detail, see <a class="reference external" href="https://docs.python.org/zh-tw/3/library/fnmatch.html">Python Doc</a></p>
</div></blockquote>
<p></p></li>
<li><p><strong>check_origin</strong> (<em>callable</em>) – The validation function for request source.
It receives the source string (which contains protocol, host, and port parts) as parameter and
return <code class="docutils literal notranslate"><span class="pre">True/False</span></code> to indicate that the server accepts/rejects the request.
If <code class="docutils literal notranslate"><span class="pre">check_origin</span></code> is set, the <code class="docutils literal notranslate"><span class="pre">allowed_origins</span></code> parameter will be ignored.</p></li>
<li><p><strong>auto_open_webbrowser</strong> – Whether or not auto open web browser when server is started (if the operating system allows it) .</p></li>
<li><p><strong>max_payload_size</strong> (<em>int/str</em>) – Max size of a websocket message which Tornado can accept.
Messages larger than the <code class="docutils literal notranslate"><span class="pre">max_payload_size</span></code> (default 200MB) will not be accepted.
<code class="docutils literal notranslate"><span class="pre">max_payload_size</span></code> can be a integer indicating the number of bytes, or a string ending with <code class="xref py py-obj docutils literal notranslate"><span class="pre">K</span></code> / <code class="xref py py-obj docutils literal notranslate"><span class="pre">M</span></code> / <code class="xref py py-obj docutils literal notranslate"><span class="pre">G</span></code>
(representing kilobytes, megabytes, and gigabytes, respectively).
E.g: <code class="docutils literal notranslate"><span class="pre">500</span></code>, <code class="docutils literal notranslate"><span class="pre">'40K'</span></code>, <code class="docutils literal notranslate"><span class="pre">'3M'</span></code></p></li>
<li><p><strong>tornado_app_settings</strong> – Additional keyword arguments passed to the constructor of <code class="docutils literal notranslate"><span class="pre">tornado.web.Application</span></code>.
For details, please refer: <a class="reference external" href="https://www.tornadoweb.org/en/stable/web.html#tornado.web.Application.settings">https://www.tornadoweb.org/en/stable/web.html#tornado.web.Application.settings</a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.tornado.webio_handler">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.tornado.</span></code><code class="sig-name descname"><span class="pre">webio_handler</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">reconnect_timeout</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/tornado.html#webio_handler"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.tornado.webio_handler" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the <code class="docutils literal notranslate"><span class="pre">RequestHandler</span></code> class for running PyWebIO applications in Tornado.
The <code class="docutils literal notranslate"><span class="pre">RequestHandler</span></code> communicates with the browser by WebSocket protocol.</p>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">webio_handler()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.tornado.start_server" title="pywebio.platform.tornado.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.tornado.start_server()</span></code></a></p>
</dd></dl>

</div>
<div class="section" id="http">
<h4><a class="toc-backref" href="#id5">HTTP</a><a class="headerlink" href="#http" title="Permalink to this headline">¶</a></h4>
<dl class="py function">
<dt id="pywebio.platform.tornado_http.start_server">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.tornado_http.</span></code><code class="sig-name descname"><span class="pre">start_server</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">port</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">8080</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">auto_open_webbrowser</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_expire_seconds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_cleanup_interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">max_payload_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'200M'</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">tornado_app_settings</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/tornado_http.html#start_server"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.tornado_http.start_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Start a Tornado server to provide the PyWebIO application as a web service.</p>
<p>The Tornado server communicates with the browser by HTTP protocol.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>session_expire_seconds</strong> (<em>int</em>) – Session expiration time, in seconds(default 60s).
If no client message is received within <code class="docutils literal notranslate"><span class="pre">session_expire_seconds</span></code>, the session will be considered expired.</p></li>
<li><p><strong>session_cleanup_interval</strong> (<em>int</em>) – Session cleanup interval, in seconds(default 120s).
The server will periodically clean up expired sessions and release the resources occupied by the sessions.</p></li>
<li><p><strong>max_payload_size</strong> (<em>int/str</em>) – Max size of a request body which Tornado can accept.</p></li>
</ul>
</dd>
</dl>
<p>The rest arguments of <code class="docutils literal notranslate"><span class="pre">start_server()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.tornado.start_server" title="pywebio.platform.tornado.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.tornado.start_server()</span></code></a></p>
<div class="versionadded">
<p><span class="versionmodified added">New in version 1.2.</span></p>
</div>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.tornado_http.webio_handler">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.tornado_http.</span></code><code class="sig-name descname"><span class="pre">webio_handler</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_expire_seconds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_cleanup_interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/tornado_http.html#webio_handler"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.tornado_http.webio_handler" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the <code class="docutils literal notranslate"><span class="pre">RequestHandler</span></code> class for running PyWebIO applications in Tornado.
The <code class="docutils literal notranslate"><span class="pre">RequestHandler</span></code>  communicates with the browser by HTTP protocol.</p>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">webio_handler()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.tornado_http.start_server" title="pywebio.platform.tornado_http.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.tornado_http.start_server()</span></code></a></p>
<div class="versionadded">
<p><span class="versionmodified added">New in version 1.2.</span></p>
</div>
</dd></dl>

</div>
</div>
<div class="section" id="flask-support">
<h3><a class="toc-backref" href="#id6">Flask support</a><a class="headerlink" href="#flask-support" title="Permalink to this headline">¶</a></h3>
<p>When using the Flask as PyWebIO backend server, you need to install Flask by yourself and make sure the version is not less than <code class="docutils literal notranslate"><span class="pre">0.10</span></code>.
You can install it with the following command:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip3</span> <span class="n">install</span> <span class="o">-</span><span class="n">U</span> <span class="n">flask</span><span class="o">&gt;=</span><span class="mf">0.10</span>
</pre></div>
</div>
<dl class="py function">
<dt id="pywebio.platform.flask.webio_view">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.flask.</span></code><code class="sig-name descname"><span class="pre">webio_view</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_expire_seconds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_cleanup_interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/flask.html#webio_view"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.flask.webio_view" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the view function for running PyWebIO applications in Flask.
The view communicates with the browser by HTTP protocol.</p>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">webio_view()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.flask.start_server" title="pywebio.platform.flask.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.flask.start_server()</span></code></a></p>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.flask.wsgi_app">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.flask.</span></code><code class="sig-name descname"><span class="pre">wsgi_app</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_expire_seconds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_cleanup_interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">max_payload_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'200M'</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/flask.html#wsgi_app"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.flask.wsgi_app" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the Flask WSGI app for running PyWebIO applications.</p>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">wsgi_app()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.flask.start_server" title="pywebio.platform.flask.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.flask.start_server()</span></code></a></p>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.flask.start_server">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.flask.</span></code><code class="sig-name descname"><span class="pre">start_server</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">port</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">8080</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">remote_access</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_expire_seconds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_cleanup_interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">max_payload_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'200M'</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">flask_options</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/flask.html#start_server"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.flask.start_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Start a Flask server to provide the PyWebIO application as a web service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>session_expire_seconds</strong> (<em>int</em>) – Session expiration time, in seconds(default 600s).
If no client message is received within <code class="docutils literal notranslate"><span class="pre">session_expire_seconds</span></code>, the session will be considered expired.</p></li>
<li><p><strong>session_cleanup_interval</strong> (<em>int</em>) – Session cleanup interval, in seconds(default 300s).
The server will periodically clean up expired sessions and release the resources occupied by the sessions.</p></li>
<li><p><strong>debug</strong> (<em>bool</em>) – Flask debug mode.
If enabled, the server will automatically reload for code changes.</p></li>
<li><p><strong>max_payload_size</strong> (<em>int/str</em>) – Max size of a request body which Flask can accept.</p></li>
<li><p><strong>flask_options</strong> – Additional keyword arguments passed to the <code class="docutils literal notranslate"><span class="pre">flask.Flask.run</span></code>.
For details, please refer: <a class="reference external" href="https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.run">https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.run</a></p></li>
</ul>
</dd>
</dl>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">start_server()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.tornado.start_server" title="pywebio.platform.tornado.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.tornado.start_server()</span></code></a></p>
</dd></dl>

</div>
<div class="section" id="django-support">
<h3><a class="toc-backref" href="#id7">Django support</a><a class="headerlink" href="#django-support" title="Permalink to this headline">¶</a></h3>
<p>When using the Django as PyWebIO backend server, you need to install Django by yourself and make sure the version is not less than <code class="docutils literal notranslate"><span class="pre">2.2</span></code>.
You can install it with the following command:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip3</span> <span class="n">install</span> <span class="o">-</span><span class="n">U</span> <span class="n">django</span><span class="o">&gt;=</span><span class="mf">2.2</span>
</pre></div>
</div>
<dl class="py function">
<dt id="pywebio.platform.django.webio_view">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.django.</span></code><code class="sig-name descname"><span class="pre">webio_view</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_expire_seconds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_cleanup_interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/django.html#webio_view"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.django.webio_view" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the view function for running PyWebIO applications in Django.
The view communicates with the browser by HTTP protocol.</p>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">webio_view()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.flask.webio_view" title="pywebio.platform.flask.webio_view"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.flask.webio_view()</span></code></a></p>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.django.wsgi_app">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.django.</span></code><code class="sig-name descname"><span class="pre">wsgi_app</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_expire_seconds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_cleanup_interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">max_payload_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'200M'</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">django_options</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/django.html#wsgi_app"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.django.wsgi_app" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the Django WSGI app for running PyWebIO applications.</p>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">wsgi_app()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.django.start_server" title="pywebio.platform.django.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.django.start_server()</span></code></a></p>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.django.start_server">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.django.</span></code><code class="sig-name descname"><span class="pre">start_server</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">port</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">8080</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">remote_access</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_expire_seconds</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">session_cleanup_interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">max_payload_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'200M'</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">django_options</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/django.html#start_server"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.django.start_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Start a Django server to provide the PyWebIO application as a web service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>debug</strong> (<em>bool</em>) – Django debug mode.
See <a class="reference external" href="https://docs.djangoproject.com/en/3.0/ref/settings/#debug">Django doc</a> for more detail.</p></li>
<li><p><strong>django_options</strong> – Additional settings to django server.
For details, please refer: <a class="reference external" href="https://docs.djangoproject.com/en/3.0/ref/settings/">https://docs.djangoproject.com/en/3.0/ref/settings/</a> .
Among them, <code class="docutils literal notranslate"><span class="pre">DEBUG</span></code>, <code class="docutils literal notranslate"><span class="pre">ALLOWED_HOSTS</span></code>, <code class="docutils literal notranslate"><span class="pre">ROOT_URLCONF</span></code>, <code class="docutils literal notranslate"><span class="pre">SECRET_KEY</span></code> are set by PyWebIO and cannot be specified in <code class="docutils literal notranslate"><span class="pre">django_options</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The rest arguments of <code class="docutils literal notranslate"><span class="pre">start_server()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.flask.start_server" title="pywebio.platform.flask.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.flask.start_server()</span></code></a></p>
</dd></dl>

</div>
<div class="section" id="aiohttp-support">
<h3><a class="toc-backref" href="#id8">aiohttp support</a><a class="headerlink" href="#aiohttp-support" title="Permalink to this headline">¶</a></h3>
<p>When using the aiohttp as PyWebIO backend server, you need to install aiohttp by yourself and make sure the version is not less than <code class="docutils literal notranslate"><span class="pre">3.1</span></code>.
You can install it with the following command:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip3</span> <span class="n">install</span> <span class="o">-</span><span class="n">U</span> <span class="n">aiohttp</span><span class="o">&gt;=</span><span class="mf">3.1</span>
</pre></div>
</div>
<dl class="py function">
<dt id="pywebio.platform.aiohttp.webio_handler">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.aiohttp.</span></code><code class="sig-name descname"><span class="pre">webio_handler</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">websocket_settings</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/aiohttp.html#webio_handler"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.aiohttp.webio_handler" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the <a class="reference external" href="https://docs.aiohttp.org/en/stable/web_quickstart.html#aiohttp-web-handler">Request Handler</a> coroutine for running PyWebIO applications in aiohttp.
The handler communicates with the browser by WebSocket protocol.</p>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">webio_handler()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.aiohttp.start_server" title="pywebio.platform.aiohttp.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.aiohttp.start_server()</span></code></a></p>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>aiohttp Request Handler</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.aiohttp.start_server">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.aiohttp.</span></code><code class="sig-name descname"><span class="pre">start_server</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">port</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">remote_access</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">auto_open_webbrowser</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">websocket_settings</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">aiohttp_settings</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/aiohttp.html#start_server"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.aiohttp.start_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Start a aiohttp server to provide the PyWebIO application as a web service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>websocket_settings</strong> (<em>dict</em>) – The  parameters passed to the constructor of <code class="docutils literal notranslate"><span class="pre">aiohttp.web.WebSocketResponse</span></code>.
For details, please refer: <a class="reference external" href="https://docs.aiohttp.org/en/stable/web_reference.html#websocketresponse">https://docs.aiohttp.org/en/stable/web_reference.html#websocketresponse</a></p></li>
<li><p><strong>aiohttp_settings</strong> – Additional keyword arguments passed to the constructor of <code class="docutils literal notranslate"><span class="pre">aiohttp.web.Application</span></code>.
For details, please refer: <a class="reference external" href="https://docs.aiohttp.org/en/stable/web_reference.html#application">https://docs.aiohttp.org/en/stable/web_reference.html#application</a></p></li>
</ul>
</dd>
</dl>
<p>The rest arguments of <code class="docutils literal notranslate"><span class="pre">start_server()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.tornado.start_server" title="pywebio.platform.tornado.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.tornado.start_server()</span></code></a></p>
</dd></dl>

</div>
<div class="section" id="fastapi-starlette-support">
<h3><a class="toc-backref" href="#id9">FastAPI/Starlette support</a><a class="headerlink" href="#fastapi-starlette-support" title="Permalink to this headline">¶</a></h3>
<p>When using the FastAPI/Starlette as PyWebIO backend server, you need to install <code class="docutils literal notranslate"><span class="pre">fastapi</span></code> or <code class="docutils literal notranslate"><span class="pre">starlette</span></code> by yourself.
Also other dependency packages are required. You can install them with the following command:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">pip3</span> <span class="n">install</span> <span class="o">-</span><span class="n">U</span> <span class="n">fastapi</span> <span class="n">starlette</span> <span class="n">uvicorn</span> <span class="n">aiofiles</span> <span class="n">websockets</span>
</pre></div>
</div>
<dl class="py function">
<dt id="pywebio.platform.fastapi.webio_routes">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.fastapi.</span></code><code class="sig-name descname"><span class="pre">webio_routes</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/fastapi.html#webio_routes"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.fastapi.webio_routes" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the FastAPI/Starlette routes for running PyWebIO applications.</p>
<p>The API communicates with the browser using WebSocket protocol.</p>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">webio_routes()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.fastapi.start_server" title="pywebio.platform.fastapi.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.fastapi.start_server()</span></code></a></p>
<div class="versionadded">
<p><span class="versionmodified added">New in version 1.3.</span></p>
</div>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>FastAPI/Starlette routes</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.fastapi.asgi_app">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.fastapi.</span></code><code class="sig-name descname"><span class="pre">asgi_app</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/fastapi.html#asgi_app"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.fastapi.asgi_app" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the starlette/Fastapi ASGI app for running PyWebIO applications.</p>
<p>Use <a class="reference internal" href="#pywebio.platform.fastapi.webio_routes" title="pywebio.platform.fastapi.webio_routes"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.fastapi.webio_routes()</span></code></a> if you prefer handling static files yourself.</p>
<p>The arguments of <code class="docutils literal notranslate"><span class="pre">asgi_app()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.fastapi.start_server" title="pywebio.platform.fastapi.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.fastapi.start_server()</span></code></a></p>
<dl class="field-list simple">
<dt class="field-odd">Example</dt>
<dd class="field-odd"><p></p></dd>
</dl>
<p>To be used with <code class="docutils literal notranslate"><span class="pre">FastAPI.mount()</span></code> to include pywebio as a subapp into an existing Starlette/FastAPI application:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">fastapi</span> <span class="kn">import</span> <span class="n">FastAPI</span>
<span class="kn">from</span> <span class="nn">pywebio.platform.fastapi</span> <span class="kn">import</span> <span class="n">asgi_app</span>
<span class="kn">from</span> <span class="nn">pywebio.output</span> <span class="kn">import</span> <span class="n">put_text</span>
<span class="n">app</span> <span class="o">=</span> <span class="n">FastAPI</span><span class="p">()</span>
<span class="n">subapp</span> <span class="o">=</span> <span class="n">asgi_app</span><span class="p">(</span><span class="k">lambda</span><span class="p">:</span> <span class="n">put_text</span><span class="p">(</span><span class="s2">"hello from pywebio"</span><span class="p">))</span>
<span class="n">app</span><span class="o">.</span><span class="n">mount</span><span class="p">(</span><span class="s2">"/pywebio"</span><span class="p">,</span> <span class="n">subapp</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Returns</dt>
<dd class="field-odd"><p>Starlette/Fastapi ASGI app</p>
</dd>
</dl>
<div class="versionadded">
<p><span class="versionmodified added">New in version 1.3.</span></p>
</div>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.fastapi.start_server">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.fastapi.</span></code><code class="sig-name descname"><span class="pre">start_server</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">applications</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">port</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">host</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">cdn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">static_dir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">remote_access</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">allowed_origins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">check_origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">auto_open_webbrowser</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">uvicorn_settings</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/fastapi.html#start_server"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.fastapi.start_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Start a FastAPI/Starlette server using uvicorn to provide the PyWebIO application as a web service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>debug</strong> (<em>bool</em>) – Boolean indicating if debug tracebacks should be returned on errors.</p></li>
<li><p><strong>uvicorn_settings</strong> – Additional keyword arguments passed to <code class="docutils literal notranslate"><span class="pre">uvicorn.run()</span></code>.
For details, please refer: <a class="reference external" href="https://www.uvicorn.org/settings/">https://www.uvicorn.org/settings/</a></p></li>
</ul>
</dd>
</dl>
<p>The rest arguments of <code class="docutils literal notranslate"><span class="pre">start_server()</span></code> have the same meaning as for <a class="reference internal" href="#pywebio.platform.tornado.start_server" title="pywebio.platform.tornado.start_server"><code class="xref py py-func docutils literal notranslate"><span class="pre">pywebio.platform.tornado.start_server()</span></code></a></p>
<div class="versionadded">
<p><span class="versionmodified added">New in version 1.3.</span></p>
</div>
</dd></dl>

</div>
</div>
<div class="section" id="other">
<h2><a class="toc-backref" href="#id10">Other</a><a class="headerlink" href="#other" title="Permalink to this headline">¶</a></h2>
<dl class="py function">
<dt id="pywebio.config">
<code class="sig-prename descclassname"><span class="pre">pywebio.</span></code><code class="sig-name descname"><span class="pre">config</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="o"><span class="pre">*</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">title</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">description</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">theme</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">js_code</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">js_file</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">css_style</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">css_file</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">[]</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/page.html#config"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.config" title="Permalink to this definition">¶</a></dt>
<dd><p>PyWebIO application configuration</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>title</strong> (<em>str</em>) – Application title</p></li>
<li><p><strong>description</strong> (<em>str</em>) – Application description</p></li>
<li><p><strong>theme</strong> (<em>str</em>) – </p><p>Application theme. Available themes are: <code class="docutils literal notranslate"><span class="pre">dark</span></code>, <code class="docutils literal notranslate"><span class="pre">sketchy</span></code>, <code class="docutils literal notranslate"><span class="pre">minty</span></code>, <code class="docutils literal notranslate"><span class="pre">yeti</span></code>.
You can also use environment variable <code class="docutils literal notranslate"><span class="pre">PYWEBIO_THEME</span></code> to specify the theme (with high priority).</p>
<p><a class="reference external" href="http://pywebio-demos.pywebio.online/theme">Theme preview demo</a></p>
<details class="summary-open-source-credits">
<summary>Open Source Credits</summary><p>The dark theme is modified from ForEvolve’s <a class="reference external" href="https://github.com/ForEvolve/bootstrap-dark">bootstrap-dark</a>.
The sketchy, minty and yeti theme are from <a class="reference external" href="https://bootswatch.com/4/">bootswatch</a>.</p>
</details><p></p></li>
<li><p><strong>js_code</strong> (<em>str</em>) – The javascript code that you want to inject to page.</p></li>
<li><p><strong>js_file</strong> (<em>str/list</em>) – The javascript files that inject to page, can be a URL in str or a list of it.</p></li>
<li><p><strong>css_style</strong> (<em>str</em>) – The CSS style that you want to inject to page.</p></li>
<li><p><strong>css_file</strong> (<em>str/list</em>) – The CSS files that inject to page, can be a URL in str or a list of it.</p></li>
</ul>
</dd>
</dl>
<p><code class="docutils literal notranslate"><span class="pre">config()</span></code> can be used in 2 ways: direct call and decorator.
If you call <code class="docutils literal notranslate"><span class="pre">config()</span></code> directly, the configuration will be global.
If you use <code class="docutils literal notranslate"><span class="pre">config()</span></code> as decorator, the configuration will only work on single PyWebIO application function.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">config</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">"My application"</span><span class="p">)</span>  <span class="c1"># global configuration</span>

<span class="nd">@config</span><span class="p">(</span><span class="n">css_style</span><span class="o">=</span><span class="s2">"* { color:red }"</span><span class="p">)</span>  <span class="c1"># only works on this application</span>
<span class="k">def</span> <span class="nf">app</span><span class="p">():</span>
    <span class="n">put_text</span><span class="p">(</span><span class="s2">"hello PyWebIO"</span><span class="p">)</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The configuration will affect all sessions</p>
</div>
<p><code class="docutils literal notranslate"><span class="pre">title</span></code> and <code class="docutils literal notranslate"><span class="pre">description</span></code> are used for SEO, which are provided when indexed by search engines.
If no <code class="docutils literal notranslate"><span class="pre">title</span></code> and <code class="docutils literal notranslate"><span class="pre">description</span></code> set for a PyWebIO application function,
the <a class="reference external" href="https://www.python.org/dev/peps/pep-0257/">docstring</a> of the function will be used as title and description by default:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">app</span><span class="p">():</span>
    <span class="sd">"""Application title</span>

<span class="sd">    Application description...</span>
<span class="sd">    (A empty line is used to separate the description and title)</span>
<span class="sd">    """</span>
    <span class="k">pass</span>
</pre></div>
</div>
<p>The above code is equal to:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="nd">@config</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">"Application title"</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">"Application description..."</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">app</span><span class="p">():</span>
    <span class="k">pass</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified added">New in version 1.4.</span></p>
</div>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 1.5: </span>add <code class="docutils literal notranslate"><span class="pre">theme</span></code> parameter</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="pywebio.platform.run_event_loop">
<code class="sig-prename descclassname"><span class="pre">pywebio.platform.</span></code><code class="sig-name descname"><span class="pre">run_event_loop</span></code><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">debug</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="reference internal" href="_modules/pywebio/platform/httpbased.html#run_event_loop"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a class="headerlink" href="#pywebio.platform.run_event_loop" title="Permalink to this definition">¶</a></dt>
<dd><p>run asyncio event loop</p>
<p>See also: <a class="reference internal" href="advanced.html#coroutine-web-integration"><span class="std std-ref">Integration coroutine-based session with Web framework</span></a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>debug</strong> – Set the debug mode of the event loop.
See also: <a class="reference external" href="https://docs.python.org/3/library/asyncio-dev.html#asyncio-debug-mode">https://docs.python.org/3/library/asyncio-dev.html#asyncio-debug-mode</a></p>
</dd>
</dl>
</dd></dl>

</div>
</div>


           </div>
           
          </div>
          <footer>
  
    <div class="rst-footer-buttons" role="navigation" aria-label="footer navigation">
      
        <a href="pin.html" class="btn btn-neutral float-right" title="pywebio.pin — Persistent input" accesskey="n" rel="next">Next <span class="fa fa-arrow-circle-right"></span></a>
      
      
        <a href="session.html" class="btn btn-neutral float-left" title="pywebio.session — More control to session" accesskey="p" rel="prev"><span class="fa fa-arrow-circle-left"></span> Previous</a>
      
    </div>
  

  <hr><div><div id="rtd-sidebar" data-ea-publisher="readthedocs" data-ea-type="readthedocs-sidebar" data-ea-manual="true" class="ethical-rtd loaded" data-ea-keywords="python|readthedocs-project-579504|readthedocs-project-pywebio" data-ea-campaign-types="community|house"><div class="ethical-sidebar"><div class="ethical-content"><a href="https://server.ethicalads.io/proxy/click/2724/6c320e4d-e8a8-4de8-975a-eef374ba6980/" rel="nofollow noopener" target="_blank" class="ethical-image-link"><img src="https://media.ethicalads.io/media/images/2022/04/wtd-na-2016_jiI9q6e.png" alt="Sponsored: Read the Docs"></a><div class="ethical-text">Love Documentation? <a href="https://server.ethicalads.io/proxy/click/2724/6c320e4d-e8a8-4de8-975a-eef374ba6980/" rel="nofollow noopener" target="_blank">Write the Docs Portland</a> is a 3-day virtual docs event. May 22-24.</div></div><div class="ethical-callout"><small><em><a href="https://docs.readthedocs.io/en/latest/advertising/ethical-advertising.html#community-ads">Community Ad</a></em></small></div></div></div></div>

  <div role="contentinfo">
    <p>
        © Copyright Weimin Wang
      
        <span class="commit">
          Revision <code>f137c414</code>.
        </span>
      

    </p>
  </div>
  Built with <a href="http://sphinx-doc.org/">Sphinx</a> using a <a href="https://github.com/rtfd/sphinx_rtd_theme">theme</a> provided by <a href="https://readthedocs.org">Read the Docs</a>. 

</footer>

        </div>
      </div>

    </section>''')



app.add_url_rule('/tool','webio.view',webio_view(start)
                 ,methods=['GET','POST','OPTIONS'])

if __name__== "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--port",type=int,default=8080)
        args = parser.parse_args()
        start_server(start,port=args.port)
