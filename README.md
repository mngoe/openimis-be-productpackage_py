# openIMISS Backend productpackage reference module
This repository holds the files of the openIMIS Backend productpackage reference module. It is dedicated to be deployed as a module of [openimis-be_py](https://github.com/openimis/openimis-be_py). 
 Start creating openimis-be-productpackage_py module.
1- from an empty repository folder (The case we have used)
  a) clone the repository or donwload the file (productpackage)
  b) checkout to the develop branch by executing the command: git checkout develop or create a new develop branch
   if not created with the command git checkout -b develop (used in our case)
  c) within openimis-be-productpackage_py, create the sub repository named productpackage
  d) prepare your module to be mounted via pip: create and 
  complete the /openimis-be-productpackage_py/ by creating or copying the setup.py, MANIFEST.in, 
  LICENSE.md and README.md (if not created), ... files (the files could be copied from product module and 
  being adpted to productpackage module needs.
  e) create the file /openimis-be-productpackagee_py/productpackage/urls.py (even empty) 
   with content: urlpatterns = []
  f) from /openimis-be_py/openIMIS: register your module in the pip requirements of openIMIS,
    referencing your 'local' codebase: pip install -e ../../openimis-be-roductpackage_py/
  g) register your module to openIMIS django site in /openimis-be_py/openimis.json

2- Without having an empty repository
  follow the link : 
  https://github.com/mngoe/openimis-be_py/tree/develop 
  and at To create a new openIMIS module (e.g. openimis-be-mymodule) part