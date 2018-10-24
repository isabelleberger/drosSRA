=======
drosSRA
=======


.. image:: https://img.shields.io/pypi/v/drosSRA.svg
        :target: https://pypi.python.org/pypi/drosSRA

.. image:: https://img.shields.io/travis/isabelleberger/drosSRA.svg
        :target: https://travis-ci.org/isabelleberger/drosSRA

.. image:: https://readthedocs.org/projects/drossra/badge/?version=latest
        :target: https://drossra.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




``drosSRA`` builds a url containing all relevant GEO_ tracks based on one or more user specified parameters (i.e. sex, tissue, cell type)

* Free software: MIT license
* Documentation: https://drosSRA.readthedocs.io.

Installation
------------

To download and install the latest version of ``drosSRA``: ::

   pip install drosSRA

Usage
-----

There are five possible flags that users can use to search for tracks of interest: PubMed ID (``-p``), sex (``-s``), developmental stage (``-d``), tissue (``-t``), and cell type (``-c``).
For example, if you are interested in viewing all tracks with testis data::

   >> drosSRA -t testis
   https://www.ncbi.nlm.nih.gov/genome/gdv/browser/?context=genome&acc=GCF_000001215.4&context=GEO&acc=ERX2162339%2CERX2162340%2CERX2162341%2CSRX014984%2CSRX014985%2CSRX1026313%2CSRX1045309%2CSRX1045369%2CSRX105953%2CSRX109278%2CSRX109279%2CSRX135547%2CSRX135548%2CSRX142027%2CSRX142028%2CSRX142029%2CSRX142030%2CSRX142031%2CSRX142032%2CSRX1512980%2CSRX1542553%2CSRX1542554%2CSRX1542555%2CSRX1542556%2CSRX1542557%2CSRX1637725%2CSRX1637726%2CSRX1637727%2CSRX1637728%2CSRX1637729%2CSRX1637730%2CSRX1637731%2CSRX1637732%2CSRX1637733%2CSRX1637734%2CSRX1637735%2CSRX1637736%2CSRX1720957%2CSRX1720958%2CSRX1842650%2CSRX1842775%2CSRX2166012%2CSRX2166014%2CSRX2166016%2CSRX2166017%2CSRX2166019%2CSRX2166020%2CSRX2166021%2CSRX2325622%2CSRX2325623%2CSRX2325625%2CSRX2325626%2CSRX2325628%2CSRX2325629%2CSRX2325630%2CSRX2325631%2CSRX2416970%2CSRX2416971%2CSRX2416972%2CSRX2416973%2CSRX2416974%2CSRX2416975%2CSRX2416976%2CSRX2416977%2CSRX2497546%2CSRX2497547%2CSRX2497548%2CSRX2497549%2CSRX2497550%2CSRX2497551%2CSRX2504297%2CSRX2504298%2CSRX2504299%2CSRX2504300%2CSRX2549197%2CSRX2549198%2CSRX2549199%2CSRX2677260%2CSRX2677261%2CSRX2677262%2CSRX2677263%2CSRX2683539%2CSRX2683540%2CSRX2683541%2CSRX2683542%2CSRX2683543%2CSRX2683545%2CSRX2683546%2CSRX2683547%2CSRX2683548%2CSRX2683550%2CSRX2683551%2CSRX2829107%2CSRX2829108%2CSRX2829109%2CSRX2829110%2CSRX3015350%2CSRX3015366%2CSRX319676%2CSRX319687%2CSRX320021%2CSRX320263%2CSRX321521%2CSRX321778%2CSRX3488043%2CSRX3488044%2CSRX3488045%2CSRX3488046%2CSRX3488047

Or, if you are interested in the intersection of two or more parameters, ::

   >> drosSRA -d 'larval stage' -t CNS
    https://www.ncbi.nlm.nih.gov/genome/gdv/browser/?context=genome&acc=GCF_000001215.4&context=GEO&acc=ERX2162997%2CERX2162999

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _GEO: https://www.ncbi.nlm.nih.gov/geo/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
