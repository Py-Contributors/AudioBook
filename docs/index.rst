<p align="center">
    <a href="https://codeperfectplus.github.io/audiobook/"><img src="https://capsule-render.vercel.app/api?type=rect&color=009ACD&height=100&section=header&text=audioBook&fontSize=80%&fontColor=ffffff" alt="website title image"></a>
    <h2 align="center">👉 Listen to any PDF book with just a few line of Python code👈</h2>
  </p>
  
  <p align="center">
  <img src="https://img.shields.io/github/pipenv/locked/python-version/codeperfectplus/audiobook?style=for-the-badge" alt="repo language">
  <a href="https://github.com/codeperfectplus/audiobook/stargazers"><img src="https://img.shields.io/github/stars/codeperfectplus/audiobook?style=for-the-badge" alt="github stars"></a>
  <a href="https://github.com/codeperfectplus/audiobook/network/members"><img src="https://img.shields.io/github/forks/codeperfectplus/audiobook?style=for-the-badge" alt="github forks"></a>
  <img src="https://img.shields.io/github/languages/code-size/codeperfectplus/audiobook?style=for-the-badge" alt="code size">
    </p>
    <p align="center">
  <a href="https://pypi.org/project/audiobook/"><img src="https://img.shields.io/pypi/status/audiobook.svg?style=for-the-badge" alt="pypi status"></a>
  <a href="https://pypi.org/project/audiobook/"><img src="https://img.shields.io/pypi/dm/audiobook?style=for-the-badge" alt="download"></a>
  
  </p>
  <p align="center">
  <a href="https://discord.gg/JfbK3bS"><img src="https://img.shields.io/discord/758030555005714512.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge" alt="discord invite"></a>
  <img src="https://img.shields.io/github/last-commit/codeperfectplus/audiobook?style=for-the-badge" alt="last contributions">
  <a href="https://api.github.com/repos/codeperfectplus/audiobook/contributors"><img src="https://img.shields.io/github/contributors/codeperfectplus/audiobook?style=for-the-badge" alt="total contributors"></a>
  </p>
  
  <h2 id="installation">Installation</h2>
  <p>Install it from <a href="https://pypi.org/project/audiobook/">pypi</a></p>
  <pre><code class="lang-sh">pip <span class="hljs-keyword">install</span> audiobook
  </code></pre>
  <pre><code class="lang-python"><span class="hljs-keyword">from</span> audiobook <span class="hljs-keyword">import</span> AudioBook
  ab = AudioBook(<span class="hljs-string">"file_path"</span>)
  ab.text_to_speech()
  </code></pre>
  <h2 id="usages">Usages</h2>
  <p>Audibook is python module to listen your fav pdf book.</p>
  <h2 id="documentation">Documentation</h2>
  <p>Read Detailed <a href="https://audiobook.readthedocs.io/">Documentation here</a></p>
  <h3 id="linux-installation-requirements">Linux installation requirements</h3>
  <ul>
  <li>If you are on a linux system and if the voice output is not working , then :
    Install espeak , ffmpeg and libespeak1 as shown below:</li>
  </ul>
  <pre><code class="lang-sh">sudo apt <span class="hljs-keyword">update</span> &amp;&amp; sudo apt <span class="hljs-keyword">install</span> espeak ffmpeg libespeak1
  </code></pre>
  <h2 id="roadmap">Roadmap</h2>
  <ul>
  <li>speech speed control</li>
  <li>Support more extensions</li>
  <li>save the audiobook for future</li>
  </ul>
  <h2 id="project-status">Project status</h2>
  <ul>
  <li>Alpha</li>
  </ul>
  <h2 id="author">Author</h2>
  <ul>
  <li>Module : AudioBook</li>
  <li>Author  : CodePerfectPlus</li>
  <li>Language : Python</li>
  </ul>
  <p><img align="right" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=for-the-badge"></p>
  