import vtk, sys

__all__ = []


####################################################################################
def tips():
    from vedo import colors, __version__
    msg  = " ==========================================================\n"
    msg += "| Press: i     print info about selected object            |\n"
    msg += "|        I     print the RGB color under the mouse         |\n"
    msg += "|        <-->  use arrows to reduce/increase opacity       |\n"
    msg += "|        w/s   toggle wireframe/surface style              |\n"
    msg += "|        p/P   change point size of vertices               |\n"
    msg += "|        l     toggle edges visibility                     |\n"
    msg += "|        x     toggle mesh visibility                      |\n"
    msg += "|        X     invoke a cutter widget tool                 |\n"
    msg += "|        1-2   change mesh color                           |\n"
    msg += "|        3     change mesh texture                         |\n"
    msg += "|        4     use data array as colors, if present        |\n"
    msg += "|        5-6   change background color(s)                  |\n"
    msg += "|        09+-  (on keypad) or +/- to cycle axes style      |\n"
    msg += "|        k     cycle available lighting styles             |\n"
    msg += "|        K     cycle available shading styles              |\n"
    msg += "|        A     toggle anti-aliasing                        |\n"
    msg += "|        D     toggle depth-peeling (for transparencies)   |\n"
    msg += "|        o/O   add/remove light to scene and rotate it     |\n"
    msg += "|        n     show surface mesh normals                   |\n"
    msg += "|        a     toggle interaction to Actor Mode            |\n"
    msg += "|        j     toggle interaction to Joystick Mode         |\n"
    msg += "|        r     reset camera position                       |\n"
    msg += "|        C     print current camera settings               |\n"
    msg += "|        S     save a screenshot                           |\n"
    msg += "|        E     export rendering window to numpy file       |\n"
    msg += "|        q     return control to python script             |\n"
    msg += "|        Esc   abort execution and exit python kernel      |\n"
    msg += "|----------------------------------------------------------|\n"
    msg += "| Mouse: Left-click    rotate scene / pick actors          |\n"
    msg += "|        Middle-click  pan scene                           |\n"
    msg += "|        Right-click   zoom scene in or out                |\n"
    msg += "|        Cntrl-click   rotate scene                        |\n"
    msg += "|----------------------------------------------------------|\n"
    msg += "| Check out documentation at:  https://vedo.embl.es        |\n"
    msg += " =========================================================="
    colors.printc(msg, dim=1)

    msg = " vedo " + __version__ + " "
    colors.printc(msg, invert=1, dim=1, end="")
    vtkVers = vtk.vtkVersion().GetVTKVersion()
    msg = "| vtk " + str(vtkVers)
    msg += " | python " + str(sys.version_info[0]) + "." + str(sys.version_info[1])
    colors.printc(msg, invert=0, dim=1)

####################################################################################
# example web page for X3D
x3d_html = """
<html>
<head>
    <title> My X3DOM web page </title>
    <script type='text/javascript' src='https://www.x3dom.org/download/x3dom.js'> </script>
    <link rel='stylesheet' type='text/css' href='https://www.x3dom.org/download/x3dom.css'/>
</head>
<body><font face="Verdana" size="3">

<h1>My x3d rendering web page</h1>
<p>
    This example loads a 3D scene from file ~fileoutput generated by
    <a href="https://github.com/marcomusy/vedo">vedo</a>
    (see e.g. <a href="https://github.com/marcomusy/vedo/tree/master/examples/other/export_x3d.py">export_x3d.py</a>).

    <br/>
    <br/> - Press t to reset viewpoint.
    <br/> - Press i to reset camera distance.
    <br/> - Right-click and drag mouse to zoom.
    <br/> - Middle-click and drag mouse to pan.
</p>

<x3d width='~widthpx' height='~heightpx'>
    <scene>
        <Inline url="~fileoutput" />
    </scene>
</x3d>

<br clear="all">
<br/>PS: This should work with Firefox/IE.
With Chrome, webgl might not be active by default, then try:<br/><i>
google-chrome --enable-webgl --use-gl=desktop
--log-level=0 --allow-file-access-from-files --allow-file-access ~fileoutput
</i>
</font></body>
</html>
"""


####################################################################################
_defs = ""

##### to generate documentation must uncomment this line:
# from vedo.docs_defs import _substitutions_defs as _defs

# Then:
    # cd vedo/docs
    # pip install -r requirements.txt # optionally
    # make html

####################################################################################
