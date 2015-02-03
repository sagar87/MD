import cPickle, base64
try:
	from SimpleSession.versions.v62 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 10, 1, 40427])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v62 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDGFyb21hdGljTW9kZXEISwFLAX2HVQp2ZHdEZW5zaXR5cQlLAUdAFAAAAAAAAH2HVQZoaWRkZW5xCksBiX2HVQ1hcm9tYXRpY0NvbG9ycQtLAU59h1UPcmliYm9uU21vb3RoaW5ncQxLAUsAfYdVCWF1dG9jaGFpbnENSwGIfYdVCG9wdGlvbmFscQ59VQ9sb3dlckNhc2VDaGFpbnNxD0sBiX2HVQlsaW5lV2lkdGhxEEsBR0AAAAAAAAAAfYdVD3Jlc2lkdWVMYWJlbFBvc3ERSwFLAH2HVQRuYW1lcRJLAVgHAAAAc2NyYXRjaH2HVQ9hcm9tYXRpY0Rpc3BsYXlxE0sBiX2HVQ9yaWJib25TdGlmZm5lc3NxFEsBRz/pmZmZmZmafYdVCnBkYkhlYWRlcnNxFV1xFn1xF2FVA2lkc3EYSwFLAEsAhn2HVQ5zdXJmYWNlT3BhY2l0eXEZSwFHv/AAAAAAAAB9h1UQYXJvbWF0aWNMaW5lVHlwZXEaSwFLAn2HVRRyaWJib25IaWRlc01haW5jaGFpbnEbSwGIfYdVB2Rpc3BsYXlxHEsBiH2HdS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksOVQEgfYdVC2ZpbGxEaXNwbGF5cQNLDol9h1UEbmFtZXEESw5YAwAAAFNFUn1xBShYAwAAAFBST11xBihLAksFSwlLDGVYAwAAAFZBTF1xByhLA0sKZVgDAAAAUEhFXXEIKEsASwdldYdVBWNoYWlucQlLDlgBAAAAQX2HVQ5yaWJib25EcmF3TW9kZXEKSw5LAn2HVQJzc3ELSw6JiYZ9h1UIbW9sZWN1bGVxDEsOSwB9h1ULcmliYm9uQ29sb3JxDUsOSwF9cQ4oSwJOXXEPSwFLAYZxEGGGSwNOXXERSwJLAYZxEmGGSwROXXETSwNLAYZxFGGGSwVOXXEVSwRLAYZxFmGGSwZOXXEXSwVLAYZxGGGGSwdOXXEZSwZLAYZxGmGGSwhOXXEbSwdLAYZxHGGGSwlOXXEdSwhLAYZxHmGGSwpOXXEfSwlLAYZxIGGGSwtOXXEhSwpLAYZxImGGSwxOXXEjSwtLAYZxJGGGSw1OXXElSwxLAYZxJmGGSw5OXXEnSw1LAYZxKGGGdYdVBWxhYmVscSlLDlgAAAAAfYdVCmxhYmVsQ29sb3JxKksOTn2HVQhmaWxsTW9kZXErSw5LAX2HVQVpc0hldHEsSw6JfYdVC2xhYmVsT2Zmc2V0cS1LDk59h1UIcG9zaXRpb25xLl1xL0sBSw6GcTBhVQ1yaWJib25EaXNwbGF5cTFLDol9h1UIb3B0aW9uYWxxMn1VBHNzSWRxM0sOSv////99h3Uu'))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS2pOfYdVBWF0b21zcQNdcQQoXXEFKEsQSw9lXXEGKEsRSxBlXXEHKEsSSxFlXXEIKEsTSxFlXXEJKEsUSxNlXXEKKEsVSxRlXXELKEsWSxVlXXEMKEsXSxVlXXENKEsYSxdlXXEOKEsZSxhlXXEPKEsaSxllXXEQKEsbSxllXXERKEscSxtlXXESKEsdSxxlXXETKEseSx1lXXEUKEsfSx1lXXEVKEsgSx9lXXEWKEshSyBlXXEXKEsiSyFlXXEYKEsjSyFlXXEZKEskSyNlXXEaKEslSyRlXXEbKEsmSyVlXXEcKEsnSyVlXXEdKEsoSydlXXEeKEspSyhlXXEfKEsqSyllXXEgKEsrSyllXXEhKEssSytlXXEiKEstSyxlXXEjKEsuSy1lXXEkKEsvSy1lXXElKEswSy9lXXEmKEsxSzBlXXEnKEsySzFlXXEoKEszSzFlXXEpKEs0SzNlXXEqKEs1SzRlXXErKEs2SzVlXXEsKEs3SzVlXXEtKEs4SzdlXXEuKEs5SzhlXXEvKEs6SzllXXEwKEs7SzllXXExKEs8SztlXXEyKEs9SzxlXXEzKEs+Sz1lXXE0KEs/Sz1lXXE1KEtASz9lXXE2KEtBS0BlXXE3KEtCS0FlXXE4KEtDS0FlXXE5KEtES0NlXXE6KEtFS0RlXXE7KEtGS0VlXXE8KEtHS0VlXXE9KEtISxBlXXE+KEtJS0hlXXE/KEtKS0llXXFAKEtLS0llXXFBKEtMS0tlXXFCKEtNS0xlXXFDKEtOS01lXXFEKEtOS0plXXFFKEtPSxRlXXFGKEtQS09lXXFHKEtRSxhlXXFIKEtSS1FlXXFJKEtTS1JlXXFKKEtTSxdlXXFLKEtUSxxlXXFMKEtVS1RlXXFNKEtWS1RlXXFOKEtXSyBlXXFPKEtYS1dlXXFQKEtZSyRlXXFRKEtaS1llXXFSKEtbS1plXXFTKEtbSyNlXXFUKEtcSyhlXXFVKEtdS1xlXXFWKEteSyxlXXFXKEtfS15lXXFYKEtgS19lXXFZKEthS19lXXFaKEtiS2FlXXFbKEtjS2JlXXFcKEtkS2NlXXFdKEtkS2BlXXFeKEtlSzBlXXFfKEtmS2VlXXFgKEtnSzRlXXFhKEtoS2dlXXFiKEtpS2hlXXFjKEtpSzNlXXFkKEtqSzhlXXFlKEtrS2plXXFmKEtsS2plXXFnKEttSzxlXXFoKEtuS21lXXFpKEtvS0BlXXFqKEtwS29lXXFrKEtxS3BlXXFsKEtxSz9lXXFtKEtyS0RlXXFuKEtzS3JlZVUFbGFiZWxxb0tqWAAAAAB9h1UIaGFsZmJvbmRxcEtqiH2HVQZyYWRpdXNxcUtqRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cXJLak59h1UIZHJhd01vZGVxc0tqSwB9h1UIb3B0aW9uYWxxdH1VB2Rpc3BsYXlxdUtqSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), 'firebrick': ((0.698039, 0.133333, 0.133333), 1, u'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), 'Rf': ((0.8, 0, 0.34902), 1, u'default'), 'Ra': ((0, 0.490196, 0), 1, u'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), 'Be': ((0.760784, 1, 0), 1, u'default'), 'Ba': ((0, 0.788235, 0), 1, u'default'), 'Bh': ((0.878431, 0, 0.219608), 1, u'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), 'H': ((1, 1, 1), 1, u'default'), 'Dy': ((0.121569, 1, 0.780392), 1, u'default'), 'P': ((1, 0.501961, 0), 1, u'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), 'Gd': ((0.270588, 1, 0.780392), 1, u'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), 'Pr': ((0.85098, 1, 0.780392), 1, u'default'),
