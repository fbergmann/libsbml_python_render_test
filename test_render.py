import unittest
import libsbml
import sys


STYLE_SHEET = 'SBGNstyles_31.xml'

print('Using libSBML: %s' % libsbml.getLibSBMLDottedVersion())
print('Using Python: %s' % sys.version)


class TestRender(unittest.TestCase):

    def test_version(self):
        assert libsbml.getLibSBMLDottedVersion() == '5.18.1'

    def test_libsbml_has_render(self):
        ns = libsbml.RenderPkgNamespaces(3, 1)
        assert ns is not None

    def test_libsbml_has_layout(self):
        ns = libsbml.LayoutPkgNamespaces(3, 1)
        assert ns is not None

    def test_sbase_has_read(self):
        compartment = libsbml.Compartment(3, 1)
        assert compartment is not None
        stream = libsbml.XMLInputStream("""<?xml version="1.0" encoding="utf-8"?>
        <compartment id="vol1" name="compartment 1" size="2.0" />""", False)
        compartment.read(stream)
        assert compartment.id == 'vol1'
        assert compartment.name == 'compartment 1'
        assert compartment.volume == 2.0

    def test_downcast_polygon(self):
        group = libsbml.RenderGroup(3, 1)
        stream = libsbml.XMLInputStream("""<?xml version="1.0" encoding="utf-8"?>
      <g stroke="black" stroke-width="0.1" fill="black">
        <polygon>
          <listOfElements>
            <element xsi:type="RenderPoint"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" x="0.0" y="0.0"/>
            <element xsi:type="RenderPoint"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" x="0.3" y="0.0"/>
            <element xsi:type="RenderPoint" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  x="0.3" y="8.0"/>
            <element xsi:type="RenderPoint"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" x="0.0" y="8.0"/>
          </listOfElements>
        </polygon>
      </g>        """, False)
        group.read(stream)
        assert group.stroke == 'black'
        assert group.fill == 'black'
        assert group.stroke_width == 0.1
        assert group.getNumElements() > 0

        p = group.getElement(0)
        assert isinstance(p, libsbml.Polygon)
        for elt in p.getListOfElements():
            assert(isinstance(elt, libsbml.RenderPoint))    

    def test_read_stylesheet_31(self):
        info = libsbml.LocalRenderInformation(3, 1)
        stream = libsbml.XMLInputStream(STYLE_SHEET, True)
        info.read(stream)
        assert info.id == 'SBGN_default'
        line = info.getLineEnding('inhibitor')
        assert isinstance(line, libsbml.LineEnding)
        assert line.id == 'inhibitor'
        group = line.getGroup()
        assert isinstance(group, libsbml.RenderGroup)
        assert group.stroke == 'black'
        assert group.fill == 'black'
        assert group.stroke_width == 0.1
        assert group.getNumElements() > 0

        p = group.getElement(0)
        assert isinstance(p, libsbml.Polygon)
        for elt in p.getListOfElements():
            assert(isinstance(elt, libsbml.RenderPoint))    

    def test_read_stylesheet_24(self):
        info = libsbml.LocalRenderInformation(2, 4)
        stream = libsbml.XMLInputStream(STYLE_SHEET, True)
        info.read(stream)
        assert info.id == 'SBGN_default'
        line = info.getLineEnding('inhibitor')
        assert isinstance(line, libsbml.LineEnding)
        assert line.id == 'inhibitor'
        group = line.getGroup()
        assert isinstance(group, libsbml.RenderGroup)
        assert group.stroke == 'black'
        assert group.fill == 'black'
        assert group.stroke_width == 0.1
        assert group.getNumElements() > 0

        p = group.getElement(0)
        assert isinstance(p, libsbml.Polygon)
        for elt in p.getListOfElements():
            assert(isinstance(elt, libsbml.RenderPoint))    


if __name__ == '__main__':
    unittest.main()
