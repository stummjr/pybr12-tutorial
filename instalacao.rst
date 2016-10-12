.. _intro-install:

==================
Guia de Instalação
==================

Instalando o Scrapy
===================

Scrapy roda em Python 2.7 e 3.3 ou maior (exceto no Windows onde Python 3
ainda não é suportado).

Se você já é familiar com a instalação de pacotes Python, você pode instalar o
Scrapy e suas dependências::

    pip install Scrapy

Nós recomendamos fortemente que você instale o Scrapy em :ref:`um virtualenv dedicado <intro-using-virtualenv>`, para evitar conflitos com os pacotes do seu sistema.

Para instruções detalhadas e específicas sobre uma plataforma, continue lendo.


Coisas que é bom ficar sabendo
------------------------------

O Scrapy é escrito em Python puro e depende de alguns poucos pacotes Python (entre outros):

* `lxml`_, um parser XML e HTML eficiente
* `parsel`_, uma biblioteca de extração de dados de HTML/XML escrito com base no ``lxml``
* `w3lib`_, uma biblioteca com helpers para lidar com URLs e codificação de páginas
* `twisted`_, um framework assíncrono de networking
* `cryptography`_ e `pyOpenSSL`_, para lidar com várias necessidades de segurança no nível de rede

O Scrapy é testado com as seguintes versões mínimas de pacotes:

* Twisted 14.0
* lxml 3.4
* pyOpenSSL 0.14
O Scrapy pode até funcionar com versões mais antigas desses pacotes, mas não é
garantido que continuará funcionando, dado que ele não é testato usando tais
versões.

Alguns desse pacotes dependem de pacotes não escritos em Python que podem requerer
passos adicionais de instalação dependendo da sua plataforma.
Por favor, verifique :ref:`os guias específicos para plataformas abaixo <intro-install-platform-notes>`.

Caso tenha algum problema relacionado com tais dependências, por favor veja as
respectivas instruções de instalação:


* `instalação do lxml`_
* `instalação do cryptography`_

.. _instalação do lxml: http://lxml.de/installation.html
.. _instalação do cryptography: https://cryptography.io/en/latest/installation/


.. _intro-using-virtualenv:

Usando um ambiente virtual - virtualenv (recomendado)
-----------------------------------------------------

TL;DR: Nós recomendamos instalar o Scrapy dentro de um ambiente virtual em
todas as plataformas.

Pacotes Python podem ser instalados tanto globalmente (sistema) ou no espaço do
usuário. Não recomendamos que você instale o Scrapy globalmente no sistema.

