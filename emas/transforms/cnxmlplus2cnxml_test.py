import os
from cnxmlplus2shortcodecnxml_standalone import cnxmlplus2cnxml

def test_cnxmlplus2cnxml():
    cnxmlplus = open(os.path.join('tests', 'test.cnxmlplus')).read()
    print cnxmlplus2cnxml(cnxmlplus)

if __name__ == "__main__":
    test_cnxmlplus2cnxml()