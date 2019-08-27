## LibSBML Render Test project
This project tests the libsbml render package, to ensure all methods are there, and things are working as they should be. 

To run the unit tests contained here, create a new virtual environment with the python version of your choice and run `python test_render.py`

### Conda
To create the virtual environment with conda use: 


	conda create -n libsbml_37 python=3.7
	conda activate libsbml_37
	pip install python-libsbml-experimental
	python test_render.py

the expected output would be: 


	Using libSBML: 5.18.1
	Using Python: 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
	.......
	----------------------------------------------------------------------
	Ran 7 tests in 0.045s

	OK

### venv
Without conda, you'd create an environment like so (on windows): 

	python -m venv libsbml_36
	.\libsbml_36\Scripts\activate.bat
	pip install python-libsbml-experimental
	python test_render.py

### using pyenv
using pyenv you'd do: 

    pyenv install 3.7.1
    pyenv virtualenv 3.7.1 libsbml
    pyenv rehash
    pyenv activate libsbml
	pip install python-libsbml-experimental
	python test_render.py



## License 
This project is open source and freely available under the [Simplified BSD](http://opensource.org/licenses/BSD-2-Clause) license. Should that license not meet your needs, please contact me. 


Copyright (c) 2019, Frank T. Bergmann  
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