Ao invés disso, recomendamos que instale o Scrapy dentro do que chamamos de
"virtualenv" (`virtualenv`_).
Virtualenvs permitem que os pacotes que você instale não conflitem com os pacotes
já instalados no seu sistema (o que poderia quebrar algumas das suas ferramentas e
scripts do sistema), e também permite a instalação normal usando ``pip`` (sem 
permissões de super-usuário.

Para começar com virtualenvs, veja `instruções de instalação do Virtualenv`_.
Para instalar o virtualenv globalmente (o que neste caso é útil), basta executar::

    $ [sudo] pip install virtualenv

Verifique este `guia de usuário`_ para aprender como criar um ambiente virtual.

.. note::
    Se você usa Linux ou OS X, o `virtualenvwrapper`_ é uma mão na roda para gerenciar vittualenvs.

Uma vez que tenha criado um virtualenv, você pode instalar o Scrapy dentro dele usando o ``pip``,
como faria com qualquer outro pacote Python.

(Veja :ref:`os guias específicos por plataforma <intro-install-platform-notes>`
abaixo para as dependências não-Pythonque você talvez precise instalar).

Virtualenvs Python podem ser criados usando Python 2 ou 3 por padrão.

* Se você quiser instalar o Scrapy com Python 3, instale ele dentro de um virtualeng Python 3.
* E se você quiser instalar o Scrapy com Python 2, instale ele dentro de um virtualeng Python 2.

.. _virtualenv: https://virtualenv.pypa.io
.. _instruções de instalação do Virtualenv: https://virtualenv.pypa.io/en/stable/installation/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.io/en/latest/install.html
.. _guia de usuário : https://virtualenv.pypa.io/en/stable/userguide/


.. _intro-install-platform-notes:

Notas de instalação específicas por plataforma
==============================================

Windows
-------

* Instale Python 2.7 (https://www.python.org/downloads/)

  Você precisa ajustar a variável de ambiente ``PATH`` para incluir caminhos para o 
  executável do interpretador Python e scripts adicionais. Os seguintes caminhos
  devem ser incluídosThe following paths need to be ao ``PATH``::
  added to ``PATH``::

      C:\Python27\;C:\Python27\Scripts\;

  O que pode ser feito executando o seguinte comando::

      c:\python27\python.exe c:\python27\tools\scripts\win_add2path.py

  Feche o prompt de comando e o reabra de forma que as alterações sejam aplicadas,
  execute o seguinte comando e verifique se ele mostra a versão esperada do Python::

      python --version

* Instale `pywin32` (http://sourceforge.net/projects/pywin32/)

  Baixe o pacote específico para a sua arquiteture (win32 ou amd64).

* *(Apenas para Python < 2.7.9)* Instale o `pip`_(https://pip.pypa.io/en/latest/installing/)

  Abra um prompt de comando para verificar se o ``pip`` foi instalado corretamente::

      pip --version

* Neste ponto, Python 2.7 e ``pip`` devem estar funcionando. Então vamos instalar o Scrapy::

      pip install Scrapy

.. note::
     Python 3 não é suportado no Windoes. Isto acontece porque o Twisted, que é uma dependência do
     Scrapy, não suporta Python 3 no Windows.

Ubuntu 12.04 ou mais recente
----------------------------
O Scrapy é atualmente testado com versões recentes o suficiente do lxml, twisted e pyOpenSSL,
e é compatível com distribuições Ubuntu recentes.

**Não** use o pacote ``python-scrapy`` disponível no Ubuntu, pois ela está severamente
desatualizada.

Para instalar o Scrapy no Ubuntu (ou sistemas baseados nele), você primeiramente precisa instalar as suas dependências::

    sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

- ``python-dev``, ``zlib1g-dev``, ``libxml2-dev`` e ``libxslt1-dev``
  são necessárias para o ``lxml``
- ``libssl-dev`` e ``libffi-dev`` são necessárias para o ``cryptography``

Se você quer instalar o Scrapy em Python 3, você irá precisar também dos
cabeçalhos de desenvolvimento do Python 3:: 

    sudo apt-get install python3 python3-dev

Dentro de um :ref:`virtualenv <intro-using-virtualenv>`, você pode instalar o Scrapy
usando o ``pip`` depois disso::

    pip install scrapy


Mac OS X
--------

Building Scrapy's dependencies requires the presence of a C compiler and
development headers. On OS X this is typically provided by Apple’s Xcode
development tools. To install the Xcode command line tools open a terminal
window and run::

    xcode-select --install

There's a `known issue <https://github.com/pypa/pip/issues/2468>`_ that
prevents ``pip`` from updating system packages. This has to be addressed to
successfully install Scrapy and its dependencies. Here are some proposed
solutions:

* *(Recommended)* **Don't** use system python, install a new, updated version
  that doesn't conflict with the rest of your system. Here's how to do it using
  the `homebrew`_ package manager:

  * Install `homebrew`_ following the instructions in http://brew.sh/

  * Update your ``PATH`` variable to state that homebrew packages should be
    used before system packages (Change ``.bashrc`` to ``.zshrc`` accordantly
    if you're using `zsh`_ as default shell)::

      echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bashrc

  * Reload ``.bashrc`` to ensure the changes have taken place::

      source ~/.bashrc

  * Install python::

      brew install python

  * Latest versions of python have ``pip`` bundled with them so you won't need
    to install it separately. If this is not the case, upgrade python::

      brew update; brew upgrade python

* *(Optional)* Install Scrapy inside an isolated python environment.

  This method is a workaround for the above OS X issue, but it's an overall
  good practice for managing dependencies and can complement the first method.

  `virtualenv`_ is a tool you can use to create virtual environments in python.
  We recommended reading a tutorial like
  http://docs.python-guide.org/en/latest/dev/virtualenvs/ to get started.

After any of these workarounds you should be able to install Scrapy::

  pip install Scrapy


Anaconda
--------


Using Anaconda is an alternative to using a virtualenv and installing with ``pip``.

.. note::

  For Windows users, or if you have issues installing through ``pip``, this is
  the recommended way to install Scrapy.

If you already have `Anaconda`_ or `Miniconda`_ installed,
`Scrapinghub`_ maintains official conda packages for Linux, Windows and OS X.

To install Scrapy using ``conda``, run::

  conda install -c scrapinghub scrapy

.. _Python: https://www.python.org/
.. _pip: https://pip.pypa.io/en/latest/installing/
.. _Control Panel: https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/sysdm_advancd_environmnt_addchange_variable.mspx
.. _lxml: http://lxml.de/
.. _parsel: https://pypi.python.org/pypi/parsel
.. _w3lib: https://pypi.python.org/pypi/w3lib
.. _twisted: https://twistedmatrix.com/
.. _cryptography: https://cryptography.io/
.. _pyOpenSSL: https://pypi.python.org/pypi/pyOpenSSL
.. _setuptools: https://pypi.python.org/pypi/setuptools
.. _AUR Scrapy package: https://aur.archlinux.org/packages/scrapy/
.. _homebrew: http://brew.sh/
.. _zsh: http://www.zsh.org/
.. _Scrapinghub: http://scrapinghub.com
.. _Anaconda: http://docs.continuum.io/anaconda/index
.. _Miniconda: http://conda.pydata.org/docs/install/quick.html