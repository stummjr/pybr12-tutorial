.. _intro-install:

==================
Guia de Instalação
==================

Instalando o Scrapy
===================

O Scrapy roda em Python 2.7 e 3.3 ou maior (exceto no Windows onde Python 3
ainda não é suportado).

Se você já é familiar com a instalação de pacotes Python, você pode instalar o
Scrapy e suas dependências executando::

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
usuário. Nós recomendamos que você **não** instale o Scrapy globalmente no sistema.

Ao invés disso, recomendamos que instale o Scrapy dentro do que chamamos de
"virtualenv" (`virtualenv`_).
Virtualenvs permitem que os pacotes que você instala não conflitem com os pacotes
já instalados no seu sistema (o que poderia quebrar algumas das suas ferramentas e
scripts do sistema), e também permite a instalação normal usando ``pip`` (sem 
permissões de super-usuário).

Para começar com virtualenvs, veja as `instruções de instalação do Virtualenv`_.
Para instalar o virtualenv globalmente (o que neste caso é útil), basta executar::

    $ [sudo] pip install virtualenv

Verifique este `guia de usuário`_ para aprender como criar um ambiente virtual.

**Nota**: Se você usa Linux ou OS X, o `virtualenvwrapper`_ é uma mão na roda para gerenciar vittualenvs.

Uma vez que tenha criado um virtualenv, você pode instalar o Scrapy dentro dele usando o ``pip``,
como faria com qualquer outro pacote Python.

(Veja :ref:`os guias específicos por plataforma <intro-install-platform-notes>`
abaixo para as dependências "não-Python que você talvez precise instalar).

Virtualenvs Python podem ser criados usando Python 2 ou 3 por padrão.

* Se você quiser instalar o Scrapy com Python 3, instale ele dentro de um virtualenv Python 3.
* E se você quiser instalar o Scrapy com Python 2, instale ele dentro de um virtualenv Python 2.

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

  Você precisa ajustar a variável de ambiente ``PATH``, incluindo caminhos para o 
  executável do interpretador Python e dos scripts adicionais. Os seguintes caminhos
  devem ser incluídos no ``PATH``::

      C:\Python27\;C:\Python27\Scripts\;

  O que pode ser feito executando o seguinte comando::

      c:\python27\python.exe c:\python27\tools\scripts\win_add2path.py

  Após executar tal comando, feche o prompt de comando e abra novamente de forma
  que as alterações sejam aplicadas. Feito isso, execute o seguinte comando e verifique se
  ele mostra a versão esperada do Python::

      python --version

* Instale `pywin32` (http://sourceforge.net/projects/pywin32/)

  Baixe o pacote específico para a sua arquiteture (win32 ou amd64).

* *(Apenas para Python < 2.7.9)* Instale o `pip`_(https://pip.pypa.io/en/latest/installing/)

  Abra um prompt de comando para verificar se o ``pip`` foi instalado corretamente::

      pip --version

* Neste ponto, Python 2.7 e ``pip`` devem estar funcionando. Então vamos instalar o Scrapy::

      pip install Scrapy

**Nota: Python 3 não é suportado no Windows. Isto acontece porque o Twisted, que é uma dependência do
     Scrapy, não suporta Python 3 no Windows.


Ubuntu 12.04 ou mais recente
----------------------------
O Scrapy é atualmente testado com versões recentes o suficiente do lxml, twisted e pyOpenSSL,
e é compatível com distribuições Ubuntu recentes.

**Não use o pacote ``python-scrapy`` disponível no Ubuntu**, pois ela está severamente
desatualizada.

Para instalar o Scrapy no Ubuntu (ou sistemas baseados nele), você primeiramente precisa instalar as suas dependências::

    sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

- ``python-dev``, ``zlib1g-dev``, ``libxml2-dev`` e ``libxslt1-dev``
  são necessárias para o ``lxml``
- ``libssl-dev`` e ``libffi-dev`` são necessárias para o ``cryptography``

Se você quer instalar o Scrapy em Python 3, você irá precisar também dos
cabeçalhos de desenvolvimento do Python 3:: 

    sudo apt-get install python3 python3-dev

Feito isso, você pode instalar o Scrapy usando o ``pip``::

    pip install scrapy


Mac OS X
--------

A construção das dependências do Scrapy necessitam da presença de um compilador C e
dos cabeçalhos de desenvolvimento. Ambos são tipicamente fornecidos pelas ferramentas de 
desenvolvimento do Xcode. Para instalar as ferramentas da linha de comando do Xcode,
abra um terminal e execute::

    xcode-select --install

Existe um `problema conhecido <https://github.com/pypa/pip/issues/2468>`_ que
não permite que o ``pip`` atualize pacotes do sistema. Isso deve ser ajustado
para instalar o Scrapy e suas dependências. Aqui seguem algumas possíveis soluções:

* *(Recomendada)* **Não** use o Python que vem instalado no OSX. Ao invés disso, instale
  uma versão atualizada que não conflite com o resto do seu sistema. Você pode fazer isso
  usando o gerenciador de pacotes `homebrew`_:

  * Siga as instruções descritas em http://brew.sh/ para instalar o `homebrew`_ 

  * Atualize sua variável de ambiente ``PATH`` para dar prioridade aos pacotes instalados via
    homebrew (Substitua ``.bashrc`` por ``.zshrc`` se estiver usando o `zsh`_)::

      echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bashrc

  * Recarregue o ``.bashrc`` pra garantir que as alterações tenham efeito::

      source ~/.bashrc

  * Instale python::

      brew install python

  * As versões mais recentes de Python já vem com o ``pip`` incluso. Se esse não
    for o seu caso, atualize python::

      brew update; brew upgrade python

* *(Opcional)* Instale o Scrapy dentro de um ambiente virtual python isolado.

  `virtualenv`_ é uma ferramenta para a criação de ambiente virtuais isolados Python.
  Recomendamos que leia
  http://docs.python-guide.org/en/latest/dev/virtualenvs/ para começar.

Depois de qualquer um dos workarounds acima terem sido aplicadas, você deve estar apto a 
instalar o Scrapy::

  pip install Scrapy


Anaconda
--------

Anaconda é uma alternativa à dupla virtualenv + pip.

**Nota:** este é o modo recomendado para instalação do Scrapy caso você esteja no Windows ou caso tenha problemas instalando via pip.

Para instalar o Scrapy usando ``conda``, execute::

  conda install -c scrapinghub scrapy

Este documento é uma tradução do `guia de instalação oficial do Scrapy <https://doc.scrapy.org/en/latest/intro/install.html>`_.

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