'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), 'Pu': ((0, 0.419608, 1), 1, u'default'), 'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), 'Pa': ((0, 0.631373, 1), 1, u'default'), 'Pd': ((0, 0.411765, 0.521569), 1, u'default'), 'Cd': ((1, 0.85098, 0.560784), 1, u'default'), 'Po': ((0.670588, 0.360784, 0), 1, u'default'), 'Pm': ((0.639216, 1, 0.780392), 1, u'default'), 'Hs': ((0.901961, 0, 0.180392), 1, u'default'), 'Ho': ((0, 1, 0.611765), 1, u'default'), 'Hf': ((0.301961, 0.760784, 1), 1, u'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), 'He': ((0.85098, 1, 1), 1, u'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), 'Mg': ((0.541176, 1, 0), 1, u'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), 'O': ((1, 0.0509804, 0.0509804), 1, u'default'), 'Mt': ((0.921569, 0, 0.14902), 1, u'default'), 'S': ((1, 1, 0.188235), 1, u'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'),
'Eu': ((0.380392, 1, 0.780392), 1, u'default'), 'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), 'Er': ((0, 0.901961, 0.458824), 1, u'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), 'Nd': ((0.780392, 1, 0.780392), 1, u'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), 'Np': ((0, 0.501961, 1), 1, u'default'), 'Fr': ((0.258824, 0, 0.4), 1, u'default'), 'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), 'B': ((1, 0.709804, 0.709804), 1, u'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), 'Sr': ((0, 1, 0), 1, u'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), 'Sm': ((0.560784, 1, 0.780392), 1, u'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, u'default'),
'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), 'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), 'Sg': ((0.85098, 0, 0.270588), 1, u'default'), 'Se': ((1, 0.631373, 0), 1, u'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), 'Ca': ((0.239216, 1, 0), 1, u'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), 'Ce': ((1, 1, 0.780392), 1, u'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), 'Tm': ((0, 0.831373, 0.321569), 1, u'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), 'La': ((0.439216, 0.831373, 1), 1, u'default'), 'Li': ((0.8, 0.501961, 1), 1, u'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), 'Lu': ((0, 0.670588, 0.141176), 1, u'default'), 'Lr': ((0.780392, 0, 0.4), 1, u'default'), 'Th': ((0, 0.729412, 1), 1, u'default'), 'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'),
'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), 'Te': ((0.831373, 0.478431, 0), 1, u'default'), 'Tb': ((0.188235, 1, 0.780392), 1, u'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), 'Ta': ((0.301961, 0.65098, 1), 1, u'default'), 'Yb': ((0, 0.74902, 0.219608), 1, u'default'), 'Db': ((0.819608, 0, 0.309804), 1, u'default'), 'navy blue': ((0, 0, 0.501961), 1, u'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), 'I': ((0.580392, 0, 0.580392), 1, u'default'), 'U': ((0, 0.560784, 1), 1, u'default'), 'Y': ((0.580392, 1, 1), 1, u'default'), 'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), 'Au': ((1, 0.819608, 0.137255), 1, u'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, u'default'),
'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((1, 1, 1), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 18, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (21, (u'', (0, 0.307692, 1, 1)), {(u'green', (0, 1, 0, 1)): [20], (u'', (0.461538, 1, 0, 1)): [9], (u'', (1, 0.615385, 0, 1)): [12], (u'', (0, 1, 0.153846, 1)): [7], (u'', (0, 0.923077, 1, 1)): [4], (u'O', (1, 0.0509804, 0.0509804, 1)): [16], (u'', (1, 0.307692, 0, 1)): [13], (u'black', (0, 0, 0, 1)): [19], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'N', (0.188235, 0.313725, 0.972549, 1)): [15], (u'red', (1, 0, 0, 1)): [14], (u'', (0, 0.615385, 1, 1)): [3], (u'', (0.153846, 1, 0, 1)): [8], (u'', (0.769231, 1, 0, 1)): [10], (u'yellow', (1, 1, 0, 1)): [18], (u'C', (0.564706, 0.564706, 0.564706, 1)): [17], (u'', (0, 1, 0.769231, 1)): [5], (u'', (1, 0.923077, 0, 1)): [11], (u'blue', (0, 0, 1, 1)): [1], (u'', (0, 1, 0.461538, 1)): [6]})
	viewerInfo = {'cameraAttrs': {'center': (-1.6445754123434, -1.6874403207658, 2.8086079087528), 'fieldOfView': 40.246463653063, 'nearFar': (24.137902681392, -21.030569744024), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 2.8086079087528}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 17.389741785199, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 20, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 19}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v62 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = []
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'Chimera default', 'rounded', u'amino acid'), (2, 'Chimera default', 'rounded', u'amino acid'), (3, 'Chimera default', 'rounded', u'amino acid'), (4, 'Chimera default', 'rounded', u'amino acid'), (5, 'Chimera default', 'rounded', u'amino acid'), (6, 'Chimera default', 'rounded', u'amino acid'), (7, 'Chimera default', 'rounded', u'amino acid'), (8, 'Chimera default', 'rounded', u'amino acid'), (9, 'Chimera default', 'rounded', u'amino acid'), (10, 'Chimera default', 'rounded', u'amino acid'), (11, 'Chimera default', 'rounded', u'amino acid'), (12, 'Chimera default', 'rounded', u'amino acid'), (13, 'Chimera default', 'rounded', u'amino acid'), (14, 'Chimera default', 'rounded', u'amino acid')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (1.0, 1.0, 1.0), 1], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.35740674433659325, 0.6604015517481454, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310293), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


try:
	from BuildStructure.gui import _sessionRestore
	_sessionRestore({'mapped': 0})
except:
	reportRestoreError("Failure restoring Build Structure")


def restoreRemainder():
	from SimpleSession.versions.v62 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1920, 1106)
	xformMap = {0: (((0.22586606077671, 0.77537123659771, -0.58973211549495), 34.932138580781), (-1.5205766140979, -0.022196517053217, -1.0306398745412), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 222: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v62 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v62 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

