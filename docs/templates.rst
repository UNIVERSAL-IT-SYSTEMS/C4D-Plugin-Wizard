About Templates 
===============

A template is a blueprint folder structure containing the files and directories representing one type of plugin that can be created, e.g. tag plugin, command plugin, etc. 

While there usually is a predetermined layout of directories and subdirectories for each plugin type (see C4D docs), the actual contents of any file is of course up to the user. 

When the template is read and a new plugin created, the wizard performs replacements of **magic tokens** and **rules** in the files and folder names of the template folder structure, as well as the contents of any file. 

Magic tokens are specific text snippets enclosed by the starting character sequence **%!** and the ending character sequence **!%**.
 
The text snippets that can be used inbetween are called **datum points** and are predetermined. Datum points can also have **alternative forms** into which they will be transformed. 

For example one datum point might be the plugin name as entered by the user and one transformation might be an uppercase transformation, called the **UppercaseID** form. 
A complete magic token of the previous example would be **PluginName**, additionally with the alternative form: **PluginNameAsUppercaseID**. 

Note the adverb **As** that separates the datum point from the alternative form. 

**Rules** on the other hand are read from a Python file called, **rules.py** that can reside in the data directory or in each template directory. This file won't be copied but a Python dictionary type variable named **RULES** will be read from it and the wizard will then perform searches looking for any text strings named the same as the keys of the RULES dict and will then perform replacements with the corresponding values. 

So, if you have a file called ``%!PluginNameAsUppercaseID!%.pyp`` in one of your templates and you enter ``Super Awesome Plugin`` as the plugin name in the wizard, the file will be renamed to ``SUPERAWESOMEPLUGIN.pyp``

Likewise, suppose your **rules.py** file contains the following **RULES** dict: 

.. code::
	
	import time

	RULES = {
	    '${YEAR}': time.strftime("%Y"),
	    'COMPANY': 'My Company'
	}

The wizard will now replace any occurrences of ``${YEAR}`` with the current year as returned by ``time.strftime`` and any occurrence of ``COMPANY`` with ``'My Company'``. 
Again, this includes files and directory names as well as file contents. 

See also :ref:`tips`.