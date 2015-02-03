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
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksOVQEgfYdVC2ZpbGxEaXNwbGF5cQNLDol9h1UEbmFtZXEESw5YAwAAAFNFUn1xBShYAwAAAFBST11xBihLAksFSwlLDGVYAwAAAFZBTF1xByhLA0sKZVgDAAAAVFlSXXEIKEsASwdldYdVBWNoYWlucQlLDlgBAAAAQX2HVQ5yaWJib25EcmF3TW9kZXEKSw5LAn2HVQJzc3ELSw6JiYZ9h1UIbW9sZWN1bGVxDEsOSwB9h1ULcmliYm9uQ29sb3JxDUsOTn2HVQVsYWJlbHEOSw5YAAAAAH2HVQpsYWJlbENvbG9ycQ9LDk59h1UIZmlsbE1vZGVxEEsOSwF9h1UFaXNIZXRxEUsOiX2HVQtsYWJlbE9mZnNldHESSw5OfYdVCHBvc2l0aW9ucRNdcRRLAUsOhnEVYVUNcmliYm9uRGlzcGxheXEWSw6JfYdVCG9wdGlvbmFscRd9VQRzc0lkcRhLDkr/////fYd1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS2xOfYdVBWF0b21zcQNdcQQoXXEFKEsQSw9lXXEGKEsRSxBlXXEHKEsSSxFlXXEIKEsTSxFlXXEJKEsUSxNlXXEKKEsVSxRlXXELKEsWSxVlXXEMKEsXSxVlXXENKEsYSxdlXXEOKEsZSxhlXXEPKEsaSxllXXEQKEsbSxllXXERKEscSxtlXXESKEsdSxxlXXETKEseSx1lXXEUKEsfSx1lXXEVKEsgSx9lXXEWKEshSyBlXXEXKEsiSyFlXXEYKEsjSyFlXXEZKEskSyNlXXEaKEslSyRlXXEbKEsmSyVlXXEcKEsnSyVlXXEdKEsoSydlXXEeKEspSyhlXXEfKEsqSyllXXEgKEsrSyllXXEhKEssSytlXXEiKEstSyxlXXEjKEsuSy1lXXEkKEsvSy1lXXElKEswSy9lXXEmKEsxSzBlXXEnKEsySzFlXXEoKEszSzFlXXEpKEs0SzNlXXEqKEs1SzRlXXErKEs2SzVlXXEsKEs3SzVlXXEtKEs4SzdlXXEuKEs5SzhlXXEvKEs6SzllXXEwKEs7SzllXXExKEs8SztlXXEyKEs9SzxlXXEzKEs+Sz1lXXE0KEs/Sz1lXXE1KEtASz9lXXE2KEtBS0BlXXE3KEtCS0FlXXE4KEtDS0FlXXE5KEtES0NlXXE6KEtFS0RlXXE7KEtGS0VlXXE8KEtHS0VlXXE9KEtISxBlXXE+KEtJS0hlXXE/KEtKS0llXXFAKEtLS0llXXFBKEtMS0tlXXFCKEtNS0xlXXFDKEtOS01lXXFEKEtPS01lXXFFKEtPS0plXXFGKEtQSxRlXXFHKEtRS1BlXXFIKEtSSxhlXXFJKEtTS1JlXXFKKEtUS1NlXXFLKEtUSxdlXXFMKEtVSxxlXXFNKEtWS1VlXXFOKEtXS1VlXXFPKEtYSyBlXXFQKEtZS1hlXXFRKEtaSyRlXXFSKEtbS1plXXFTKEtcS1tlXXFUKEtcSyNlXXFVKEtdSyhlXXFWKEteS11lXXFXKEtfSyxlXXFYKEtgS19lXXFZKEthS2BlXXFaKEtiS2BlXXFbKEtjS2JlXXFcKEtkS2NlXXFdKEtlS2RlXXFeKEtmS2RlXXFfKEtlS2FlXXFgKEtnSzBlXXFhKEtoS2dlXXFiKEtpSzRlXXFjKEtqS2llXXFkKEtrS2plXXFlKEtrSzNlXXFmKEtsSzhlXXFnKEttS2xlXXFoKEtuS2xlXXFpKEtvSzxlXXFqKEtwS29lXXFrKEtxS0BlXXFsKEtyS3FlXXFtKEtzS3JlXXFuKEtzSz9lXXFvKEt0S0RlXXFwKEt1S3RlZVUFbGFiZWxxcUtsWAAAAAB9h1UIaGFsZmJvbmRxcktsiH2HVQZyYWRpdXNxc0tsRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cXRLbE59h1UIZHJhd01vZGVxdUtsSwB9h1UIb3B0aW9uYWxxdn1VB2Rpc3BsYXlxd0tsSwJ9h3Uu'))
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
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 4, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (7, (u'green', (0, 1, 0, 1)), {(u'N', (0.188235, 0.313725, 0.972549, 1)): [1], (u'O', (1, 0.0509804, 0.0509804, 1)): [2], (u'black', (0, 0, 0, 1)): [5], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'yellow', (1, 1, 0, 1)): [4], (u'C', (0.564706, 0.564706, 0.564706, 1)): [3]})
	viewerInfo = {'cameraAttrs': {'center': (-1.3236782593836, -2.0847760974122, 2.3998743827034), 'fieldOfView': 40.246463653063, 'nearFar': (24.110563617095, -21.039729674835), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 2.3998743827034}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 18.229008106025, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 6, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 5}

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
	_sessionRestore({'mapped': 1})
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
	xformMap = {0: (((0.23455958140744, 0.96614649244174, -0.10743722777739), 35.113287790339), (-1.8435256718954, 0.53872687086593, -0.93253756175632), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 226: True}

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

